import matplotlib.pyplot as plt
import matplotlib.gridspec as grd

import analysis.tools.format
import analysis.compute.monetary_and_medium


def _monetary_behavior_phase_diagram(data, fig, gs, col, row, labels, n_good, title=None,
                                    letter=None, n_ticks=3, fig_name=None):

    ax = fig.add_subplot(gs[row, col])

    im = ax.imshow(data, cmap="binary", origin="lower", vmin=0.0, vmax=1.0)  # , vmin=0.5)

    # Create colorbar
    if col == n_good - 1:

        cbar = ax.figure.colorbar(im, ax=ax)

    step = int(len(labels)/n_ticks)
    lab_to_display = labels[::step]

    ax.set_xticklabels(lab_to_display)
    ax.set_yticklabels(lab_to_display)

    ticks = list(range(len(labels)))[::step]

    ax.set_xticks(ticks)
    ax.set_yticks(ticks)

    ax.tick_params(labelsize=8)

    ax.set_xlabel(f'$x_{n_good-1}$')

    ax.set_aspect(1)

    if title is not None:
        ax.set_title(title)

    if letter:
        ax.text(
            s=letter, x=-0.1, y=-0.2, horizontalalignment='center', verticalalignment='center',
            transform=ax.transAxes,
            fontsize=20)

    if col == 0:

        ax.set_ylabel(f'$x_{n_good}$')

        ax.text(
            s=f'{n_good} goods', x=-0.3, y=0, horizontalalignment='center', verticalalignment='center',
            transform=ax.transAxes,
            fontsize=20
        )

    # if 'fig' in locals():
    #     print('Saving fig.')
    #     noinspection PyUnboundLocalVariable
        # fig.tight_layout()
        #
        # if fig_name is None:
        #     fig_name = f'fig/phase_{n_good}.pdf'
        #
        # os.makedirs(os.path.dirname(fig_name), exist_ok=True)
        # plt.savefig(fig_name)


def plot(three_good, four_good):

    fig = plt.figure(figsize=(15, 10))

    gs = grd.GridSpec(ncols=4, nrows=2)

    for row, n_good in enumerate((3, 4)):

        if n_good == 3:

            monetary_bhv = three_good.monetary_bhv
            repartition = three_good.repartition

        else:
            monetary_bhv = four_good.monetary_bhv
            repartition = four_good.repartition

        formatted_data, labels = analysis.tools.format.for_phase_diagram(
            monetary_bhv,
            repartition,
            n_good
        )

        for col in range(n_good):

            _monetary_behavior_phase_diagram(
                data=formatted_data[col],
                labels=labels,
                gs=gs,
                col=col,
                row=row,
                fig=fig,
                n_good=n_good,
            )

    plt.show()
