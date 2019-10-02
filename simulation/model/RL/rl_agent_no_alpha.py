import numpy as np
import itertools as it
import math

from simulation.model.RL.stupid_agent import StupidAgent
from simulation.model.RL.get_paths import get_paths

from simulation.model.RL.rl_agent import RLAgent


class RLAgentEconomic(RLAgent):

    bounds = \
        ('gamma', 0.01, 1.00),

    def __init__(self, cognitive_parameters, **kwargs):

        super().__init__(metaclass=True, **kwargs)
        self.gamma, = cognitive_parameters

        self.t = 0

    def get_exchanges_and_values(self, in_hand):

        self.t += 1

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

    def learn_from_result(self, in_hand=None, desired=None, success=None):

        if success is None:
            success = int(self.H != self.attempted_exchange[0])
        else:
            self.attempted_exchange = in_hand, desired

        self.acceptance[self.attempted_exchange] += \
            self.alpha * (success - self.acceptance[self.attempted_exchange])



