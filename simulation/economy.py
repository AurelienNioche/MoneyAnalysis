import numpy as np
import itertools as it

# noinspection PyUnresolvedReferences
from simulation.model.RL.rl_agent import RLAgent


class Economy(object):

    def __init__(self, t_max, cognitive_parameters, agent_model='RLAgent', distribution=None,
                 economy_model='prod: i-1', seed=123, heterogeneous=False, prod=None, cons=None):

        np.random.seed(seed)
        self.t_max = t_max
        self.cognitive_parameters = cognitive_parameters
        self.agent_model = agent_model

        self.n_goods, self.n_agent, self.agents, self.prod, self.cons = \
            self.create_agents(economy_model=economy_model,
                               heterogeneous=heterogeneous, distribution=distribution,
                               prod=prod, cons=cons)

        # ---- For backup ----- #
        self.in_hand = np.zeros((self.n_agent, self.t_max), dtype=int)
        self.desired = np.zeros((self.n_agent, self.t_max), dtype=int)
        self.success = np.zeros((self.n_agent, self.t_max), dtype=bool)

        # ---------- #

        self.t = 0

        self.markets = self.get_markets(self.n_goods)
        self.exchange_types = list(it.combinations(range(self.n_goods), r=2))

    def create_agents(self, economy_model, heterogeneous, distribution, prod, cons):

        if distribution is not None:

            n_goods = len(distribution)
            n_agent = sum(distribution)

            roles = np.zeros((n_goods, 2), dtype=int)
            if economy_model == 'prod: i+1':
                for i in range(n_goods):
                    roles[i] = (i + 1) % n_goods, i

            elif economy_model == 'prod: i-1':
                for i in range(n_goods):
                    roles[i] = (i - 1) % n_goods, i

            else:
                raise Exception(f'Model "{economy_model}" is not defined.')

            idx = 0

            agents = np.zeros(n_agent, dtype=object)
            prod, cons = np.zeros(n_agent, dtype=int), np.zeros(n_agent, dtype=int)

            for agent_type, n in enumerate(distribution):

                i, j = roles[agent_type]

                cognitive_parameters = self.cognitive_parameters \
                    if not heterogeneous else self.cognitive_parameters[idx]

                for ind in range(n):
                    a = eval(self.agent_model)(
                        prod=i, cons=j,
                        cognitive_parameters=cognitive_parameters,
                        n_goods=n_goods,
                        idx=idx
                    )

                    agents[idx], prod[idx], cons[idx] = a, i, j

                    idx += 1

        else:
            assert cons is not None and prod is not None
            n_goods = max(cons) + 1
            n_agent = len(cons)

            agents = np.zeros(n_agent, dtype=object)

            for i in range(n_agent):

                cognitive_parameters = self.cognitive_parameters if not heterogeneous else \
                    self.cognitive_parameters[i]

                agents[i] = eval(self.agent_model)(
                    prod=prod[i], cons=cons[i],
                    cognitive_parameters=cognitive_parameters,
                    n_goods=n_goods,
                    idx=i
                )

        return n_goods, n_agent, agents, prod, cons

    @staticmethod
    def get_markets(n_goods):

        markets = {}
        for i in it.permutations(range(n_goods), r=2):
            markets[i] = []
        return markets

    def run(self):

        for t in range(self.t_max):
            self.time_step(t)

        return {
            'in_hand': self.in_hand,
            'desired': self.desired,
            'prod': self.prod,
            'cons': self.cons,
            'success': self.success
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
            self.in_hand[agent.idx, self.t], \
                self.desired[agent.idx, self.t] = agent_choice

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

            self.success[idx, self.t] = True


def launch(**kwargs):
    e = Economy(**kwargs)
    return e.run()
