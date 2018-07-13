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

    # def choose(self, in_hand):
    #     exchanges, values = self.which_exchange_do_you_want_to_try(in_hand)
    #     self.epsilon_rule(exchanges=exchanges, values=values)

    def which_exchange_do_you_want_to_try(self):

        exchanges, values = self.get_exchanges_and_values(in_hand=self.H)

        #p = self.softmax(np.asarray(values), temp=self.gamma)
        #{idx_ex = np.random.choice(np.arange(len(exchanges)), p=p)

        return self.epsilon_rule(values, exchanges)

        # self.attempted_exchange = exchanges[idx_ex]

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

    def learn_from_human_choice(self, in_hand, desired, successful):

        self.attempted_exchange = (in_hand, desired)

        diff = self.alpha * (successful - self.acceptance[self.attempted_exchange])

        if diff >= 0:
            self.acceptance[self.attempted_exchange] += diff

    def get_p_choose(self, in_hand, desired):

        exchanges, values = self.get_exchanges_and_values(in_hand)

        self.softmax(np.asarray(values), temp=self.gamma)

        # max_value = np.max(values)

        # idx_max_values = [i for i in range(len(values)) if values[i] == max_value]

        idx_ex = -1
        for i, ex in enumerate(exchanges):
            if ex == (in_hand, desired):
                idx_ex = i
                break

        assert idx_ex != -1

        soft = self.softmax(np.asarray(values), temp=self.gamma)
        return soft[idx_ex]

        # max_value = np.max(values)
        #
        # idx_max_values = [i for i in range(len(values)) if values[i] == max_value]
        #
        # idx_ex = -1
        # for i, ex in enumerate(exchanges):
        #     if ex == (in_hand, desired):
        #         idx_ex = i
        #         break
        #
        # assert idx_ex != -1
        #
        # if idx_ex in idx_max_values:
        #     return 1 - self.gamma
        #
        # else:
        #     return self.gamma / (len(exchanges) - len(idx_max_values))

    def consume(self):

        self.learn_from_result()
        super().consume()

    def learn_from_result(self):

        successful = int(self.H != self.attempted_exchange[0])

        self.acceptance[self.attempted_exchange] += \
            self.alpha * (successful - self.acceptance[self.attempted_exchange])

    @staticmethod
    def softmax(x, temp):

        try:
            return np.exp(x / temp) / np.sum(np.exp(x / temp))
        except (Warning, FloatingPointError) as w:
            print(x, temp)
            raise Exception(f'{w} [x={x}, temp={temp}]')
