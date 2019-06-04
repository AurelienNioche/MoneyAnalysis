import numpy as np

import analysis.fit.data
import simulation.run_based_on_fit

import simulation.run_xp_like
from analysis.metric import metric
from xp import xp


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


def supplementary_gender(obs_type='dir', n_split=3):

    data, room_n_good, room_uniform = xp.get_data()

    categories = "FEMALE", "MALE"

    n_good_cond = np.unique(room_n_good)

    data_gender = {
        n_good: {
            cat: [] for cat in categories
        } for n_good in n_good_cond
    }

    for d, n_good in zip(data, room_n_good):

        for i, g in enumerate(d.gender):

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


def supplementary_parameter_recovery():

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


def supplementary_fit(heterogeneous=True, t_max=None):

    alpha, beta, gamma, mean_p, lls, bic, eco = analysis.fit.data.get()

    data = {}
    data["HUMAN"], room_n_good, room_uniform = xp.get_data()
    data["SIM"] = simulation.run_based_on_fit.get_data(
        xp_data_list=data["HUMAN"], alpha=alpha, beta=beta, gamma=gamma, eco=eco,
        heterogeneous=heterogeneous, t_max=t_max)

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