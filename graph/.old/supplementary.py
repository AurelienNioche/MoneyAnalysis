import matplotlib.pyplot as plt
import numpy as np


def box_plot(data, xlabel=None, ylabel=None, f_name=None):

    fig = plt.figure()
    ax = fig.add_subplot(111)

    n = len(data[:, 0])
    colors = ['C0' for _ in range(n - 1)] + ['C1']
    fontsize = 10

    y_scatter = data.flatten()
    x_scatter = np.repeat(np.arange(n) + 1, len(data[0, :]))

    colors_scatter = np.array([colors[i-1] for i in x_scatter])

    # box plot reads by columns
    box_plot_data = data.transpose()

    ax.scatter(x_scatter, y_scatter, c=colors_scatter, s=30, alpha=0.5, linewidth=0.0, zorder=1)

    # ax.axhline(0.5, linestyle='--', color='0.3', zorder=-10, linewidth=0.5)
    # ax.tick_params(axis='both', labelsize=fontsize)

    if xlabel is not None:
        ax.set_ylabel(ylabel, fontsize=fontsize)

    if ylabel is not None:
        ax.set_ylabel(ylabel, fontsize=fontsize)

    ax.set_ylim(0, 1)

    # Boxplot
    bp = ax.boxplot(box_plot_data, showfliers=False, zorder=2)

    for e in ['boxes', 'caps', 'whiskers', 'medians']:  # Warning: only one box, but several whiskers by plot
        for b, c in zip(bp[e], colors):
            b.set(color='black')
            b.set_alpha(1)

    plt.show()

    if f_name is not None:

        plt.savefig(f_name)


def main():

    y = np.random.random((10, 10))
    box_plot(y)
    plt.show()


if __name__ == '__main__':
    main()
