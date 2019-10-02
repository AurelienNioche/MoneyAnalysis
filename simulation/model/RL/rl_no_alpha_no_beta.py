from simulation.model.RL.rl_agent import RLAgent


class RLNoAlphaNoBeta(RLAgent):

    bounds = (
        ('gamma', 0.1, 0.15),
    )

    def __init__(self, cognitive_parameters, **kwargs):

        super().__init__(**kwargs)
        self.gamma, = cognitive_parameters

        self.t = 0

    def get_exchanges_and_values(self, in_hand):

        exchanges, values = super().get_exchanges_and_values(in_hand)

        self.t += 1

        return exchanges, values

    def discounting_rule(self, delay):
        return 1/delay

    def learn_from_result(self, in_hand=None, desired=None, success=None):

        if success is None:
            success = int(self.H != self.attempted_exchange[0])
        else:
            self.attempted_exchange = in_hand, desired

        self.acceptance[self.attempted_exchange] = \
            ((self.t-1)/self.t) * self.acceptance[self.attempted_exchange] + \
            (1/self.t) * (success - self.acceptance[self.attempted_exchange])



