import numpy as np

from simulation.model.RL.rl_agent import RLAgent

from fit import fit
from xp import xp


class PProvider:

    def __init__(self, xp_data, agent_idx):

        self.xp_data = xp_data
        self.agent_idx = agent_idx

    def get_p_choices(self, parameters):

        prod = self.xp_data.prod[self.agent_idx]
        cons = self.xp_data.cons[self.agent_idx]
        n_good = self.xp_data.n_good

        t_max = len(self.xp_data.in_hand[self.agent_idx])

        agent = RLAgent(prod=prod,
                        cons=cons,
                        n_goods=n_good,
                        cognitive_parameters=parameters)

        p_choices = np.zeros(t_max)

        for t in range(t_max):

            in_hand = self.xp_data.in_hand[self.agent_idx, t]
            desired = self.xp_data.desired[self.agent_idx, t]
            successful = self.xp_data.success[self.agent_idx, t]

            p = agent.p_choice(in_hand=in_hand, desired=desired)
            agent.learn_from_result(in_hand=in_hand, desired=desired, successful=successful)

            if p == 0:
                return None
            p_choices[t] = p

        return p_choices

    @staticmethod
    def model_name():
        return "RL"


def main():

    xp_data_list, room_n_good, room_uniform = xp.get_data()

    bounds = (
        ('alpha', 0.1, 0.25),  # Learning rate
        ('beta', 0.8, 1.2),  # Decay
        ('gamma', 0.1, 0.15)  # Stochasticity
    )

    for d, n_good, uniform in zip(xp_data_list, room_n_good, room_uniform):

        print(n_good, "UNIF:", uniform)
        for i in range(len(d.prod)):
            print("agent", i)

            p_provider = PProvider(xp_data=d, agent_idx=i)

            fitter = fit.Fit()
            fitter.evaluate(bounds=bounds, p_provider=p_provider)
            print("***")

        print("___\n")


if __name__ == "__main__":

    main()
