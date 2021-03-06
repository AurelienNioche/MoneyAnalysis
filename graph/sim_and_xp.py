import os
import string

import matplotlib.pyplot as plt
import matplotlib.gridspec as grd
import numpy as np

from graph.parameters import FIG_FOLDER, AGENT_LABELLING, SUP_FIG_FOLDER


def boxplot(
        results, ax, n_good, colors=None, color=None, tick_labels=None,
        y_label="y_label",
        y_lim=(-0.02, 1.02),
        fontsize=10, aspect=3, title=None,
        n_subplot=None):

    if tick_labels is None:
        tick_labels = results.keys()

    if colors is None:
        if color is None:
            color = 'black'
        colors = [color for _ in range(len(results.keys()))]

    if title:
        ax.set_title(title, fontsize=fontsize)

    if n_subplot is not None:
        # Add letter
        ax.text(-0.2, 1.2, string.ascii_uppercase[n_subplot],
                transform=ax.transAxes,
                size=20, weight='bold')

    n = len(results.keys())

    # For boxplot
    positions = list(range(n))
    values_box_plot = [[] for _ in range(n)]

    # For scatter
    x_scatter = []
    y_scatter = []
    colors_scatter = []

    for i, cond in enumerate(results.keys()):

        for v in results[cond]:

            # For boxplot
            values_box_plot[i].append(v)

            # For scatter
            x_scatter.append(i)
            y_scatter.append(v)
            colors_scatter.append(colors[i])

    # For scatter
    ax.scatter(x_scatter+np.random.random(size=len(x_scatter)) * 0.05 *
               np.random.choice([-1, 1], size=len(x_scatter)),
               y_scatter, c=colors_scatter, s=30, alpha=0.5,
               linewidth=0.0, zorder=1)

    if n_good == 3:
        chance_level = 0.5
        y_ticks = [0, 0.5, 1]
    elif n_good == 4:
        chance_level = 0.33
        y_ticks = [0, 0.33, 0.66, 1]
    else:
        raise NotImplementedError

    # For horizontal line
    ax.axhline(chance_level, linestyle='--', color='0.3', zorder=-10,
               linewidth=0.5)

    ax.set_yticks(y_ticks)
    ax.set_ylim(y_lim)

    # For boxplot
    bp = ax.boxplot(values_box_plot, positions=positions,
                    labels=tick_labels, showfliers=False, zorder=2)

    # Warning: only one box, but several whiskers by plot
    for e in ['boxes', 'caps', 'whiskers', 'medians']:
        for b in bp[e]:
            b.set(color='black')
            # b.set_alpha(1)

    ax.tick_params(axis='both', labelsize=fontsize)
    ax.set_ylabel(y_label, fontsize=fontsize)
    ax.set_aspect(aspect)


def plot(fig_data, name_extension=''):

    post_hoc = 'fit' in name_extension

    n_good_cond = sorted(list(fig_data.keys()))

    category = sorted(fig_data[n_good_cond[0]].keys())
    if not post_hoc:
        # Simulation would on the left column
        category = category[::-1]

    for n_good in n_good_cond:

        n_rows = n_good-2

        fig = plt.figure(figsize=(7, 4*n_rows))
        gs = grd.GridSpec(ncols=len(category), nrows=n_rows)

        n = 0

        for col, cat in enumerate(category):

            agent_type = sorted(fig_data[n_good][cat].keys())
            for row, at in enumerate(agent_type):

                ax = fig.add_subplot(gs[row, col])

                at_label = AGENT_LABELLING[n_good][at]

                results = fig_data[n_good][cat][at]

                if post_hoc and cat == 'Simulation':
                    cat_label = 'Post hoc simulation'
                else:
                    cat_label = cat

                title = f'{cat_label} - Type {at_label}'

                boxplot(results=results, n_good=n_good,
                        ax=ax,
                        title=title,
                        y_label='Freq. ind. ex. with good 1',
                        colors=('C0', 'C1'),
                        n_subplot=n)

                n += 1

        plt.tight_layout()

        f_name = f'xp_{n_good}{name_extension}.pdf'

        if not name_extension:
            f_path = os.path.join(FIG_FOLDER, f_name)
        else:
            f_path = os.path.join(SUP_FIG_FOLDER, f_name)
        plt.savefig(f_path)
        print(f'{f_name} created.')
