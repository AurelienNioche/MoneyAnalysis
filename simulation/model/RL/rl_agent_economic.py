import numpy as np
import itertools as it
import math

from simulation.model.RL.stupid_agent import StupidAgent
from simulation.model.RL.get_paths import get_paths

from simulation.model.RL.rl_agent import RLAgent


class RLAgentEconomic(RLAgent):

    bounds = \
        ('epsilon', 0.01, 1.00),

    def __init__(self, cognitive_parameters, cons, n_goods, **kwargs):

        super().__init__(metaclass=True, **kwargs)
        self.gamma, = cognitive_parameters

        self.paths = get_paths(final_node=cons, n_nodes=n_goods)

    def get_exchanges_and_values(self, in_hand):

        exchanges = []
        values = []
        for path in self.paths[in_hand]:
            pass

    def learn_from_result(self, in_hand=None, desired=None, success=None):
        pass



