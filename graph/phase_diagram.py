import os
import string

import matplotlib.pyplot as plt
import matplotlib.gridspec as grd
# import matplotlib.colors
# import matplotlib.cm

from graph.labelling import agent_labeling
from graph.utils import save_fig


def phase_diagram(
        data, labels, n_good,
        ticks_position=None,
        ticks_index=None,
        n_levels=20,
        fontsize=10,
        ax=None,
        n_subplot=None,
        x_label=None,
        y_label=None,
        fig_folder=None,
        fig_name=None,
        ):

    if ax is None:
        fig, ax = plt.subplot(figsize=(8, 8))

    if n_subplot is not None:

        # Add letter
        ax.text(-0.1, 1.1, string.ascii_uppercase[n_subplot],
                transform=ax.transAxes,
                size=20, weight='bold')

    # Ticks
    if ticks_position or ticks_index:
        if ticks_position:
            ticks_labels = ticks_position

            ticks = [list(labels).index(i) for i in ticks_position]
        else:
            ticks_labels = [f'{i:.2f}' for i in labels[ticks_index]]
            ticks = ticks_index

        ax.set_xticklabels(ticks_labels)
        ax.set_yticklabels(ticks_labels)

        ax.set_xticks(ticks)
        ax.set_yticks(ticks)
        ax.tick_params(axis='both', labelsize=fontsize)

    # Axes labels

    ax.set_xlabel(x_label, fontsize=fontsize*1.5)
    ax.set_ylabel(y_label, fontsize=fontsize*1.5)

    # Title
    title = f'{n_good} goods'
    ax.set_title(title)

    import numpy as np

    if n_good == 3:
        y_ticks = [0, 0.25, 0.5, 0.75, 1]
        #vmax = 0.66
    elif n_good == 4:
        y_ticks = [0, 0.33, 0.66, 1]
        #vmax = 0.7
    else:
        y_ticks = np.linspace(0, 1, n_good)
        #vmax = 0.75

    x, y = np.meshgrid(range(data.shape[0]), range(data.shape[1]))
    z = data

    print("n good", n_good, "max", np.max(data))

    c = ax.contourf(x, y, z, n_levels, cmap='viridis') #, vmax=vmax)

    from mpl_toolkits.axes_grid1 import make_axes_locatable
    divider = make_axes_locatable(ax)

    cax = divider.append_axes("right", size="5%", pad=0.05)

    # norm = matplotlib.colors.Normalize(vmin=0, vmax=vmax)

    # import matplotlib as mpl

    plt.colorbar(c, cax=cax, ticks=y_ticks)

    ax.set_aspect(1)

    save_fig(fig_folder=fig_folder, fig_name=fig_name)


def plot(data, labels,
         x_label=None,
         y_label=None,
         ticks_position=None,
         ticks_index=None,
         fig_folder=None,
         fig_name='phase_diagram.pdf'):

    fig = plt.figure(figsize=(14, 8))

    gs = grd.GridSpec(nrows=1, ncols=2)

    for i, n_good in enumerate(sorted(data.keys())):

        ax = fig.add_subplot(gs[0, i])

        if not ticks_index and not ticks_position:
            ticks_position = (10, 50, 100, 150, 200)

        if x_label is None or y_label is None:

            al = agent_labeling(n_good)

            x_agent_type = n_good - 2
            x_at_label = al[x_agent_type] \
                .replace('(', '').replace(')', '') \
                .replace(',', '').replace(' ', '') \
                .replace('$', '')

            x_label = f'$x_{{{x_at_label}}}$'

            y_agent_type = n_good - 1
            y_at_label = al[y_agent_type] \
                .replace('(', '').replace(')', '') \
                .replace(',', '').replace(' ', '') \
                .replace('$', '')

            y_label = f'$x_{{{y_at_label}}}$'

        phase_diagram(
            data=data[n_good],
            labels=labels,
            ax=ax,
            n_good=n_good,
            n_subplot=i,
            x_label=x_label,
            y_label=y_label,
            ticks_position=ticks_position,
            ticks_index=ticks_index
        )

    plt.tight_layout()

    save_fig(fig_folder=fig_folder, fig_name=fig_name)
