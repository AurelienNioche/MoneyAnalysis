import matplotlib.pyplot as plt
import matplotlib.gridspec as grd

import numpy as np
import os


def _phase_diagram(
        data, ax, col, labels, n_good, title=None,
        letter=None, ticks_position=(10, 50, 100, 150, 200), vmax=1):
        # , fig_name=None):

    im = ax.imshow(data, cmap="binary", origin="lower", vmin=0.0, vmax=vmax)  # , vmin=0.5)

    # Create colorbar
    ax.figure.colorbar(im, ax=ax)

    #step = int(len(labels)/n_ticks)
    lab_to_display = ticks_position #labels[::step]

    ax.set_xticklabels(lab_to_display)
    ax.set_yticklabels(lab_to_display)

    # ticks = list(range(len(labels)))[::step]

    ticks = [list(labels).index(i) for i in ticks_position]
    # print(ticks)

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


def plot(data, labels, f_name, max_col=None):

    fig = plt.figure(figsize=(7, 9))

    gs = grd.GridSpec(ncols=max_col if max_col else 4, nrows=2)

    for row, n_good in enumerate((3, 4)):

        for col in range(n_good):

            if max_col and col >= max_col:
                break

            vmax = np.max(data[:][col])

            _phase_diagram(
                data=data[row][col],
                labels=labels,
                ax=fig.add_subplot(gs[row, col]),
                col=col,
                n_good=n_good,
                vmax=vmax,
            )

    plt.tight_layout()

    os.makedirs(os.path.dirname(f_name), exist_ok=True)
    plt.savefig(f_name)
    print(f"Figure '{f_name}' created.\n")


def plot_example():

    labels = np.arange(10, 200, 20)
    n_side = len(labels)

    data = [
        np.random.random(size=(i, n_side, n_side)) for i in (3, 4)
    ]

    plot(data=data, labels=labels, f_name="../../fig/phase_diagram_example.pdf")


if __name__ == "__main__":

    plot_example()
