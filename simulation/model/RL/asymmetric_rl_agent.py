import numpy as np
import itertools as it
import math

from simulation.model.RL.stupid_agent import StupidAgent
from simulation.model.RL.get_paths import get_paths

from simulation.model.RL.rl_agent import RLAgent


class RLAgentAsymmetric(RLAgent):

    name = "RLAgentAsymmetric"

    def __init__(self, cognitive_parameters, **kwargs):

        super().__init__(metaclass=True, **kwargs)

        self.alpha_plus, self.alpha_minus, _, _ = cognitive_parameters

    def learn_from_result(self, in_hand=None, desired=None, success=None):

        if success is None:
            success = int(self.H != self.attempted_exchange[0])
        else:
            self.attempted_exchange = in_hand, desired

        prediction_error = (success - self.acceptance[self.attempted_exchange])
        self.acceptance[self.attempted_exchange] += \
            self.alpha_minus * (prediction_error < 0) * prediction_error\
            + self.alpha_plus * (prediction_error >= 0) * prediction_error


