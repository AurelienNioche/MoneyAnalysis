import matplotlib.pyplot as plt
import matplotlib.gridspec as grd
import numpy as np

import os


FIG_FOLDER = "fig"
os.makedirs(FIG_FOLDER, exist_ok=True)


def _plot(
        results, ax, color='black', y_label="y_label", y_lim=(-0.01, 1.01), y_ticks=None,
        fontsize=10,
        aspect=3,
        tick_labels=None,
):

    n_split = len(results[0])

    if tick_labels is None:
        tick_labels = range(n_split)

    for data_ind in results:
        ax.plot(data_ind, color='black', alpha=0.5)

    x_scatter = []
    y_scatter = []

    for data_ind in results:
        for idx_split, split_value in enumerate(data_ind):

            # For scatter
            x_scatter.append(idx_split)
            y_scatter.append(split_value)

    ax.scatter(x_scatter, y_scatter, c=color, s=30, alpha=0.5, linewidth=0.0, zorder=1)
    ax.axhline(0.5, linestyle='--', color='0.3', zorder=-10, linewidth=0.5)

    if y_ticks is not None:
        ax.set_yticks(y_ticks)

    ax.tick_params(axis='both', labelsize=fontsize)

    ax.set_ylabel(y_label, fontsize=fontsize)

    ax.set_xticks(range(len(tick_labels)))
    ax.set_xticklabels(tick_labels)

    if y_lim is not None:
        ax.set_ylim(y_lim)

    ax.set_aspect(aspect)


def plot(fig_data):

    n_good_cond = fig_data.keys()

    for n_good in n_good_cond:

        category = fig_data[n_good].keys()

        n_cols = 2*len(category)  # '2' because 2 conditions
        n_rows = n_good-2

        print(n_good, "col, row", n_cols, n_rows)

        fig = plt.figure(figsize=(15, 15), dpi=200)
        gs = grd.GridSpec(ncols=n_cols, nrows=n_rows)

        agent_type = fig_data[n_good][list(category)[0]].keys()

        for row, at in enumerate(agent_type):

            col = 0

            for cat in category:

                conditions = fig_data[n_good][cat][at].keys()
                assert len(conditions) == 2

                for cond in conditions:

                    # print('row, col', row, col+col)
                    # print(n_good, cat, at, cond)

                    ax = fig.add_subplot(gs[row, col])
                    ax.set_title(f'{cat} - {cond} - type {at}')

                    _plot(results=fig_data[n_good][cat][at][cond], ax=ax, y_label='Freq. ind. ex. with good 0',
                          tick_labels=('1/3', '2/3', '3/3'))

                    col += 1

                # ax = fig.add_subplot(gs[row, col])
                # ax.set_title(f'{cat} - type {at}')

                # _plot(results=fig_data[n_good][cat][at], ax=ax, y_label='Freq. ind. ex. with good 0')

        plt.tight_layout()
        plt.savefig(f'fig/supplementary_indirect_{n_good}.pdf')