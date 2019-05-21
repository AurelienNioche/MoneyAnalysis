import matplotlib.pyplot as plt
import matplotlib.gridspec as grd

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


def plot(fig_data, obs_type):

    n_good_cond = fig_data.keys()

    for n_good in n_good_cond:

        category = fig_data[n_good].keys()

        n_cols = 2*len(category)  # '2' because 2 conditions
        n_rows = n_good - 2 if 'ind' in obs_type else n_good

        y_label = 'Freq. ind. ex. with good 0' if 'ind' in obs_type else "Freq. dir. ex."

        fig = plt.figure(figsize=(15, 15), dpi=200)
        gs = grd.GridSpec(ncols=n_cols, nrows=n_rows)

        agent_type = sorted(fig_data[n_good][list(category)[0]].keys())

        for row, at in enumerate(agent_type):

            col = 0

            for cat in category:

                conditions = fig_data[n_good][cat][at].keys()
                assert len(conditions) == 2

                for cond in conditions:

                    ax = fig.add_subplot(gs[row, col])
                    ax.set_title(f'{cat} - {cond} - type {at}')

                    _plot(results=fig_data[n_good][cat][at][cond], ax=ax, y_label='Freq. ind. ex. with good 0',
                          tick_labels=('1/3', '2/3', '3/3'))

                    col += 1

        plt.tight_layout()

        f_name = f'fig/supplementary_indirect_{n_good}_{obs_type}.pdf'
        plt.savefig(f_name)
        print(f'{f_name} has been produced')
