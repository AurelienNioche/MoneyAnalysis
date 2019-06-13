import numpy as np
import scipy.stats

import analysis.fit.data
import simulation.run_xp_like
from analysis.metric import metric
from simulation.model.RL.rl_agent import RLAgent
import simulation.run_based_on_fit
import simulation.cross_validation
from xp import xp

import math


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


def ind0_freq_over_time(m=0):

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


def cross_validation():
    alpha, beta, gamma, mean_p, lls, bic, eco = analysis.fit.data.get()

    data = {}
    data["HUMAN"], room_n_good, room_uniform = xp.get_data()

    cond_labels = "NON-UNIF", "UNIF"

    fig_data = {cond: None for cond in cond_labels}
    agent_type = 2

    for uniform in True, False:

        # Find the good indexes
        cond_n_good = room_n_good == 3
        cond_uniform = room_uniform == uniform

        xp_cond = cond_n_good * cond_uniform
        assert (np.sum(xp_cond) == 1)
        d_idx = np.where(xp_cond == 1)[0][0]

        d = data['HUMAN'][d_idx]

        n_agent = len(d.cons)
        a = np.ones(n_agent) * np.mean(alpha)
        b = np.ones(n_agent) * np.mean(beta)
        g = np.ones(n_agent) * np.mean(gamma)

        data['SIM'] = simulation.cross_validation.get_data(
            prod=d.prod, cons=d.cons, alpha=a, beta=b, gamma=g, n_good=3, t_max=d.t_max)

        d_formatted = metric.dynamic_data(data_xp_session=data['SIM'])

        fig_data[cond_labels[int(uniform)]] = d_formatted[agent_type]

    return fig_data


def agent_selection():

    """
    Median split
    :return:
    """

    raw_data, room_n_good, room_uniform = xp.get_data()

    alpha, beta, gamma, mean_p, lls, bic, eco = analysis.fit.data.get()

    data = dict()
    data["SIM"] = simulation.run_based_on_fit.get_data(
        xp_data_list=raw_data, alpha=alpha, beta=beta,
        gamma=gamma, eco=eco,
        heterogeneous=True, t_max=None)

    n_good_cond = np.unique(room_n_good)

    alpha = np.asarray(alpha)
    beta = np.asarray(beta)
    gamma = np.asarray(gamma)

    # alpha = np.zeros(room_n_good.shape[0])
    # beta = np.zeros(room_n_good.shape[0])
    # gamma = np.zeros(room_n_good.shape[0])

    for n_good in n_good_cond:

        for uniform in True, False:

            # Find the good indexes
            cond_n_good = room_n_good == n_good
            cond_uniform = room_uniform == uniform

            xp_cond = cond_n_good * cond_uniform
            assert (np.sum(xp_cond) == 1)
            d_idx = np.where(xp_cond == 1)[0][0]

            # Get formatted data
            d = raw_data[d_idx]
            d_formatted = metric.dynamic_data(data_xp_session=d)

            assert type(d.cons) == np.ndarray

            # n = d.cons.shape[0]

            to_select = eco == d_idx

            alpha_eco = alpha[to_select]
            beta_eco = beta[to_select]
            gamma_eco = gamma[to_select]
            #
            # for i, (a, b, g) in enumerate(d.cognitive_parameters):
            #     alpha[i] = a
            #     beta[i] = b
            #     gamma[i] = g

            for agent_type in sorted(d_formatted.keys()):

                at_id = d.cons == agent_type

                at_alpha = alpha_eco[at_id]
                at_beta = beta_eco[at_id]
                at_gamma = gamma_eco[at_id]

                n = len(d_formatted[agent_type])
                half_n = math.ceil(n/2)
                best_id = np.argsort(d_formatted[agent_type])[:half_n]

                best_alpha = at_alpha[best_id]
                best_beta = at_beta[best_id]
                best_gamma = at_gamma[best_id]

                new_alpha_at = np.asarray(list(best_alpha) * 2)[:n]
                new_beta_at = np.asarray(list(best_beta) * 2)[:n]
                new_gamma_at = np.asarray(list(best_gamma) * 2)[:n]

                alpha_eco[at_id] = new_alpha_at
                beta_eco[at_id] = new_beta_at
                gamma_eco[at_id] = new_gamma_at

            alpha[to_select] = alpha_eco
            beta[to_select] = beta_eco
            gamma[to_select] = gamma_eco

    # =================== #

    data["SIM_SELECT"] = simulation.run_based_on_fit.get_data(
        xp_data_list=raw_data, alpha=alpha, beta=beta,
        gamma=gamma, eco=eco,
        heterogeneous=True, t_max=None)

    # =================== #

    category = data.keys()
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

                    fig_data[n_good][cat][agent_type][
                        cond_labels[int(uniform)]] = d_formatted[
                        agent_type]

    return fig_data
