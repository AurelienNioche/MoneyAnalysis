import os
import string

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as grd

from graph.parameters import SUP_FIG_FOLDER


def plot(data,
         f_name='sensibility_analysis.pdf',
         parameters=(r'$\alpha$',
                     r'$\beta$',
                     r'$\gamma$',
                     ),
         y_label='Freq. ind. ex. with good 1'):

    fig = plt.figure(figsize=(8, 8))
    gs = grd.GridSpec(nrows=3, ncols=2)

    n_subplot = 0

    n_good_cond = sorted(list(data.keys()))

    for i, n_good in enumerate(n_good_cond):

        if n_good == 3:
            chance_level = 0.5
            y_ticks = [0, 0.5, 1]
        elif n_good == 4:
            chance_level = 0.33
            y_ticks = [0, 0.33, 0.66, 1]
        else:
            raise NotImplementedError

        for j, param in enumerate(parameters):

            # assert not np.sum(np.isnan(data[n_good]['ind0'])),
            # np.isnan(data[n_good]['ind0']).nonzero()

            ax = fig.add_subplot(gs[j, i])

            if j == 0:
                ax.set_title(f'{n_good} goods\n')

            ax.scatter(data[n_good][param],
                       data[n_good]['ind0'],
                       alpha=0.01,
                       s=0.5)

            ax.set_xlabel(param)
            ax.set_ylabel(y_label)
            ax.set_ylim(0, 1)
            ax.set_yticks(y_ticks)

            x_ticks = np.unique(data[n_good][param])

            # For horizontal line
            ax.axhline(chance_level,
                       linestyle='--',
                       color='0.3', zorder=-10,
                       linewidth=0.5)

            values_box_plot = [[] for _ in range(len(x_ticks))]
            for idx, x in enumerate(x_ticks):

                not_nan = np.invert(np.isnan(data[n_good]['ind0']))
                relevant = data[n_good][param] == x
                values = data[n_good]['ind0'][relevant * not_nan]
                values_box_plot[idx] += list(values)

            span = x_ticks[-1] - x_ticks[0]

            # For boxplot
            bp = ax.boxplot(values_box_plot, positions=x_ticks,
                            showfliers=False, zorder=-2,
                            widths=[0.10*span for _ in range(len(x_ticks))])

            # Warning: only one box, but several whiskers by plot
            for e in ['boxes', 'caps', 'whiskers', 'medians']:
                for b in bp[e]:
                    b.set(color='black')

            ax.set_xticks(x_ticks)
            ax.set_xlim(x_ticks[0]-0.10*span, x_ticks[-1]+0.10*span)

            if j == 0:
                # Add letter
                ax.text(-0.3, 1.1, string.ascii_uppercase[n_subplot],
                        transform=ax.transAxes,
                        size=20, weight='bold')

                n_subplot += 1

    plt.tight_layout()

    fig_path = os.path.join(SUP_FIG_FOLDER, f_name)
    plt.savefig(fig_path)

    print(f"Figure '{fig_path}' created.\n")
