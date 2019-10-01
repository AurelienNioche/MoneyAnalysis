import numpy as np
import itertools as it
import math

from simulation.model.RL.stupid_agent import StupidAgent
from simulation.model.RL.get_paths import get_paths

from simulation.model.RL.rl_agent import RLAgent


class RLAgentAsymmetric(RLAgent):

    name = "RLAgent"

    def __init__(self, cognitive_parameters, **kwargs):

        super().__init__(**kwargs)

