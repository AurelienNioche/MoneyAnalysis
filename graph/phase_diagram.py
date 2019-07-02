import matplotlib.pyplot as plt
import matplotlib.gridspec as grd

import os
import string

FIG_FOLDER = "fig"
os.makedirs(FIG_FOLDER, exist_ok=True)


AGENT_LABELLING = {
    3:
        {
            0: '31',
            1: '12',
            2: '23',
        },
    4: {
            0: '41',
            1: '12',
            2: '23',
            3: '34'
        }
    }


def _phase_diagram(
        data, ax, labels, n_good, title=None,
        ticks_position=(10, 50, 100, 150, 200),
        v_max=1.0,
        colorbar=True):

    im = ax.imshow(data, cmap="viridis", origin="lower", vmin=0.0, vmax=v_max)

    lab_to_display = ticks_position

    ax.set_xticklabels(lab_to_display)
    ax.set_yticklabels(lab_to_display)

    ticks = [list(labels).index(i) for i in ticks_position]

    ax.set_xticks(ticks)
    ax.set_yticks(ticks)

    ax.tick_params(labelsize=8)

    agent_type = n_good-2
    at_label = AGENT_LABELLING[n_good][agent_type]

    ax.set_xlabel(f'$x_{{{at_label}}}$')

    if title is not None:
        ax.set_title(title)

    # if letter:
    #     ax.text(
    #         s=letter, x=-0.1, y=-0.2,
    #         horizontalalignment='center',
    #         verticalalignment='center',
    #         transform=ax.transAxes,
    #         fontsize=20)

    agent_type = n_good-1
    at_label = AGENT_LABELLING[n_good][agent_type]
    ax.set_ylabel(f'$x_{{{at_label}}}$')

    title = f'{n_good} goods'
    ax.set_title(title)

    if colorbar:
        from mpl_toolkits.axes_grid1 import make_axes_locatable
        divider = make_axes_locatable(ax)
        cax = divider.append_axes("right", size="5%", pad=0.05)

        plt.colorbar(im, cax=cax)

    ax.set_aspect(1)


def plot(data, labels, f_name, v_max=0.9):

    fig = plt.figure(figsize=(14, 8))

    gs = grd.GridSpec(nrows=1, ncols=2)

    for idx_g, n_good in enumerate((3, 4)):

        ax = fig.add_subplot(gs[0, idx_g])

        _phase_diagram(
            data=data[n_good],
            labels=labels,
            ax=ax,
            n_good=n_good,
            v_max=v_max
        )

        # Add letter
        ax.text(-0.2, 1.2, string.ascii_uppercase[idx_g],
                transform=ax.transAxes,
                size=20, weight='bold')

    plt.tight_layout()

    fig_path = os.path.join(FIG_FOLDER, f_name)
    plt.savefig(fig_path)
    print(f"Figure '{fig_path}' created.\n")
