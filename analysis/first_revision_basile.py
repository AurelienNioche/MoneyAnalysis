import numpy as np
import scipy.stats

import simulation.run_xp_like
from analysis.metric import metric
from simulation.model.RL.rl_agent import RLAgent
import simulation.run_based_on_fit
import simulation.cross_validation
from xp import xp

import math


def learning_curves_xp(m=0):

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

            n_good = xp_data.n_good

            # Potential users of m
            agent_types = tuple(range(2, n_good))  # 2: prod + cons of m

            p_choices_mean = {at: np.zeros(t_max) for at in agent_types}
            p_choices_sem = {at: np.zeros(t_max) for at in agent_types}

            for at in agent_types:

                agents = np.arange(len(cons))[cons == at]
                n_agent = len(agents)

                ind_matrix = np.zeros((n_agent, t_max))

                for i, agent_idx in enumerate(agents):

                    _, ind_ex, n = metric.exchange(
                        n_good=n_good,
                        prod=prod[agent_idx],
                        cons=cons[agent_idx],
                        desired=desired[agent_idx],
                        in_hand=in_hand[agent_idx]
                    )

                    for t in range(t_max):

                        ind_matrix[i, t] = ind_ex[t, m] / n[t]

                for t in range(t_max):

                    p_choices_mean[at][t] = np.mean(ind_matrix[:, t])
                    p_choices_sem[at][t] = scipy.stats.sem(ind_matrix[:, t])

                fig_data[n_good][cond_labels[uniform]][at] = \
                    {
                        'mean': p_choices_mean[at],
                        'sem': p_choices_sem[at]
                    }

    return fig_data


def learning_curves_sim(alpha=.175, beta=1, gamma=.125, m=0):

    raw_data, room_n_good, room_uniform = xp.get_data()

    data = \
        simulation.run_xp_like.get_data(xp_data=raw_data,
                                        alpha=alpha, beta=beta, gamma=gamma)

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

            n_good = xp_data.n_good

            # Potential users of m
            agent_types = tuple(range(2, n_good))  # 2: prod + cons of m

            p_choices_mean = {at: np.zeros(t_max) for at in agent_types}
            p_choices_sem = {at: np.zeros(t_max) for at in agent_types}

            for at in agent_types:

                agents = np.arange(len(cons))[cons == at]
                n_agent = len(agents)

                ind_matrix = np.zeros((n_agent, t_max))

                for i, agent_idx in enumerate(agents):

                    _, ind_ex, n = metric.exchange(
                        n_good=n_good,
                        prod=prod[agent_idx],
                        cons=cons[agent_idx],
                        desired=desired[agent_idx],
                        in_hand=in_hand[agent_idx]
                    )

                    for t in range(t_max):

                        ind_matrix[i, t] = ind_ex[t, m] / n[t]

                for t in range(t_max):
                    p_choices_mean[at][t] = np.mean(ind_matrix[:, t])
                    p_choices_sem[at][t] = scipy.stats.sem(ind_matrix[:, t])

                fig_data[n_good][cond_labels[uniform]][at] = \
                    {
                        'mean': p_choices_mean[at],
                        'sem': p_choices_sem[at],
                    }

    return fig_data

