import numpy as np


class WSSAgent:

    def __init__(self, n_good, prod, cons):

        self.n_good = n_good
        self.prod = prod
        self.cons = cons

        self.med = [i for i in range(n_good) if i not in (prod, cons)]

        self.possible_strategies = ['direct', ] + [f'indirect_{i}' for i in range(n_good-2)]

        self.current_strategy = None

    def choose(self, in_hand, previous_success):

        if not previous_success:
            possible = [i for i in self.possible_strategies if i != self.current_strategy]
            self.current_strategy = np.random.choice(possible)

        if self.current_strategy == 'direct':

            if in_hand == self.prod:
                desired = self.cons

            else:
                desired = self.prod

        else:

            for i in range(len(self.med)):

                if self.current_strategy == f'indirect_{i}':

                    if in_hand == self.prod:
                        desired = self.med[i]

                    elif in_hand == self.med[i]:
                        desired = self.cons

                    else:
                        desired = self.prod

                    break

        return desired
