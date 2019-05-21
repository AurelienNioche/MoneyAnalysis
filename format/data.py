import os

import numpy as np

import simulation.run_xp_like
import simulation.run
from xp import xp

from metric import metric
from backup import backup


SCRIPT_FOLDER = os.path.dirname(os.path.abspath(__file__))
DATA_FOLDER = f'{SCRIPT_FOLDER}/../data'


def sim_and_xp():
    raw_data = {}

    raw_data['HUMAN'], room_n_good, room_uniform = xp.get_data()

    raw_data['SIM'] = simulation.run_xp_like.get_data(xp_data=raw_data['HUMAN'])

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

    else:

        data = []

        for n_good in 3, 4:
            d = simulation.run.get_data(n_good=n_good)

            formatted_data, labels = metric.phase_diagram(
                in_hand=d.in_hand,
                desired=d.desired,
                prod=d.prod,
                cons=d.cons,
                distribution=d.distribution,
                n_good=len(d.distribution[0])
            )
            data.append(formatted_data)

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


def supplementary_gender(obs_type='dir', n_split=3):

    data, room_n_good, room_uniform = xp.get_data()

    categories = "FEMALE", "MALE"

    data_gender = {
        cat: [] for cat in categories
    }

    for d in data:

        for i, g in enumerate(d.gender):

            to_append = metric.get_individual_measure(
                data_xp_session=d, i=i, n_split=n_split, slice_idx=-1, obs_type=obs_type)

            data_gender[categories[int(g)]].append(to_append)

    return data_gender


def supplementary_age(obs_type='dir', n_split=3):

    data, room_n_good, room_uniform = xp.get_data()

    age = []
    data_age = []

    for d in data:

        for i, a in enumerate(d.age):

            to_append = metric.get_individual_measure(
                data_xp_session=d, i=i, n_split=n_split, slice_idx=-1, obs_type=obs_type)
            data_age.append(to_append)
            age.append(a)

    return age, data_age
