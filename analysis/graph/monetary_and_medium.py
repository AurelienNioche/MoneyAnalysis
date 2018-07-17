import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as grd
import os
import string
import itertools as it

import analysis.graph.monetary_and_medium_bar


def monetary_behavior_over_t(data, fig, subplot_spec, letter=None, title=None, xlabel=True):

    """
    :param data: (array n_good * t_max) data
    :param fig: (string) complete path
    :param subplot_spec: (SubPlotSpec) coordinates
    :param letter: (string) A, B, C....
    :return: None
    """

    n_good = len(data)
    colors = [f'C{i}' for i in range(n_good)]

    gs = grd.GridSpecFromSubplotSpec(subplot_spec=subplot_spec, ncols=1, nrows=n_good)

    for i in range(n_good):

        ax = fig.add_subplot(gs[i, 0])
        ax.plot(data[i], color=colors[i], linewidth=2)
        ax.set_yticks([0, 1])
        ax.set_ylim(-0.1, 1.1)
        ax.set_xlim(0, len(data[i]))

        ax.axhline(y=1 / (n_good - 1), linewidth=1, linestyle='--', color='0.5', zorder=-10)

        if i == (n_good - 1):
            ax.set_xlabel('$t$')
            ax.set_xticks([0, len(data[i])])
        else:
            ax.set_xticks([])

        ax.tick_params(labelsize=8)

    ax0 = fig.add_subplot(gs[:, :])
    ax0.set_axis_off()

    if xlabel:
        ax0.text(s="Monetary behavior", x=-0.15, y=0.5, horizontalalignment='center', verticalalignment='center',
             transform=ax0.transAxes, fontsize=10, rotation='vertical')

    if letter:
        ax0.text(
            s=letter, x=-0.1, y=-0.1, horizontalalignment='center', verticalalignment='center',
            transform=ax0.transAxes,
            fontsize=20)

    if title is not None:
        ax0.set_title(title)


def medium_over_t(data, fig, subplot_spec, letter=None):

    """
    :param data: (array n_good * t_max) data
    :param fig: (string) complete path
    :param subplot_spec: (SubPlotSpec) coordinates
    :param letter: (string) A, B, C....
    :return: None
    """

    n_good = len(data)
    colors = [f'C{i+4}' for i in range(n_good)]

    gs = grd.GridSpecFromSubplotSpec(subplot_spec=subplot_spec, ncols=1, nrows=n_good)

    for i in range(n_good):

        ax = fig.add_subplot(gs[i, 0])
        ax.plot(data[i], color=colors[i], linewidth=2)
        ax.set_yticks([0, 1])
        # ax.set_yticklabels(['0', f'n/{n_good}'])
        ax.set_ylim(-0.01, 1.01)
        ax.set_xlim(0, len(data[i]))
        if i == (n_good - 1):
            ax.set_xlabel('$t$')
            ax.set_xticks([0, len(data[i])])

        else:
            ax.set_xticks([])

        ax.axhline(y=0.5, linewidth=1, linestyle='--', color='0.5', zorder=-10)

        ax.tick_params(labelsize=8)

    ax0 = fig.add_subplot(gs[:, :])
    ax0.set_axis_off()

    ax0.text(s="Used as medium", x=-0.2, y=0.5, horizontalalignment='center', verticalalignment='center',
             transform=ax0.transAxes, fontsize=10, rotation='vertical')

    if letter:
        ax0.text(
            s=letter, x=-0.1, y=-0.1, horizontalalignment='center', verticalalignment='center',
            transform=ax0.transAxes,
            fontsize=20)


def one_condition_monetary_behavior_all_goods(data, fig, subplot_spec):

    n_good = len(data['repartition'])

    coord = it.product(range(n_good), range(n_good))
    gs = grd.GridSpecFromSubplotSpec(nrows=1, ncols=n_good, subplot_spec=subplot_spec)

    for i in range(n_good):

        monetary_behavior_over_t(
            data=data['monetary_over_t'][i],
            fig=fig, subplot_spec=gs[next(coord)],
            title=f'm={i}',
            xlabel=i == 0
        )


def overall_one_condition(data, title, f_name):

    fig = plt.figure(figsize=(10, 10)) # fig.subplots_adjust(left=0.05, bottom=0.1, top=0.94, right=0.98)
    gs = grd.GridSpec(ncols=2, nrows=2, width_ratios=[3, 1], height_ratios=[5, 1])

    one_condition_monetary_behavior_all_goods(data, fig=fig, subplot_spec=gs[0, 0])

    medium_over_t(data['medium_over_t'], fig=fig, subplot_spec=gs[0, 1])

    analysis.graph.monetary_and_medium_bar.one_condition_bar(
        means=data['monetary_bar'][0],
        err=data['monetary_bar'][1],
        subplot_spec=gs[1, 0],
        # title=f_name,
        title='',
        xlabel='Good',
        ylabel='Monetary behavior',
        fig=fig
    )

    analysis.graph.monetary_and_medium_bar.one_condition_bar(
        means=data['medium_bar'][0],
        err=data['medium_bar'][1],
        subplot_spec=gs[1, 1],
        xlabel='Good',
        ylabel='Used as medium',
        # title=f_name,
        title='',
        fig=fig
    )

    set_title_with_fake_fig(title=title, subplot_spec=gs[:, :], fig=fig)

    plt.savefig(f_name)


