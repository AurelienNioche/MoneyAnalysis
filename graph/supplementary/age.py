import os
import string

import matplotlib.pyplot as plt
import matplotlib.gridspec as grd


from graph.parameters import SUP_FIG_FOLDER


def plot(data, f_name='age.pdf',
         y_label='Freq. direct ex.'):

    fig = plt.figure(figsize=(7, 4))
    gs = grd.GridSpec(nrows=1, ncols=2)

    for i, n_good in enumerate(sorted(list(data.keys()))):

        ax = fig.add_subplot(gs[0, i])
        ax.set_title(f'{n_good} goods', fontsize=10)

        ax.scatter(
            data[n_good]['age'],
            data[n_good]['obs'],
            s=15, alpha=1,
            facecolor="black", edgecolor='white',
        )

        ax.set_ylabel(y_label)
        ax.set_ylim((-0.01, 1.01))

        if n_good == 3:
            chance_level = 0.5
            y_ticks = (0, 0.5, 1.0)
        elif n_good == 4:
            chance_level = 0.33
            y_ticks = (0, 0.33, 0.66, 1.00)
        else:
            raise NotImplementedError

        ax.set_yticks(y_ticks)
        ax.set_xlabel('Age')

        ratio = 1.0
        xleft, xright = ax.get_xlim()
        ybottom, ytop = ax.get_ylim()
        # the abs method is used to make sure that all numbers are positive
        # because x and y axis of an axes maybe inversed.
        ax.set_aspect(abs((xright - xleft) / (ybottom - ytop)) * ratio)

        # For horizontal line
        ax.axhline(chance_level, linestyle='--', color='0.3', zorder=-10,
                   linewidth=0.5)

        # Add letter
        ax.text(-0.3, 1.1, string.ascii_uppercase[i],
                transform=ax.transAxes,
                size=20, weight='bold')

    plt.tight_layout()

    fig_path = os.path.join(SUP_FIG_FOLDER, f_name)
    plt.savefig(fig_path)
    print(f"Figure '{fig_path}' created.\n")
