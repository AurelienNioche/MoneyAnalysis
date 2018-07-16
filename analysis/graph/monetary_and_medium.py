import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as grd
import os
import string
import itertools as it

import analysis.tools.format
import analysis.compute.monetary_and_medium


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


def monetary_behavior_over_t(data, fig, subplot_spec, letter=None, title=None):

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


def _bar_plots(means, errors, labels,
               ylabel=None, xlabel=None, ax=None, letter=None, title=None, sig=None):

    if ax is None:
        print('No ax given, I will create a fig.')
        fig, ax = plt.subplots()

    if letter:
        ax.text(
            s=letter, x=-0.1, y=-0.68, horizontalalignment='center', verticalalignment='center',
            transform=ax.transAxes,
            fontsize=20)

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

    if sig:

        y_inc_line = 0.08
        y_inc_text = 0.11

        for i, j, k in sig:
            # For significance bars

            # ax.axhline(y=max(means[i:j+1])+y_inc_line, xmin=(1/len(means)) * i, xmax=(1/len(means)) * j, color='black')
            ax.axhline(y=max(means[i:j+1])+y_inc_line, xmin=(i/2) + 0.1, xmax=(j/2) + 0.1, color='black')
            if k:
                ax.text(s='***',
                        y=max(means[i:j+1])+y_inc_text, x=(i+j)/2, horizontalalignment='center', verticalalignment='center')
            else:
                ax.text(s='NS',
                        y=max(means[i:j+1])+y_inc_text, x=(i+j)/2, horizontalalignment='center', verticalalignment='center')
            y_inc_text += 0.1
            y_inc_line += 0.1

                # ax.axhline(y=max(means[2:4]) + 0.06, xmin=0.63, xmax=0.88, color='black')
            # ax.text(s='***',
            #         y=max(means[2:4]) + 0.085, x=2.5, horizontalalignment='center', verticalalignment='center')

        ax.set_ylim(0, 1)
    ax.set_yticks((0, 0.5, 1))

    ax.set_ylabel(ylabel)
    ax.set_xlabel(xlabel)

    ax.set_title(title)

    # create
    ax.bar(labels_pos, means, yerr=errors, edgecolor="white", align="center", color="grey")
    

def one_condition(data, f_name):

    coord = it.product(range(2), range(3))
    gs = grd.GridSpec(nrows=2, ncols=3)

    fig = plt.figure(figsize=(14, 14))

    for i in range(len(data['repartition'])):
        data_mbh = analysis.tools.format.for_monetary_behavior_over_t(data['monetary_bhv'][i], data['repartition'])

        monetary_behavior_over_t(data=data_mbh, fig=fig, subplot_spec=gs[next(coord)], title=f'm={i}')

    data_m = analysis.tools.format.for_medium_over_t(data['medium'], data['repartition'])
    medium_over_t(data=data_m, fig=fig, subplot_spec=gs[next(coord)])

    plt.tight_layout()

    if f_name is not None:
        os.makedirs('fig', exist_ok=True)
        plt.savefig(f'fig/{f_name}')


def one_condition_money_bar(data, title, subplot_spec=None, fig=None):

    if not fig:
        fig = plt.figure()

    means, err = analysis.tools.format.for_monetary_behavior_bar_plot(data)

    if title == '3_good_non_uniform':
        sig = [(0, 1, False), (0, 2, False)]

    elif title == '3_good_uniform':
        sig = [(0, 1, True), (0, 2, False)]

    elif title == '4_good_non_uniform':
        sig = [(0, 1, False), (0, 2, True), (0, 3, False)]

    elif title == '4_good_uniform':
        sig = [(0, 1, False), (0, 2, False), (0, 3, False)]
    else:
        sig = None

    _bar_plots(
        means=means,
        errors=err,
        labels=[str(i + 1) for i in range(len(means))],
        xlabel='Good',
        ylabel='Monetary behavior',
        ax=fig.add_subplot(subplot_spec) if subplot_spec else fig.add_subplot(),
        title=title,
        sig=sig
    )

    plt.savefig(f'fig/bar_plot_monetary_bhv_{title}.pdf')


def one_condition_medium_bar(data, title, subplot_spec=None, fig=None):

    if not fig:
        fig = plt.figure()

    means, err = analysis.tools.format.for_medium_bar_plot(data)

    if title == '3_good_non_uniform':
        sig = [(0, 1, False), (0, 2, False)]

    elif title == '3_good_uniform':
        sig = [(0, 1, False), (0, 2, False)]

    elif title == '4_good_non_uniform':
        sig = [(0, 1, False), (0, 2, True), (0, 3, True)]

    elif title == '4_good_uniform':
        sig = [(0, 1, False), (0, 2, False), (0, 3, False)]
    else:
        sig = None

    _bar_plots(
        means=means,
        errors=err,
        labels=[str(i + 1) for i in range(len(means))],
        xlabel='Good',
        ylabel='Used as medium',
        ax=fig.add_subplot(subplot_spec) if subplot_spec else fig.add_subplot(),
        title=title,
        sig=sig
    )

    plt.savefig(f'fig/bar_plot_medium_{title}.pdf')


def one_condition_monetary_behavior_all_goods(data, fig, subplot_spec):

    n_good = len(data['repartition'])

    coord = it.product(range(n_good), range(n_good))
    gs = grd.GridSpecFromSubplotSpec(nrows=n_good, ncols=n_good, subplot_spec=subplot_spec)

    for i in range(n_good):
        data_mbh = analysis.tools.format.for_monetary_behavior_over_t(data['monetary_bhv'][i], data['repartition'])

        monetary_behavior_over_t(data=data_mbh, fig=fig, subplot_spec=gs[next(coord)], title=f'm={i}')


def one_condition_medium(data, fig, subplot_spec):

    medium = analysis.tools.format.for_medium_over_t(data['medium'], repartition=data['repartition'])

    medium_over_t(medium, fig=fig, subplot_spec=subplot_spec)


def overall_one_condition(data, f_name):

    fig = plt.figure(figsize=(10, 13)) # fig.subplots_adjust(left=0.05, bottom=0.1, top=0.94, right=0.98)
    gs = grd.GridSpec(ncols=2, nrows=2, width_ratios=[0.7, 0.3], height_ratios=[0.8, 0.2])

    one_condition_monetary_behavior_all_goods(data, fig=fig, subplot_spec=gs[0, 0])
    one_condition_money_bar(data['monetary_bhv'], subplot_spec=gs[1, 0], title=f_name, fig=fig)
    one_condition_medium_bar(data['medium'], subplot_spec=gs[1, 1], title=f_name, fig=fig)

    plt.show()


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

    _bar_plots(
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


if __name__ == '__main__':

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
