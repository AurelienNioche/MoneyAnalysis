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

        if n_good == 3:
            chance_level = 0.5
            y_ticks = [0, 0.5, 1]
        elif n_good == 4:
            chance_level = 0.33
            y_ticks = [0, 0.33, 0.66, 1]
        else:
            raise NotImplementedError

        for i, param in enumerate(('alpha', 'beta', 'gamma')):

            # assert not np.sum(np.isnan(data[n_good]['ind0'])), np.isnan(data[n_good]['ind0']).nonzero()

            ax = axes[i]
            ax.scatter(data[n_good][param], data[n_good]['ind0'], alpha=0.01, s=0.5)
            # axes[i].set_title(param)
            ax.set_xlabel(param)
            ax.set_ylabel('Freq. ind. ex.')
            ax.set_ylim(0, 1)
            ax.set_yticks(y_ticks)

            x_ticks = np.unique(data[n_good][param])

            # For horizontal line
            ax.axhline(chance_level, linestyle='--', color='0.3', zorder=-10, linewidth=0.5)

            values_box_plot = [[] for _ in range(len(x_ticks))]
            for idx, x in enumerate(x_ticks):

                not_nan = np.invert(np.isnan(data[n_good]['ind0']))
                relevant = data[n_good][param] == x
                values = data[n_good]['ind0'][relevant * not_nan]
                print(len(values))
                values_box_plot[idx] += list(values)

            span = x_ticks[-1] - x_ticks[0]

            # For boxplot
            bp = ax.boxplot(values_box_plot, positions=x_ticks, showfliers=False, zorder=-2,
                            widths=[0.10*span for _ in range(len(x_ticks))])

            for e in ['boxes', 'caps', 'whiskers', 'medians']:  # Warning: only one box, but several whiskers by plot
                for b in bp[e]:
                    b.set(color='black')

            ax.set_xticks(x_ticks)
            ax.set_xlim(x_ticks[0]-0.10*span, x_ticks[-1]+0.10*span)

        plt.tight_layout()
        f_name = f"fig/sensibility_analysis_{n_good}.pdf"
        plt.savefig(f_name)
        print(f"Figure {f_name} has been produced.")


if __name__ == "__main__":

    main()
