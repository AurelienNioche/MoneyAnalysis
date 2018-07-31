import matplotlib.pyplot as plt
import numpy as np


def box_plot(data, xlabel=None, ylabel=None, f_name=None):

    fig = plt.figure()
    ax = fig.add_subplot(111)
    # n = len(results.keys())
    #
    # tick_labels = [
    #     "Loss\nvs\ngains", "Diff. $x +$\nSame $p$", "Diff. $x -$\nSame $p$",
    #     "Diff. $p$\nSame $x +$", "Diff. $p$\nSame $x -$"]

    n = len(data[:, 0])
    colors = ['C0' for _ in range(n - 1)] + ['C1']
    fontsize = 10
    positions = list(range(len(data[0])))

    y_scatter = data.flatten()
    x_scatter = np.repeat(np.arange(n) + 1, len(data[0, :]))

    colors_scatter = np.array([colors[i-1] for i in x_scatter])

    # box plot reads by columns
    box_plot_data = data.transpose()#data.reshape(data.shape[1], data.shape[0])

    ax.scatter(x_scatter, y_scatter, c=colors_scatter, s=30, alpha=0.5, linewidth=0.0, zorder=1)

    # ax.axhline(0.5, linestyle='--', color='0.3', zorder=-10, linewidth=0.5)

    # ax.set_yticks(np.arange(0.4, 1.1, 0.2))

    # ax.tick_params(axis='both', labelsize=fontsize)

    # ax.set_xlabel("Type of control\nMonkey {}.".format(monkey), fontsize=fontsize)
    # ax.set_xlabel("Control type", fontsize=fontsize)
    if ylabel is not None:
        ax.set_ylabel(ylabel, fontsize=fontsize)
    # ax.set_xlim()

    # ax.set_xlim(0, 3)

    ax.set_ylim(0, 1)

    # Boxplot
    bp = ax.boxplot(box_plot_data, showfliers=False, zorder=2)

    for e in ['boxes', 'caps', 'whiskers', 'medians']:  # Warning: only one box, but several whiskers by plot
        for b, c in zip(bp[e], colors):
            b.set(color='black')
            b.set_alpha(1)

    # ax.set_aspect(3)

    if f_name is not None:

        plt.savefig(f_name)


def main():

    y = np.random.random((10, 10))
    box_plot(y)
    plt.show()


if __name__ == '__main__':
    main()
