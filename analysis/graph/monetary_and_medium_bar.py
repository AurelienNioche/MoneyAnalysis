import matplotlib.pyplot as plt
import numpy as np


def plot(
        means, errors, sig=None,
        title=None,
        xlabel=None, xlabel_fontsize=10, ylabel=None, ylabel_fontsize=10, xticks_fontsize=5,
        subplot_spec=None, fig=None, f_name=None, letter=None, labels=None):

    if fig is None:
        fig = plt.figure()

    ax = fig.add_subplot(subplot_spec) if subplot_spec else fig.add_subplot()

    if letter:
        ax.text(
            s=letter, x=-0.1, y=-0.68, horizontalalignment='center', verticalalignment='center',
            transform=ax.transAxes,
            fontsize=20)

    if labels is None:
        labels = [str(i + 1) for i in range(len(means))]

    # Hide spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    ax.tick_params(axis='y', labelsize=8)
    ax.tick_params(axis='x', length=0, labelsize=xticks_fontsize)

    # Set x labels
    labels_pos = np.arange(len(labels))
    ax.set_xticklabels(labels)
    ax.set_xticks(labels_pos)

    # For significance bars
    if sig:

        y_inc_line = 0.05
        y_inc_text = 0.07

        shift = 0.11

        for idx, (i, j, k) in enumerate(sig):

            x = (i+j)/2
            y = max(means[i:j+1])

            ax.hlines(y=y + y_inc_line + shift*idx,
                      xmin=i, xmax=j, color='black')

            if k < 0.001:
                s = '***'
            elif k < 0.01:
                s = '**'
            elif k < 0.05:
                s = '*'
            else:
                s = '$^{ns}$'

            ax.text(s=s,
                    x=x,
                    y=y + y_inc_text + shift*idx,
                    horizontalalignment='center', verticalalignment='center')

    ax.set_ylim(0, 1)

    ax.set_yticks((0, 0.5, 1))

    ax.set_ylabel(ylabel, fontsize=ylabel_fontsize)
    ax.set_xlabel(xlabel, fontsize=xlabel_fontsize)

    ax.set_title(title)

    # Create
    ax.bar(labels_pos, means, yerr=errors, edgecolor="white", align="center", color="grey")

    if f_name is not None:
        plt.savefig(f_name)


def plot_example():

    np.random.seed(123)
    means = np.random.random(size=3)
    errors = np.random.random(size=3) / 100
    sig = [(0, 1, True), (0, 2, False)]
    plot(means=means, errors=errors, sig=sig)

    plt.show()


if __name__ == '__main__':
    plot_example()
