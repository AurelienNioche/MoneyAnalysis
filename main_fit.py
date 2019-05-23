import os
import numpy as np

from simulation.model.RL.rl_agent import RLAgent

from backup import backup, structure

import matplotlib.pyplot as plt

from fit import fit
from xp import xp

from simulation.run import _run

from metric import metric

import graph.sim_and_xp
from stats import stats

SCRIPT_FOLDER = os.path.dirname(os.path.abspath(__file__))
DATA_FOLDER = f'{SCRIPT_FOLDER}/data'

FILE_PATH = f'{DATA_FOLDER}/fit.p'


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


def get_fit():
    xp_data_list, room_n_good, room_uniform = xp.get_data()

    bounds = (
        ('alpha', 0.01, 0.9),  # Learning rate
        ('beta', 0.1, 1.99),  # Decay
        ('gamma', 0.01, 0.99)  # Stochasticity
    )

    alpha, beta, gamma, mean_p, lls, bic, eco = [], [], [], [], [], [], []

    eco_idx = 0

    for d, n_good, uniform in zip(xp_data_list, room_n_good, room_uniform):

        print(n_good, "UNIF:", uniform)
        for i in range(len(d.prod)):
            print("agent", i)

            p_provider = PProvider(xp_data=d, agent_idx=i)

            fitter = fit.Fit()
            best_param, mean_p_, lls_, bic_ = fitter.evaluate(bounds=bounds, p_provider=p_provider)

            alpha.append(best_param['alpha'])
            beta.append(best_param['beta'])
            gamma.append(best_param['gamma'])
            mean_p.append(mean_p_)
            lls.append(lls_)
            bic.append(bic_)
            eco.append(eco_idx)
            print("***")

        eco_idx += 1
        print("___\n")

    return alpha, beta, gamma, mean_p, lls, bic, eco


def simulate_eco(xp_data_list, alpha, beta, gamma, eco):

    alpha = np.array(alpha)
    beta = np.array(beta)
    gamma = np.array(gamma)
    eco = np.array(eco)

    np.random.seed(1234)

    n_rooms = len(xp_data_list)

    # list of DataXpSession
    data = np.zeros(n_rooms, dtype=object)

    for i, xp_d in enumerate(xp_data_list):

        n_good = xp_d.n_good
        t_max = xp_d.t_max

        prod = xp_d.prod
        cons = xp_d.cons

        cognitive_parameters = [(a, b, g) for a, b, g in
                                zip(alpha[eco == i], beta[eco == i], gamma[eco == i])]

        param, bkp = _run({
            'cognitive_parameters': cognitive_parameters,
            'prod': prod,
            'cons': cons,
            't_max': t_max,
            'heterogeneous': True,
            'seed': np.random.randint(2 ** 32 - 1)
        })

        sim_d = structure.DataXPSession(
            in_hand=bkp['in_hand'],
            desired=bkp['desired'],
            prod=bkp['prod'],
            cons=bkp['cons'],
            n_good=n_good,
            t_max=t_max
        )

        data[i] = sim_d

    return data


def plot_hist(alpha, beta, gamma, mean_p, lls, bic, ):

    for v, param_name in zip(
            (alpha, beta, gamma, mean_p, lls, bic, ),
            ("alpha", "beta", "gamma", "mean_p", "lls", "bic", )
    ):

        plt.hist(v)
        plt.title(param_name)
        plt.savefig(f"fig/{param_name}_distribution.pdf")
        plt.close()


def main():

    if not os.path.exists(FILE_PATH):
        alpha, beta, gamma, mean_p, lls, bic, eco = get_fit()
        backup.save(obj=(alpha, beta, gamma, mean_p, lls, bic, eco), file_name=FILE_PATH)

    else:
        alpha, beta, gamma, mean_p, lls, bic, eco = backup.load(file_name=FILE_PATH)

    data = {}
    data["HUMAN"], room_n_good, room_uniform = xp.get_data()
    data["SIM"] = simulate_eco(xp_data_list=data["HUMAN"], alpha=alpha, beta=beta, gamma=gamma, eco=eco)

    category = data.keys()
    n_good_cond = np.unique(room_n_good)
    cond_labels = "NON-UNIF", "UNIF"

    fig_data = {n_good: {
        cat: {

        } for cat in category
    } for n_good in n_good_cond}

    for n_good in room_n_good:

        for uniform in True, False:

            # Find the good indexes
            cond_n_good = room_n_good == n_good
            cond_uniform = room_uniform == uniform

            xp_cond = cond_n_good * cond_uniform
            assert (np.sum(xp_cond) == 1)
            d_idx = np.where(xp_cond == 1)[0][0]

            for cat in category:

                # Get formatted data
                d = data[cat][d_idx]
                d_formatted = metric.dynamic_data(data_xp_session=d)

                for agent_type in sorted(d_formatted.keys()):
                    if agent_type not in fig_data[n_good][cat].keys():
                        fig_data[n_good][cat][agent_type] = {}

                    fig_data[n_good][cat][agent_type][cond_labels[int(uniform)]] = d_formatted[agent_type]

    graph.sim_and_xp.plot(fig_data, name_extension='FIT')
    stats.sim_and_xp(fig_data)


if __name__ == "__main__":

    main()
