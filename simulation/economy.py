import numpy as np
import itertools as it

# noinspection PyUnresolvedReferences
from simulation.model.RL.rl_agent import RLAgent


class Economy(object):

    def __init__(self, **kwargs):

        np.random.seed(kwargs.get('seed'))
        self.t_max = kwargs.get('t_max')
        self.cognitive_parameters = kwargs.get('cognitive_parameters')
        self.agent_model = kwargs.get('agent_model')
        self.repartition = np.asarray(kwargs.get('distribution'))

        self.n_goods = len(self.repartition)
        self.roles = self.get_roles(self.n_goods, kwargs.get('economy_model'))

        self.n_agent = sum(self.repartition)

        # ---- For backup ----- #
        self.bkp_in_hand = np.zeros((self.n_agent, self.t_max))
        self.bkp_desired = np.zeros((self.n_agent, self.t_max))
        self.bkp_prod = np.zeros(self.n_agent)
        self.bkp_cons = np.zeros(self.n_agent)

        # ---------- #

        self.agents = self.create_agents(kwargs.get('heterogeneous'))

        self.t = 0

        self.markets = self.get_markets(self.n_goods)
        self.exchange_types = list(it.combinations(range(self.n_goods), r=2))

    @staticmethod
    def get_markets(n_goods):

        markets = {}
        for i in it.permutations(range(n_goods), r=2):
            markets[i] = []
        return markets

    @staticmethod
    def get_roles(n_goods, model):
        """
        :param n_goods: int
        :param model: string: 'prod: i+1' or 'prod: i-1'
        :return: array of size n_goods:2 (prod / cons)
        """

        roles = np.zeros((n_goods, 2), dtype=int)
        if model == 'prod: i+1':
            for i in range(n_goods):
                roles[i] = (i+1) % n_goods, i

        elif model == 'prod: i-1':
            for i in range(n_goods):
                roles[i] = (i-1) % n_goods, i

        else:
            raise Exception(f'Model "{model}" is not defined.')

        return roles

    def create_agents(self, heterogeneous):

        agents = np.zeros(self.n_agent, dtype=object)

        idx = 0

        for agent_type, n in enumerate(self.repartition):

            i, j = self.roles[agent_type]

            for ind in range(n):
                a = eval(self.agent_model)(
                    prod=i, cons=j,
                    cognitive_parameters=
                    self.cognitive_parameters if not heterogeneous else self.cognitive_parameters[idx],
                    n_goods=self.n_goods,
                    idx=idx
                )

                agents[idx] = a

                self.bkp_prod[idx] = i
                self.bkp_cons[idx] = j

                idx += 1

        return agents

    def run(self):

        for t in range(self.t_max):
            self.time_step(t)

        return {
            'in_hand': self.bkp_in_hand,
            'desired': self.bkp_desired,
            'prod': self.bkp_prod,
            'cons': self.bkp_cons
        }

    def time_step(self, t):

        self.t = t

        self.organize_encounters()

        # Each agent consumes at the end of each round and adapt his behavior (or not).
        for agent in self.agents:
            agent.consume()

    def organize_encounters(self):

        for k in self.markets:
            self.markets[k] = []

        for agent in self.agents:

            agent_choice = agent.which_exchange_do_you_want_to_try()
            self.markets[agent_choice].append(agent.idx)

            # Bkp
            self.bkp_in_hand[agent.idx, self.t], \
                self.bkp_desired[agent.idx, self.t] = agent_choice

        success_idx = []

        for i, j in self.exchange_types:

            a1 = self.markets[(i, j)]
            a2 = self.markets[(j, i)]

            min_a = int(min([len(a1), len(a2)]))

            if min_a:

                success_idx += list(
                    np.random.choice(a1, size=min_a, replace=False)
                )
                success_idx += list(
                    np.random.choice(a2, size=min_a, replace=False)
                )

        for idx in success_idx:

            agent = self.agents[idx]
            agent.proceed_to_exchange()


def launch(**kwargs):
    e = Economy(**kwargs)
    return e.run()
