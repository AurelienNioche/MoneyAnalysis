import numpy as np

import analysis.fit.data
import simulation.run_xp_like
from analysis.metric import metric
from simulation.model.RL.rl_agent import RLAgent
import simulation.run_based_on_fit
from xp import xp


def sim_and_xp_exploration(alpha=.175, beta=1, gamma=.125, random_cognitive_param=False):

    raw_data = {}

    raw_data['HUMAN'], room_n_good, room_uniform = xp.get_data()

    raw_data['SIM'] = simulation.run_xp_like.get_data(xp_data=raw_data['HUMAN'],
                                                      gamma=gamma, beta=beta, alpha=alpha,
                                                      random_cognitive_param=random_cognitive_param)

    category = raw_data.keys()
    n_good_cond = np.unique(room_n_good)
    cond_labels = "NON-UNIF", "UNIF"

    fig_data = {n_good: {
        cat: {

        } for cat in category
    } for n_good in n_good_cond}

    for n_good in n_good_cond:

        for uniform in True, False:

            # Find the good indexes
            cond_n_good = room_n_good == n_good
            cond_uniform = room_uniform == uniform

            xp_cond = cond_n_good * cond_uniform
            assert (np.sum(xp_cond) == 1)
            d_idx = np.where(xp_cond == 1)[0][0]

            for cat in category:

                # Get formatted data
                d = raw_data[cat][d_idx]
                d_formatted = metric.dynamic_data(data_xp_session=d)

                for agent_type in sorted(d_formatted.keys()):
                    if agent_type not in fig_data[n_good][cat].keys():
                        fig_data[n_good][cat][agent_type] = {}

                    fig_data[n_good][cat][agent_type][cond_labels[int(uniform)]] = d_formatted[agent_type]

    return fig_data


def learning_curves(m=0):

    alpha, beta, gamma, mean_p, lls, bic, eco = analysis.fit.data.get()

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

    return fig_data
