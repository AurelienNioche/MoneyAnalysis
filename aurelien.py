import os

import numpy as np

import matplotlib.pyplot as plt

import analysis.supplementary
import graph.sim_and_xp
import analysis.stats.stats

from backup import backup

import simulation.run

import analysis.metric.metric

np.seterr(all='raise')
DATA_FOLDER = "data"


def check_effect_of_heterogeneous():

    name_extension = 'FIT_non_heterogeneous'
    fig_data = analysis.supplementary.supplementary_fit(heterogeneous=False)
    graph.sim_and_xp.plot(fig_data, name_extension=name_extension)
    analysis.stats.stats.sim_and_xp(fig_data, name_extension=name_extension)


def check_effect_of_extended_time():

    name_extension = 'FIT_extended'
    fig_data = analysis.supplementary.supplementary_fit(heterogeneous=False, t_max=1000)
    graph.sim_and_xp.plot(fig_data, name_extension=name_extension)
    analysis.stats.stats.sim_and_xp(fig_data, name_extension=name_extension)


def _data_effect_of_unique_parameter():

    data_file = f'{DATA_FOLDER}/sensibility_analysis.p'

    if os.path.exists(data_file):
        data = backup.load(data_file)
        return data

    n_good_cond = 3, 4

    data = {
        g: {} for g in n_good_cond
    }

    for n_good in n_good_cond:

        d = simulation.run.get_data(n_good=n_good)
        # dist = d.distribution

        # n = len(dist)  # Number of economies in this batch

        alpha = [i[0] for i in d.cognitive_parameters]
        beta = [i[1] for i in d.cognitive_parameters]
        gamma = [i[2] for i in d.cognitive_parameters]

        observation = analysis.metric.metric.get_economy_measure(
            in_hand=d.in_hand, desired=d.desired, prod=d.prod, cons=d.cons, m=0)
        data[n_good]['alpha'] = alpha
        data[n_good]['beta'] = beta
        data[n_good]['gamma'] = gamma
        data[n_good]['ind0'] = observation

    backup.save(data, data_file)

    return data


def main():

    data = _data_effect_of_unique_parameter()

    n_good_cond = list(data.keys())
    n_good_cond.sort()

    for n_good in n_good_cond:

        fig, axes = plt.subplots(nrows=3)
        for i, param in enumerate(('alpha', 'beta', 'gamma')):
            print(data[n_good][param])
            print(data[n_good]['ind0'])
            axes[i].scatter(data[n_good][param], data[n_good]['ind0'])
            # axes[i].set_title(param)
            axes[i].set_xlabel(param)
            axes[i].set_ylabel('Freq. ind. ex.')
        plt.savefig(f"fig/sensibility_analysis_{n_good}.pdf")


if __name__ == "__main__":

    main()
