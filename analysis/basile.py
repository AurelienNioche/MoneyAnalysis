import os

import numpy as np
import scipy.stats

import simulation.run_xp_like
import simulation.run
import simulation.run_based_on_fit
import simulation.cross_validation

from xp import xp

import analysis.fit.data

from analysis.metric import metric
from backup import backup

from simulation.model.RL.rl_agent import RLAgent


# SCRIPT_FOLDER = os.path.dirname(os.path.abspath(__file__))
DATA_FOLDER = f'data'


def sim_and_xp(alpha=.175, beta=1, gamma=.125):

    raw_data = {}

    raw_data['HUMAN'], room_n_good, room_uniform = xp.get_data()

    raw_data['SIM'] = simulation.run_xp_like.get_data(xp_data=raw_data['HUMAN'], alpha=alpha, beta=beta, gamma=gamma)

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


def phase_diagram():

    data_file = f'{DATA_FOLDER}/formatted_phase_diagram.p'

    if os.path.exists(data_file):
        data, labels = backup.load(data_file)
        return data, labels

    data = []

    for n_good in 3, 4:

        d = simulation.run.get_data(n_good=n_good)
        dist = d.distribution

        n = len(dist)  # Number of economies in this batch

        observation = metric.get_economy_measure(in_hand=d.in_hand, desired=d.desired, prod=d.prod, cons=d.cons)

        money = np.array([
            [observation[i][good] for good in range(n_good)] for i in range(n)
        ])

        unq_repartition = np.unique(dist, axis=0)
        labels = np.unique([i[-1] for i in unq_repartition])

        n_side = len(labels)

        phases = []

        for good in range(n_good):
            scores = np.array([
                np.mean([money[i][good] for i in range(n) if np.all(dist[i] == r)])
                for r in unq_repartition
            ])

            phases.append(scores.reshape(n_side, n_side).T)

        data.append(phases)

    backup.save((data, labels), data_file)

    return data, labels


def supplementary_sim_and_xp():
    raw_data = {}

    raw_data['HUMAN'], room_n_good, room_uniform = xp.get_data()

    raw_data['SIM'] = simulation.run_xp_like.get_data(xp_data=raw_data['HUMAN'])

    category = raw_data.keys()
    n_good_cond = np.unique(room_n_good)
    cond_labels = "NON-UNIF", "UNIF"

    obs_type = 'ind_0', 'dir'

    fig_data = {
        ot: {
            n_good: {
                cat: {

                } for cat in category
            } for n_good in n_good_cond
        } for ot in obs_type
    }

    for ot in obs_type:
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
                    d_formatted = metric.dynamic_data(data_xp_session=d,
                                                      obs_type=ot,
                                                      slice_idx='all')

                    for agent_type in sorted(d_formatted.keys()):
                        if agent_type not in fig_data[ot][n_good][cat].keys():
                            fig_data[ot][n_good][cat][agent_type] = {}

                        fig_data[ot][n_good][cat][agent_type][cond_labels[int(uniform)]] = d_formatted[agent_type]

    return fig_data


def supplementary_gender(obs_type='ind_0', n_split=3):

    data, room_n_good, room_uniform = xp.get_data()

    categories = "FEMALE", "MALE"

    n_good_cond = np.unique(room_n_good)

    data_gender = {
        n_good: {
            cat: [] for cat in categories
        } for n_good in n_good_cond
    }

    for d, n_good in zip(data, room_n_good):

        # get agent types depending on the number of good
        agent_types = tuple(range(2, n_good))

        # get agents of this type
        agent_of_interest = []
        for at in agent_types:
            agent_of_interest += np.arange(len(d.cons))[d.cons == at].tolist()

        for i, g in enumerate(d.gender):

            # only compute and append for this agent type
            if i in agent_of_interest:
                to_append = metric.get_individual_measure(
                    data_xp_session=d, i=i, n_split=n_split, slice_idx=-1, obs_type=obs_type)

                data_gender[n_good][categories[int(g)]].append(to_append)

    return data_gender


def supplementary_age(obs_type='dir', n_split=3):

    data, room_n_good, room_uniform = xp.get_data()

    n_good_cond = np.unique(room_n_good)

    fig_data = {
        n_good: {"age": [], "obs": []} for n_good in n_good_cond
    }

    for d, n_good in zip(data, room_n_good):

        for i, a in enumerate(d.age):

            to_append = metric.get_individual_measure(
                data_xp_session=d, i=i, n_split=n_split, slice_idx=-1, obs_type=obs_type)
            fig_data[n_good]['obs'].append(to_append)
            fig_data[n_good]['age'].append(a)

    return fig_data


def parameter_recovery():

    data = {}
    data["HUMAN"], room_n_good, room_uniform = xp.get_data()
    alpha, beta, gamma, mean_p, lls, bic, eco = analysis.fit.data.get(data["HUMAN"], room_n_good, room_uniform)

    data["SIM"] = simulation.run_based_on_fit.get_data(
        xp_data_list=data["HUMAN"], alpha=alpha, beta=beta, gamma=gamma, eco=eco)

    r_alpha, r_beta, r_gamma, r_mean_p, r_lls, r_bic, r_eco = analysis.fit.data.get(
        data["SIM"], room_n_good, room_uniform, extension="sim")

    fig_data = {
        "alpha": (alpha, r_alpha),
        "beta": (beta, r_beta),
        "gamma": (gamma, r_gamma)
    }

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


def fit():

    alpha, beta, gamma, mean_p, lls, bic, eco = analysis.fit.data.get()

    data = {}
    data["HUMAN"], room_n_good, room_uniform = xp.get_data()

    data["SIM"] = simulation.run_based_on_fit.get_data(
        xp_data_list=data["HUMAN"], alpha=alpha, beta=beta, gamma=gamma, eco=eco)

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
