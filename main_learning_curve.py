import fit.data

import numpy as np
import scipy.stats

from xp import xp

from simulation.model.RL.rl_agent import RLAgent

import matplotlib.pyplot as plt
import matplotlib.gridspec as grd

import graph.learning_curves

import os

FIG_FOLDER = "fig"
os.makedirs(FIG_FOLDER, exist_ok=True)


def main(m=0):

    alpha, beta, gamma, mean_p, lls, bic, eco = fit.data.get()

    alpha = np.array(alpha)
    beta = np.array(beta)
    gamma = np.array(gamma)
    eco = np.array(eco)

    data, room_n_good, room_uniform = xp.get_data()

    n_good_cond = np.unique(room_n_good)
    cond_labels = "NON-UNIF", "UNIF"

    fig_data = {n_good: {
        cond: {
        } for cond in cond_labels
    } for n_good in n_good_cond}

    for n_good in n_good_cond:

        for uniform in True, False:

            # Find the good indexes
            cond_n_good = room_n_good == n_good
            cond_uniform = room_uniform == uniform

            xp_cond = cond_n_good * cond_uniform
            assert (np.sum(xp_cond) == 1)
            d_idx = np.where(xp_cond == 1)[0][0]

            xp_data = data[d_idx]

            t_max = xp_data.t_max

            prod = xp_data.prod
            cons = xp_data.cons
            desired = xp_data.desired
            in_hand = xp_data.in_hand
            success = xp_data.success

            n_good = xp_data.n_good
            n_agent = len(xp_data.prod)

            room_alpha = alpha[eco == d_idx]
            room_beta = beta[eco == d_idx]
            room_gamma = gamma[eco == d_idx]

            assert len(room_alpha) == n_agent

            # Potential users of m
            agent_types = tuple(range(2, n_good))  # 2: prod + cons of m

            p_choices_mean = {at: np.zeros(t_max) for at in agent_types}
            p_choices_sem = {at: np.zeros(t_max) for at in agent_types}

            agents = []

            for i in range(n_agent):

                if not cons[i] in agent_types:
                    agents.append(None)
                    continue

                agent = RLAgent(
                    prod=prod[i],
                    cons=cons[i],
                    n_goods=n_good,
                    cognitive_parameters=(room_alpha[i], room_beta[i], room_gamma[i])
                )
                agents.append(agent)

            for t in range(t_max):

                p_choices_t = {at: [] for at in agent_types}

                for i in range(n_agent):

                    if agents[i] is None:
                        continue

                    p = agents[i].p_choice(in_hand=prod[i], desired=m)
                    agents[i].learn_from_result(in_hand=in_hand[i, t], desired=desired[i, t],
                                                success=success[i, t])

                    at = cons[i]
                    p_choices_t[at].append(p)

                for at in agent_types:
                    p_choices_mean[at][t] = np.mean(p_choices_t[at])
                    p_choices_sem[at][t] = np.std(p_choices_t[at])

            for at in agent_types:
                fig_data[n_good][cond_labels[uniform]][at] = \
                    {
                        'mean': p_choices_mean[at],
                        'sem': p_choices_sem[at]
                    }

    for n_good in n_good_cond:

        n_rows = n_good-2

        fig = plt.figure(figsize=(10, 4*n_rows))
        gs = grd.GridSpec(ncols=2, nrows=n_rows)

        for col, cond in enumerate(cond_labels[::-1]):

            agent_types = sorted(fig_data[n_good][cond].keys())

            for row, at in enumerate(agent_types):

                ax = fig.add_subplot(gs[row, col])
                graph.learning_curves.plot(fig_data[n_good][cond][at]['mean'],
                                           fig_data[n_good][cond][at]['sem'],
                                           n_good=n_good, cond=cond, agent_type=at,
                                           ax=ax)

        plt.tight_layout()
        f_name = f"fig/learning_curves_{n_good}.pdf"
        plt.savefig(f_name)
        print(f'{f_name} has been produced')


if __name__ == "__main__":

    main()
