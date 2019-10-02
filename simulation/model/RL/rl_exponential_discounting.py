from simulation.model.RL.rl_agent import RLAgent

import numpy as np


class RLExponentialDiscounting(RLAgent):

    def __init__(self, cognitive_parameters, **kwargs):

        super().__init__(cognitive_parameters=cognitive_parameters, **kwargs)

    def discounting_rule(self, delay):

        return self.u * np.exp(-self.beta*delay)
