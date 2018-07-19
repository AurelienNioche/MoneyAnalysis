import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as grd
import os
import string
import itertools as it

# import analysis.tools.format
# import analysis.compute.monetary_and_medium


def _bar(means, errors, labels, title, subplot_spec=None, fig=None):

    if subplot_spec:
        ax = fig.add_subplot(subplot_spec)
    else:
        fig, ax = plt.figure()

    # Hide spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    ax.tick_params(length=0)
    ax.set_title(f"$\{title}$", fontsize=20)

    # print(labels)

    # Set x labels
    labels_pos = np.arange(len(labels))
    ax.set_xticklabels(labels)
    ax.set_xticks(labels_pos)

    ax.set_ylim(0, 1)

    # create
    ax.bar(labels_pos, means, yerr=errors, edgecolor="white", align="center", color="black")


def bar_plots(means, errors, labels=None,
               ylabel=None, xlabel=None, ax=None, letter=None, title=None, sig=None):

    if ax is None:
        # print('No ax given, I will create a fig.')
        fig, ax = plt.subplots()

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
    ax.tick_params(axis='x', length=0)

    # print(labels)

    # Set x labels
    labels_pos = np.arange(len(labels))
    ax.set_xticklabels(labels) #rotation='vertical')
    ax.set_xticks(labels_pos)

    # For significance bars
    if sig:

        y_inc_line = 0.08
        y_inc_text = 0.11

        shift = 0.1

        for idx, (i, j, k) in enumerate(sig):

            print(i, j, k)
            x = (i+j)/2
            y = max(means[i:j+1])

            ax.hlines(y=y + y_inc_line + shift*idx,
                      xmin=i, xmax=j, color='black')

            ax.text(s='***' if k else 'NS',
                    x=x,
                    y=y + y_inc_text + shift*idx,
                    horizontalalignment='center', verticalalignment='center')

    ax.set_ylim(0, 1)

    ax.set_yticks((0, 0.5, 1))

    ax.set_ylabel(ylabel)
    ax.set_xlabel(xlabel)

    ax.set_title(title)

    # create
    ax.bar(labels_pos, means, yerr=errors, edgecolor="white", align="center", color="grey")
    

def one_condition_bar(means, err, title,
                             xlabel=None, ylabel=None, sig=None,
                             subplot_spec=None, fig=None, f_name='fig/random_bar_plot.pdf'):

    if not fig:
        fig = plt.figure()

    bar_plots(
        means=means,
        errors=err,
        xlabel=xlabel,
        ylabel=ylabel,
        ax=fig.add_subplot(subplot_spec) if subplot_spec else fig.add_subplot(),
        title=title,
        sig=sig
    )

    plt.savefig(f_name)


def main():

    np.random.seed(123)
    means = np.random.random(size=3)
    errors = np.random.random(size=3) / 100
    sig = [(0, 1, True), (0, 2, False)]
    bar_plots(means=means, errors=errors, sig=sig)

    plt.show()


if __name__ == '__main__':

    main()
