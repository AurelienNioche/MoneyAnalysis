from simulation.model.RL.rl_agent import RLAgent


class RLHyperbolicDiscounting(RLAgent):

    def __init__(self, cognitive_parameters, **kwargs):

        super().__init__(cognitive_parameters=cognitive_parameters, **kwargs)

    def discounting_rule(self, delay):

        return self.u / (1 + self.beta*delay)
