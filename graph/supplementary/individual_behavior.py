import os
import string

import matplotlib.pyplot as plt
import matplotlib.gridspec as grd


from graph.parameters import SUP_FIG_FOLDER, AGENT_LABELLING


def _plot(
        results, ax,
        x_label='x_label',
        y_label='y_label',
        y_lim=(-0.01, 1.01),
        y_ticks=None,
        fontsize=10,
        tick_labels=None,
        title=None,
        color='black'
    ):

    n_split = len(results[0])

    if tick_labels is None:
        tick_labels = range(n_split)

    for data_ind in results:
        ax.plot(data_ind, color=color, alpha=0.5, linewidth=0.5)

    if title is not None:
        ax.set_title(title, fontsize=fontsize)

    x_scatter = []
    y_scatter = []

    for data_ind in results:
        for idx_split, split_value in enumerate(data_ind):

            x_scatter.append(idx_split)
            y_scatter.append(split_value)

    ax.scatter(x_scatter, y_scatter, c=color, s=30, alpha=0.5, linewidth=0.0,
               zorder=1)
    ax.axhline(0.5, linestyle='--', color='0.3', zorder=-10, linewidth=0.5)

    if y_ticks is not None:
        ax.set_yticks(y_ticks)

    ax.tick_params(axis='both', labelsize=fontsize)

    ax.set_xlabel(x_label, fontsize=fontsize)
    ax.set_ylabel(y_label, fontsize=fontsize)

    ax.set_xticks(range(len(tick_labels)))
    ax.set_xticklabels(tick_labels)

    if y_lim is not None:
        ax.set_ylim(y_lim)

    ratio = 1.0
    xleft, xright = ax.get_xlim()
    ybottom, ytop = ax.get_ylim()
    # the abs method is used to make sure that all numbers are positive
    # because x and y axis of an axes maybe inversed.
    ax.set_aspect(abs((xright - xleft) / (ybottom - ytop)) * ratio)


def plot(fig_data, y_labels=None, colors=None,
         x_label='Time chunk', tick_labels=('1/3', '2/3', '3/3')):

    if y_labels is None:
        y_labels = {
            'ind_0': 'Freq. ind. ex. with good 1',
            'dir': 'Freq. direct ex.'
        }

    if colors is None:
        colors = {
            'Uniform': 'C0',
            'Non-uniform': 'C1'
        }

    # Type of measure ('dir', 'ind_0', ...)
    obs_type = fig_data.keys()

    for ot in obs_type:

        n_good_cond = fig_data[ot].keys()

        for n_good in n_good_cond:

            # Human or artificial
            category = sorted(list(fig_data[ot][n_good].keys()))[::-1]

            n_cols = 2*len(category)  # '2' because 2 conditions
            n_rows = n_good - 2 if 'ind' in ot else n_good

            y_label = y_labels[ot]

            fig = plt.figure(figsize=(3*n_cols, 3*n_rows))
            gs = grd.GridSpec(ncols=n_cols, nrows=n_rows)

            agent_type = sorted(fig_data[ot][n_good][list(category)[0]].keys())

            idx_fig = 0

            for row, at in enumerate(agent_type):

                col = 0

                for cat in category:

                    conditions = fig_data[ot][n_good][cat][at].keys()
                    assert len(conditions) == 2

                    for cond in conditions:

                        ax = fig.add_subplot(gs[row, col])

                        at_label = AGENT_LABELLING[n_good][at]

                        title = f'{cat} - {cond} - Type {at_label}'

                        color = colors[cond]

                        _plot(results=fig_data[ot][n_good][cat][at][cond],
                              ax=ax,
                              x_label=x_label,
                              y_label=y_label,
                              tick_labels=tick_labels,
                              title=title,
                              color=color)

                        if col % 2 == 0 and row == 0:
                            # Add letter
                            ax.text(-0.2, 1.1,
                                    string.ascii_uppercase[idx_fig],
                                    transform=ax.transAxes,
                                    size=20, weight='bold')
                            idx_fig += 1

                        col += 1

            plt.tight_layout()

            f_name = f'individual_behavior_{n_good}_{ot}.pdf'

            plt.tight_layout()

            fig_path = os.path.join(SUP_FIG_FOLDER, f_name)
            plt.savefig(fig_path)
            print(f"Figure '{fig_path}' created.\n")
