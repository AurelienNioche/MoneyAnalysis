import numpy as np
import itertools as it

from simulation.model.RL.rl_agent import RLAgent


class Economy(object):

    def __init__(self, repartition, t_max, agent_model, economy_model, cognitive_parameters=None, seed=None,
                 **kwargs):  # Args for analysis

        np.random.seed(seed)
        self.t_max = t_max
        self.cognitive_parameters = cognitive_parameters
        self.agent_model = agent_model
        self.repartition = np.asarray(repartition)

        self.n_goods = len(self.repartition)
        self.roles = self.get_roles(self.n_goods, economy_model)

        self.n_agent = sum(self.repartition)

        self.agents = self.create_agents()

        self.t = 0

        self.markets = self.get_markets(self.n_goods)
        self.exchange_types = list(it.combinations(range(self.n_goods), r=2))

        # ---- For backup ----- #
        self.bkp_medium_over_agents = np.zeros((self.n_goods, self.n_agent, self.t_max))
        self.bkp_medium_over_time = np.zeros((self.n_goods, self.t_max))
        self.bkp_monetary_bhv = \
            np.ones((self.n_goods, self.n_agent, self.t_max)) * -1

    @staticmethod
    def get_markets(n_goods):

        markets = {}
        for i in it.permutations(range(n_goods), r=2):
            markets[i] = []
        return markets

    @staticmethod
    def get_roles(n_goods, model):

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

    def create_agents(self):

        agents = np.zeros(self.n_agent, dtype=object)

        idx = 0

        for agent_type, n in enumerate(self.repartition):

            i, j = self.roles[agent_type]

            for ind in range(n):
                a = eval(self.agent_model)(
                    prod=i, cons=j,
                    cognitive_parameters=self.cognitive_parameters,
                    n_goods=self.n_goods,
                    idx=idx
                )

                agents[idx] = a
                idx += 1

        return agents

    def run(self):

        for t in range(self.t_max):
            self.time_step(t)

        return {
            'medium_over_agents': self.bkp_medium_over_agents,
            'medium_over_time': self.bkp_medium_over_time,
            'monetary_bhv': self.bkp_monetary_bhv
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

            # ---- For backup ----- #

            for m in range(self.n_goods):

                if m in (agent.P, agent.C):
                    monetary_conform = agent_choice == (agent.P, agent.C)

                else:
                    monetary_conform = agent_choice in [(agent.P, m), (m, agent.C)]

                    if monetary_conform:

                        self.bkp_medium_over_time[m, self.t] += 1

                self.bkp_monetary_bhv[m, agent.idx, self.t] = monetary_conform

            # ---- For backup ----- #

            ind_first_part = \
                agent_choice[0] == agent.P and agent_choice[1] != agent.C
            ind_second_part = \
                agent_choice[0] != agent.P and agent_choice[1] == agent.C

            if ind_first_part:
                self.bkp_medium_over_agents[agent_choice[1], agent.idx, self.t] = ind_first_part
            if ind_second_part:
                self.bkp_medium_over_agents[agent_choice[0], agent.idx, self.t] = ind_second_part

            # ----------- #

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
