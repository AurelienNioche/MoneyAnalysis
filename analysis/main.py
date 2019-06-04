import os

import numpy as np

import simulation.run
import simulation.run_xp_like
from analysis.data import DATA_FOLDER
from analysis.metric import metric
from backup import backup
from xp import xp


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
