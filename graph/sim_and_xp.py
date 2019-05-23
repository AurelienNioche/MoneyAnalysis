import matplotlib.pyplot as plt
import matplotlib.gridspec as grd
import numpy as np

import os


FIG_FOLDER = "fig"
os.makedirs(FIG_FOLDER, exist_ok=True)


def boxplot(
        results, ax, colors=None, tick_labels=None, y_label="y_label", y_lim=None, y_ticks=None,
        fontsize=10, aspect=3):

    if tick_labels is None:
        tick_labels = results.keys()

    if colors is None:
        colors = ['black' for _ in range(len(results.keys()))]

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
    ax.scatter(x_scatter, y_scatter, c=colors_scatter, s=30, alpha=0.5, linewidth=0.0, zorder=1)
    ax.axhline(0.5, linestyle='--', color='0.3', zorder=-10, linewidth=0.5)

    # For boxplot
    bp = ax.boxplot(values_box_plot, positions=positions, labels=tick_labels, showfliers=False, zorder=2)

    for e in ['boxes', 'caps', 'whiskers', 'medians']:  # Warning: only one box, but several whiskers by plot
        for b in bp[e]:
            b.set(color='black')
            # b.set_alpha(1)

    # Aesthetics
    if y_ticks is not None:
        ax.set_yticks(y_ticks)

    if y_lim is not None:
        ax.set_ylim(y_lim)

    ax.tick_params(axis='both', labelsize=fontsize)
    ax.set_ylabel(y_label, fontsize=fontsize)
    ax.set_aspect(aspect)


def plot(fig_data, name_extension=''):

    n_good_cond = fig_data.keys()

    for n_good in n_good_cond:

        category = sorted(fig_data[n_good].keys())

        fig = plt.figure(figsize=(7, 9))
        gs = grd.GridSpec(ncols=len(category), nrows=n_good-2)

        for col, cat in enumerate(category):

            agent_type = sorted(fig_data[n_good][cat].keys())
            for row, at in enumerate(agent_type):
                ax = fig.add_subplot(gs[row, col])
                ax.set_title(f'{cat} - type {at}')

                boxplot(results=fig_data[n_good][cat][at], ax=ax, y_label='Freq. ind. ex. with good 0')

        plt.tight_layout()
        f_name = f'fig/xp_{n_good}_{name_extension}.pdf'
        plt.savefig(f_name)
        print(f'{f_name} has been produced')
