import os
import string

import matplotlib.pyplot as plt
import matplotlib.gridspec as grd

from graph.parameters import FIG_FOLDER, AGENT_LABELLING


def phase_diagram(
        data, labels, n_good,
        ticks_position=(10, 50, 100, 150, 200),
        n_levels=20,
        fontsize=10,
        ax=None,
        n_subplot=None,
        f_name=None,
        ):

    if ax is None:
        fig, ax = plt.subplot(figsize=(8, 8))

    if n_subplot is not None:

        # Add letter
        ax.text(-0.1, 1.1, string.ascii_uppercase[n_subplot],
                transform=ax.transAxes,
                size=20, weight='bold')

    # Ticks
    lab_to_display = ticks_position

    ax.set_xticklabels(lab_to_display)
    ax.set_yticklabels(lab_to_display)

    ticks = [list(labels).index(i) for i in ticks_position]

    ax.set_xticks(ticks)
    ax.set_yticks(ticks)
    ax.tick_params(axis='both', labelsize=fontsize)

    # Axes labels
    x_agent_type = n_good-2
    x_at_label = AGENT_LABELLING[n_good][x_agent_type]\
        .replace('(', '').replace(')', '')\
        .replace(',', '').replace(' ', '')\
        .replace('$', '')

    ax.set_xlabel(f'$x_{{{x_at_label}}}$', fontsize=fontsize*1.5)

    y_agent_type = n_good-1
    y_at_label = AGENT_LABELLING[n_good][y_agent_type]\
        .replace('(', '').replace(')', '')\
        .replace(',', '').replace(' ', '')\
        .replace('$', '')

    ax.set_ylabel(f'$x_{{{y_at_label}}}$', fontsize=fontsize*1.5)

    # Title
    title = f'{n_good} goods'
    ax.set_title(title)

    import numpy as np

    if n_good == 3:
        y_ticks = [0, 0.25, 0.5, 0.75, 1]
    elif n_good == 4:
        y_ticks = [0, 0.33, 0.66, 1]
    else:
        raise NotImplementedError

    x, y = np.meshgrid(range(data.shape[0]), range(data.shape[1]))
    z = data

    c = ax.contourf(x, y, z, n_levels, cmap='viridis')

    from mpl_toolkits.axes_grid1 import make_axes_locatable
    divider = make_axes_locatable(ax)

    cax = divider.append_axes("right", size="5%", pad=0.05)

    plt.colorbar(c, cax=cax, ticks=y_ticks)

    ax.set_aspect(1)

    if f_name is not None:
        plt.tight_layout()

        fig_path = os.path.join(FIG_FOLDER, f_name)
        plt.savefig(fig_path)
        print(f"Figure '{fig_path}' created.\n")


def plot(data, labels, f_name='phase_diagram.pdf'):

    fig = plt.figure(figsize=(14, 8))

    gs = grd.GridSpec(nrows=1, ncols=2)

    for i, n_good in sorted(data.keys()):

        ax = fig.add_subplot(gs[0, i])

        phase_diagram(
            data=data[n_good],
            labels=labels,
            ax=ax,
            n_good=n_good,
            n_subplot=i
        )

    plt.tight_layout()

    fig_path = os.path.join(FIG_FOLDER, f_name)
    plt.savefig(fig_path)
    print(f"Figure '{fig_path}' created.\n")
