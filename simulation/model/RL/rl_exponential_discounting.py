from simulation.model.RL.rl_agent import RLAgent

import numpy as np


class RLExponentialDiscounting(RLAgent):

    def __init__(self, cognitive_parameters, **kwargs):

        super().__init__(cognitive_parameters=cognitive_parameters, **kwargs)

    def discounting_rule(self, delay):
        try:
            value = self.u * np.exp(-self.beta*delay)
        except FloatingPointError:
            # print("beta", self.beta, "delay", delay)
            value = 0
        return value
