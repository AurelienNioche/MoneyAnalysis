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
        data, ax, labels, n_good,
        ticks_position=(10, 50, 100, 150, 200),
        v_max=1.0,
        colorbar=True,
        fontsize=10):

    im = ax.imshow(data, cmap="viridis", origin="lower", vmin=0.0, vmax=v_max)

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
    x_at_label = AGENT_LABELLING[n_good][x_agent_type]

    ax.set_xlabel(f'$x_{{{x_at_label}}}$', fontsize=fontsize*1.5)

    y_agent_type = n_good-1
    y_at_label = AGENT_LABELLING[n_good][y_agent_type]
    ax.set_ylabel(f'$x_{{{y_at_label}}}$', fontsize=fontsize*1.5)

    # Title
    title = f'{n_good} goods'
    ax.set_title(title)

    if colorbar:
        from mpl_toolkits.axes_grid1 import make_axes_locatable
        divider = make_axes_locatable(ax)

        if n_good == 3:
            ticks_position = 0.5
        cax = divider.append_axes("right", size="5%", pad=0.05,
                                  ticks_position=ticks_position)

        plt.colorbar(im, cax=cax)

    ax.set_aspect(1)


def plot(data, labels, f_name):

    fig = plt.figure(figsize=(14, 8))

    gs = grd.GridSpec(nrows=1, ncols=2)

    for idx_g, n_good in enumerate((3, 4)):

        ax = fig.add_subplot(gs[0, idx_g])

        _phase_diagram(
            data=data[n_good],
            labels=labels,
            ax=ax,
            n_good=n_good)

        # Add letter
        ax.text(-0.1, 1.1, string.ascii_uppercase[idx_g],
                transform=ax.transAxes,
                size=20, weight='bold')

    plt.tight_layout()

    fig_path = os.path.join(FIG_FOLDER, f_name)
    plt.savefig(fig_path)
    print(f"Figure '{fig_path}' created.\n")
