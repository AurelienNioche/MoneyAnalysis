import numpy as np

from simulation.model.RL.rl_agent import RLAgent


class RLSoftmax(RLAgent):

    bounds = (
        ('alpha', 0.1, 0.25),
        ('gamma', 0.01, 0.15)
    )

    def __init__(self, cognitive_parameters, **kwargs):

        super().__init__(**kwargs)

        self.alpha, self.gamma, = cognitive_parameters

    def discounting_rule(self, delay):
        return 1/delay

    def decision_rule(self, values, exchanges):

        """
        Softmax
        :param values:
        :param exchanges:
        :return:
        """

        try:
            p = np.exp(values / self.gamma) / \
                   np.sum(np.exp(values / self.gamma))
        except (Warning, FloatingPointError) as w:
            raise Exception(f'{w} [x={values}, temp={self.gamma}]')

        self.attempted_exchange = \
            exchanges[np.random.choice(range(len(exchanges)), p=p)]
        return self.attempted_exchange
