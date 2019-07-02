import os
import numpy as np

import analysis.fit.data
import simulation.run_xp_like
import simulation.run_based_on_fit
import simulation.run
from analysis.metric import metric
from xp import xp
from backup import backup

from game.models import User

DATA_FOLDER = "data"


def reward():
    print('_' * 10)
    print('\n********* Rewards ***********\n')
    users = User.objects.all()
    var = 10 + 0.20 * np.array([u.score for u in users])
    print(f'Reward = {np.mean(var):.2f} (+/- {np.std(var):.2f} STD)')
    print("Computation: 10 euros + 0.20 cents per point")
    print()
    print('_' * 10)


def individual_behavior():

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


def gender(obs_type='ind_0', n_split=3):
    """
    Selection of agents able to proceed to indirect exchanges with good 0
    :param obs_type:
    :param n_split:
    :return:
    """

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
                    data_xp_session=d, i=i, n_split=n_split, slice_idx=-1,
                    obs_type=obs_type)

                data_gender[n_good][categories[int(g)]].append(to_append)

    return data_gender


def age(obs_type='dir', n_split=3):

    data, room_n_good, room_uniform = xp.get_data()

    n_good_cond = np.unique(room_n_good)

    fig_data = {
        n_good: {"age": [], "obs": []} for n_good in n_good_cond
    }

    for d, n_good in zip(data, room_n_good):

        for i, a in enumerate(d.age):

            to_append = metric.get_individual_measure(
                data_xp_session=d, i=i, n_split=n_split, slice_idx=-1,
                obs_type=obs_type)
            fig_data[n_good]['obs'].append(to_append)
            fig_data[n_good]['age'].append(a)

    return fig_data


def parameter_recovery():

    data = {}
    data["HUMAN"], room_n_good, room_uniform = xp.get_data()
    alpha, beta, gamma, mean_p, lls, bic, eco = \
        analysis.fit.data.get(data["HUMAN"], room_n_good, room_uniform)

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


def fit(heterogeneous=True, t_max=None):

    alpha, beta, gamma, mean_p, lls, bic, eco = analysis.fit.data.get()

    data = {}
    data["Human"], room_n_good, room_uniform = xp.get_data()
    data["Simulation"] = simulation.run_based_on_fit.get_data(
        xp_data_list=data["Human"], alpha=alpha, beta=beta, gamma=gamma, eco=eco,
        heterogeneous=heterogeneous, t_max=t_max)

    category = data.keys()
    n_good_cond = np.unique(room_n_good)
    cond_labels = "Non-uniform", "Uniform"

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

                    cond = cond_labels[int(uniform)]
                    fig_data[n_good][cat][agent_type][cond] = \
                        d_formatted[agent_type]

    return fig_data


def sensibility_analysis():

    data_file = os.path.join(DATA_FOLDER, 'sensibility_analysis.p')

    if os.path.exists(data_file):
        data = backup.load(data_file)
        return data

    n_good_cond = 3, 4

    data = {
        g: {} for g in n_good_cond
    }

    for n_good in n_good_cond:

        d = simulation.run.get_data(n_good=n_good)

        alpha = [i[0] for i in d.cognitive_parameters]
        beta = [i[1] for i in d.cognitive_parameters]
        gamma = [i[2] for i in d.cognitive_parameters]

        observation = analysis.metric.metric.get_economy_measure(
            in_hand=d.in_hand, desired=d.desired,
            prod=d.prod, cons=d.cons, m=0)
        data[n_good]['alpha'] = alpha
        data[n_good]['beta'] = beta
        data[n_good]['gamma'] = gamma
        data[n_good]['ind0'] = observation

    backup.save(data, data_file)

    return data
