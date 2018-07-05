import numpy as np
import itertools as it
import math
from RL.model.stupid_agent import StupidAgent
from RL.model.get_paths import get_paths

np.seterr(all='raise')


class RLAgent(StupidAgent):

    name = "RLAgent"

    def __init__(self, prod, cons, n_goods, cognitive_parameters):

        super().__init__(prod=prod, cons=cons, n_goods=n_goods, cognitive_parameters=cognitive_parameters)

        self.alpha, self.beta, self.gamma = cognitive_parameters

        self.acceptance = self.get_acceptance_dic(n_goods)

        self.paths = get_paths(final_node=cons, n_nodes=n_goods)

    @staticmethod
    def get_acceptance_dic(n_goods):

        acceptance = dict()
        for i in it.permutations(range(n_goods), r=2):
            acceptance[i] = 1.

        return acceptance

    def choose(self, in_hand):
        exchanges, values = self.which_exchange_do_you_want_to_try(in_hand)
        self.epsilon_rule(exchanges=exchanges, values=values)

    def which_exchange_do_you_want_to_try(self, in_hand):

        exchanges = []
        values = []
        for path in self.paths[in_hand]:

            num = 0
            for exchange in path:

                easiness = self.acceptance[exchange]
                if easiness:

                    num += 1/easiness

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

    def learn(self, successful):

        self.acceptance[self.attempted_exchange] += \
            self.alpha * (successful - self.acceptance[self.attempted_exchange])

    def get_exchange_value(self, in_hand, desired):

        return self.acceptance[(in_hand, desired)]
    #
    # def set_attempted_exchange(self, in_hand, desired):
    #
    #     self.attempted_exchange = (in_hand, desired)