def set_title_with_fake_fig(title, subplot_spec, fig):

    ax = fig.add_subplot(subplot_spec)

    for k in ax.spines.keys():
        ax.spines[k].set_visible(False)

    ax.patch.set_alpha(0)
    ax.set_xticks([])
    ax.set_yticks([])
    # ax.set_xtickslabel([])

    ax.text(s=title.replace('_', ' ').capitalize(), x=0.4, y=1.1, fontsize=20)


def overall(data):

    fig = plt.figure(figsize=(14, 6), dpi=200)
    fig.subplots_adjust(left=0.05, bottom=0.1, top=0.94, right=0.98)
    gs = grd.GridSpec(ncols=5, nrows=2, width_ratios=[1, 1, 1, 1, 0.4], wspace=0.4, hspace=0.3)

    letter = (i.upper() for i in string.ascii_uppercase)

    for i, n in enumerate((3, 4)):
        col_idx = (i for i in range(4))

        monetary_behavior_over_t(
            data=data[f'{n}_good_non_uniform_monetary_behavior'],
            fig=fig, subplot_spec=gs[i, next(col_idx)], letter=next(letter))

        medium_over_t(
            data=data[f'{n}_good_non_uniform_medium'],
            fig=fig, subplot_spec=gs[i, next(col_idx)], letter=next(letter))

        monetary_behavior_over_t(
            data=data[f'{n}_good_uniform_monetary_behavior'],
            fig=fig, subplot_spec=gs[i, next(col_idx)], letter=next(letter))

        medium_over_t(
            data=data[f'{n}_good_uniform_medium'],
            fig=fig, subplot_spec=gs[i, next(col_idx)], letter=next(letter))

    ax = fig.add_subplot(gs[:, 4])

    analysis.graph.monetary_and_medium_bar.bar_plots(
        [
            data['3_good_non_uniform_mean'],
            data['3_good_uniform_mean'],
            data['4_good_non_uniform_mean'],
            data['4_good_uniform_mean']
        ],
        [
            data['3_good_non_uniform_sem'],
            data['3_good_uniform_sem'],
            data['4_good_non_uniform_sem'],
            data['4_good_uniform_sem']
        ],
        labels=
        [
            '3 goods - Non-un. rep.',
            '3 goods - Un. rep.',
            '4 goods - Non-un. rep.',
            '4 goods - Un. rep.'
        ],
        ax=ax, letter=next(letter))

    ax.set_aspect(aspect=14.5, anchor='NE')

    ax0 = fig.add_subplot(gs[:, :])
    ax0.set_axis_off()

    ax0.text(
        s='Non-uniform repartition', x=0.2, y=1.05, horizontalalignment='center', verticalalignment='center',
        transform=ax0.transAxes,
        fontsize=15)

    ax0.text(
        s='Uniform repartition', x=0.65, y=1.05, horizontalalignment='center', verticalalignment='center',
        transform=ax0.transAxes,
        fontsize=15)

    ax0.text(
        s='4 goods', x=-0.045, y=0.22, horizontalalignment='center', verticalalignment='center',
        transform=ax0.transAxes, rotation='vertical',
        fontsize=15)

    ax0.text(
        s='3 goods', x=-0.045, y=0.76, horizontalalignment='center', verticalalignment='center',
        transform=ax0.transAxes, rotation='vertical',
        fontsize=15)

    f_name = 'fig/results.pdf'

    os.makedirs(os.path.dirname(f_name), exist_ok=True)
    plt.savefig(f_name)
    plt.show()


def overall_example():

    example_data = {
        "3_good_non_uniform_monetary_behavior": np.random.random((3, 50)),
        "3_good_non_uniform_medium": np.random.random((3, 50)),
        "3_good_uniform_monetary_behavior": np.random.random((3, 50)),
        "3_good_uniform_medium": np.random.random((3, 50)),
        "4_good_non_uniform_monetary_behavior": np.random.random((4, 50)),
        "4_good_non_uniform_medium": np.random.random((4, 50)),
        "4_good_uniform_monetary_behavior": np.random.random((4, 50)),
        "4_good_uniform_medium": np.random.random((4, 50)),
        "3_good_non_uniform_mean": np.random.random(),
        "3_good_uniform_mean": np.random.random(),
        "4_good_non_uniform_mean": np.random.random(),
        "4_good_uniform_mean": np.random.random(),
        "3_good_non_uniform_sem": np.random.random() / 100,
        "3_good_uniform_sem":  np.random.random() / 100,
        "4_good_non_uniform_sem": np.random.random() / 100,
        "4_good_uniform_sem": np.random.random() / 100,
    }

    overall(example_data)


if __name__ == '__main__':

    overall_example()
