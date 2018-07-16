import matplotlib.pyplot as plt
import matplotlib.gridspec as grd

import numpy as np

# import analysis.tools.format
# import analysis.compute.monetary_and_medium


def _monetary_behavior_phase_diagram(
        data, ax, col, labels, n_good, title=None,
        letter=None, n_ticks=3):
        # , fig_name=None):

    im = ax.imshow(data, cmap="binary", origin="lower", vmin=0.0, vmax=1.0)  # , vmin=0.5)

    # Create colorbar
    if col == n_good - 1 and n_good == 4:

        ax.figure.colorbar(im, ax=ax)

    step = int(len(labels)/n_ticks)
    lab_to_display = labels[::step]

    ax.set_xticklabels(lab_to_display)
    ax.set_yticklabels(lab_to_display)

    ticks = list(range(len(labels)))[::step]

    ax.set_xticks(ticks)
    ax.set_yticks(ticks)

    ax.tick_params(labelsize=8)

    ax.set_xlabel(f'$x_{n_good-1}$')

    if title is not None:
        ax.set_title(title)

    ax.set_aspect(1)

    if letter:
        ax.text(
            s=letter, x=-0.1, y=-0.2, horizontalalignment='center', verticalalignment='center',
            transform=ax.transAxes,
            fontsize=20)

    if col == 0:

        ax.set_ylabel(f'$x_{n_good}$')

        ax.text(
            s=f'{n_good} goods', x=-0.2, y=0.5, horizontalalignment='center', verticalalignment='center',
            transform=ax.transAxes,
            fontsize=20,
            rotation='vertical'
        )


    # if 'fig' in locals():
    #     print('Saving fig.')
    #     #noinspection PyUnboundLocalVariable
    #     fig.tight_layout()
    #
    #     if fig_name is None:
    #         fig_name = f'fig/phase_{n_good}.pdf'
    #
    #     os.makedirs(os.path.dirname(fig_name), exist_ok=True)
    #     plt.savefig(fig_name)


# def pre_processing(three_good, four_good):
#
#     formatted_data, labels = analysis.tools.format.for_phase_diagram(
#         monetary_bhv,
#         repartition,
#         n_good
#     )
#
#     return


def plot(data, labels, f_name):

    fig = plt.figure(figsize=(22, 9))

    gs = grd.GridSpec(ncols=4, nrows=2)

    for row, n_good in enumerate((3, 4)):

        for col in range(n_good):

            _monetary_behavior_phase_diagram(
                data=data[row][col],
                labels=labels,
                ax=fig.add_subplot(gs[row, col]),
                col=col,
                n_good=n_good,
            )

    plt.tight_layout()
    plt.savefig(f_name)
    plt.show()


def main():

    labels = np.arange(10, 200, 20)
    n_side = len(labels)

    data = [
        np.random.random(size=(i, n_side, n_side)) for i in (3, 4)
    ]

    plot(data=data, labels=labels, f_name="../../fig/phase_diagram_example.pdf")

    # three_data =
    # plot()


if __name__ == "__main__":

    main()
