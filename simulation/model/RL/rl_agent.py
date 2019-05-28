import numpy as np
import itertools as it
import math

from simulation.model.RL.stupid_agent import StupidAgent
from simulation.model.RL.get_paths import get_paths


class RLAgent(StupidAgent):

    name = "RLAgent"

    def __init__(self, prod, cons, n_goods, cognitive_parameters, idx=None):

        super().__init__(prod=prod, cons=cons, n_goods=n_goods, cognitive_parameters=cognitive_parameters)

        self.alpha, self.beta, self.gamma = cognitive_parameters

        self.acceptance = self.get_acceptance_dic(n_goods)

        self.paths = get_paths(final_node=cons, n_nodes=n_goods)

        self.idx = idx

    @staticmethod
    def get_acceptance_dic(n_goods):

        acceptance = dict()
        for i in it.permutations(range(n_goods), r=2):
            acceptance[i] = 1.

        return acceptance

    def which_exchange_do_you_want_to_try(self):

        exchanges, values = self.get_exchanges_and_values(in_hand=self.H)
        return self.epsilon_rule(values=values, exchanges=exchanges)

    def p_choice(self, in_hand, desired):
        
        exchanges, values = self.get_exchanges_and_values(in_hand=int(in_hand))
        max_idx = np.argmax(values)
        if exchanges[int(max_idx)] == (in_hand, desired):
            p = 1 - self.gamma
        else:
            p = self.gamma / (len(exchanges)-1)

        return p

    def get_exchanges_and_values(self, in_hand):

        exchanges = []
        values = []
        for path in self.paths[in_hand]:

            num = 0
            for exchange in path:

                easiness = self.acceptance[exchange]
                if easiness:

                    num += 1 / easiness

                else:
                    num = 0
                    break

            if num:

                try:
                    value = 1 / math.pow(1 + self.beta, num)
                except OverflowError:
                    value = 0

            else:
                value = 0

            exchanges.append(path[0])
            values.append(value)

        return exchanges, values

    def epsilon_rule(self, values, exchanges):

        max_idx = np.argmax(values)

        if np.random.random() < self.gamma:
            del exchanges[max_idx]
            random_idx = np.random.randint(len(exchanges))
            self.attempted_exchange = exchanges[random_idx]

        else:
            self.attempted_exchange = exchanges[max_idx]

        return self.attempted_exchange

    def consume(self):

        self.learn_from_result()
        super().consume()

    def learn_from_result(self, in_hand=None, desired=None, success=None):

        if success is None:
            success = int(self.H != self.attempted_exchange[0])
        else:
            self.attempted_exchange = in_hand, desired

        self.acceptance[self.attempted_exchange] += \
            self.alpha * (success - self.acceptance[self.attempted_exchange])
