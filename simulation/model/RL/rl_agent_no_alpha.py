from simulation.model.RL.rl_agent import RLAgent


class RLAgentNoAlpha(RLAgent):

    bounds = (
        ('gamma', 0.1, 0.15),
    )

    def __init__(self, cognitive_parameters, **kwargs):

        super().__init__(metaclass=True, **kwargs)
        self.gamma, = cognitive_parameters

        self.t = 0

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
                    value = 1 / num
                except OverflowError:
                    value = 0

            else:
                value = 0

            exchanges.append(path[0])
            values.append(value)

        self.t += 1

        return exchanges, values

    def learn_from_result(self, in_hand=None, desired=None, success=None):

        if success is None:
            success = int(self.H != self.attempted_exchange[0])
        else:
            self.attempted_exchange = in_hand, desired

        self.acceptance[self.attempted_exchange] = \
            ((self.t-1)/self.t) * self.acceptance[self.attempted_exchange] + \
            (1/self.t) * (success - self.acceptance[self.attempted_exchange])



