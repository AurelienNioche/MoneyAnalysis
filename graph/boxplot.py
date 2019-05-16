import matplotlib.pyplot as plt
import matplotlib.gridspec as grd

import os


FIG_FOLDER = "fig"
os.makedirs(FIG_FOLDER, exist_ok=True)


def _boxplot(
        results, ax, colors=None, tick_labels=None, y_label="y_label", y_lim=None, y_ticks=None,
        fontsize=10, aspect=3):

    if tick_labels is None:
        tick_labels = results.keys()

    if colors is None:
        colors = ["black" for _ in range(len(results.keys()))]

    n = len(results.keys())
    positions = list(range(n))

    x_scatter = []
    y_scatter = []
    colors_scatter = []

    values_box_plot = []

    for i, cond in enumerate(results.keys()):

        values_box_plot.append([])

        for v in results[cond].values():
            # For box plot
            values_box_plot[-1].append(v)

            # For scatter
            y_scatter.append(v)
            x_scatter.append(i)
            colors_scatter.append(colors[i])

    ax.scatter(x_scatter, y_scatter, c=colors_scatter, s=30, alpha=0.5, linewidth=0.0, zorder=1)

    ax.axhline(0.5, linestyle='--', color='0.3', zorder=-10, linewidth=0.5)

    if y_ticks is not None:
        ax.set_yticks(y_ticks)

    ax.tick_params(axis='both', labelsize=fontsize)

    # ax.set_xlabel("Type of control\nMonkey {}.".format(monkey), fontsize=fontsize)
    # ax.set_xlabel("Control type", fontsize=fontsize)
    ax.set_ylabel(y_label, fontsize=fontsize)

    if y_lim is not None:
        ax.set_ylim(y_lim)

    # Boxplot
    bp = ax.boxplot(values_box_plot, positions=positions, labels=tick_labels, showfliers=False, zorder=2)

    for e in ['boxes', 'caps', 'whiskers', 'medians']:  # Warning: only one box, but several whiskers by plot
        for b in bp[e]:
            b.set(color='black')
            # b.set_alpha(1)

    ax.set_aspect(aspect)


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
