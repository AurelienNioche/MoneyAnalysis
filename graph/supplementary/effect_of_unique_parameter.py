import numpy as np
import matplotlib.pyplot as plt


def plot(data):

    n_good_cond = list(data.keys())
    n_good_cond.sort()

    for n_good in n_good_cond:

        fig, axes = plt.subplots(nrows=3)

        if n_good == 3:
            chance_level = 0.5
            y_ticks = [0, 0.5, 1]
        elif n_good == 4:
            chance_level = 0.33
            y_ticks = [0, 0.33, 0.66, 1]
        else:
            raise NotImplementedError

        for i, param in enumerate(('alpha', 'beta', 'gamma')):

            # assert not np.sum(np.isnan(data[n_good]['ind0'])), np.isnan(data[n_good]['ind0']).nonzero()

            ax = axes[i]
            ax.scatter(data[n_good][param], data[n_good]['ind0'], alpha=0.01, s=0.5)
            # axes[i].set_title(param)
            ax.set_xlabel(param)
            ax.set_ylabel('Freq. ind. ex.')
            ax.set_ylim(0, 1)
            ax.set_yticks(y_ticks)

            x_ticks = np.unique(data[n_good][param])

            # For horizontal line
            ax.axhline(chance_level, linestyle='--', color='0.3', zorder=-10, linewidth=0.5)

            values_box_plot = [[] for _ in range(len(x_ticks))]
            for idx, x in enumerate(x_ticks):

                not_nan = np.invert(np.isnan(data[n_good]['ind0']))
                relevant = data[n_good][param] == x
                values = data[n_good]['ind0'][relevant * not_nan]
                values_box_plot[idx] += list(values)

            span = x_ticks[-1] - x_ticks[0]

            # For boxplot
            bp = ax.boxplot(values_box_plot, positions=x_ticks, showfliers=False, zorder=-2,
                            widths=[0.10*span for _ in range(len(x_ticks))])

            for e in ['boxes', 'caps', 'whiskers', 'medians']:  # Warning: only one box, but several whiskers by plot
                for b in bp[e]:
                    b.set(color='black')

            ax.set_xticks(x_ticks)
            ax.set_xlim(x_ticks[0]-0.10*span, x_ticks[-1]+0.10*span)

        plt.tight_layout()
        f_name = f"fig/sensibility_analysis_{n_good}.pdf"
        plt.savefig(f_name)
        print(f"Figure {f_name} has been produced.")
