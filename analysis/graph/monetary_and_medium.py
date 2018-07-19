import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as grd
import itertools as it
import string

import analysis.graph.monetary_and_medium_bar


def _monetary_behavior_over_t(data, fig, subplot_spec,
                             letter=None, title=None, xlabel=True,
                             mean_plot=None, thick_linewidth=2, thin_linewidth=0.5,
                             alpha=0.3):
    """
    :param data: either one (array n_good * t_max) data/ or a list [(array n_good * tmax), ...]
    :param fig:
    :param subplot_spec:
    :param letter:
    :param title:
    :param xlabel:
    :param mean_plot:
    :param thick_linewidth:
    :param thin_linewidth:
    :param alpha:
    :return:
    """

    n_good = len(data[0]) if mean_plot is not None else len(data)

    colors = [f'C{i}' for i in range(n_good)]

    gs = grd.GridSpecFromSubplotSpec(subplot_spec=subplot_spec, ncols=1, nrows=n_good)

    for i in range(n_good):

        ax = fig.add_subplot(gs[i, 0])

        if mean_plot is not None:
            for j in range(len(data)):
                ax.plot(data[j][i], color=colors[i], linewidth=thin_linewidth, alpha=alpha)

            ax.plot(mean_plot[i], color=colors[i], linewidth=thick_linewidth)
        else:
            ax.plot(data[i], color=colors[i], linewidth=thick_linewidth)

        ax.set_yticks([0, 1])
        ax.set_ylim(-0.1, 1.1)

        if mean_plot is not None:
            ax.set_xlim(0, len(data[0][i]))
        else:
            ax.set_xlim(0, len(data[i]))

        ax.axhline(y=1 / (n_good - 1), linewidth=1, linestyle='--', color='0.5', zorder=-10)

        if i == (n_good - 1):
            ax.set_xlabel('$t$')

            if mean_plot is not None:

                ax.set_xticks([0, len(data[0][i])])
            else:
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


def _medium_over_t(data, fig, subplot_spec, thick_linewidth=2, thin_linewidth=0.5, alpha=0.3,
                  letter=None, mean_plot=None):
    """
    :param data: either one (array n_good * t_max) data/ or a list [(array n_good * tmax), ...]
    :param fig:
    :param subplot_spec:
    :param thick_linewidth:
    :param thin_linewidth:
    :param alpha:
    :param letter:
    :param mean_plot:
    :return:
    """

    n_good = len(data[0]) if mean_plot is not None else len(data)
    colors = [f'C{i+4}' for i in range(n_good)]

    gs = grd.GridSpecFromSubplotSpec(subplot_spec=subplot_spec, ncols=1, nrows=n_good)

    for i in range(n_good):

        ax = fig.add_subplot(gs[i, 0])

        if mean_plot is not None:
            for j in range(len(data)):
                ax.plot(data[j][i], color=colors[i], linewidth=thin_linewidth, alpha=alpha)

            ax.plot(mean_plot[i], color=colors[i], linewidth=thick_linewidth)
        else:
            ax.plot(data[i], color=colors[i], linewidth=thick_linewidth)

        ax.set_yticks([0, 1])
        ax.set_ylim(-0.01, 1.01)

        if mean_plot is not None:
            ax.set_xlim(0, len(data[0][i]))
        else:
            ax.set_xlim(0, len(data[i]))

        if i == (n_good - 1):

            ax.set_xlabel('$t$')

            if mean_plot is not None:

                ax.set_xticks([0, len(data[0][i])])
            else:
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


def _one_condition_monetary_behavior_all_goods(data, mean_plot, n_side, fig, subplot_spec, exp):

    coord = it.product(range(n_side), range(n_side))
    gs = grd.GridSpecFromSubplotSpec(nrows=1, ncols=n_side, subplot_spec=subplot_spec)

    for i in range(n_side):

        _monetary_behavior_over_t(
            # If the graph is generated from experiment data, each column (the good considered as money) is one 'i'.
            # If the graph is generated from simulation data, 'i' stills represents one column
            # (the good considered as money),
            # but there are multiple economies so multiple curves (each curves representing
            # one simulated economy and the mean plot is the mean computed from these economies)
            data=data[i] if exp else [j[i] for j in data],
            mean_plot=mean_plot[i] if mean_plot is not None else None,
            fig=fig, subplot_spec=gs[next(coord)],
            title=f'm={i+1}',
            xlabel=i == 0
        )


def overall_one_good(data, titles, f_name, exp=True):

    fig = plt.figure(figsize=(10, 7), dpi=200)
    gs = grd.GridSpec(ncols=2, nrows=1)

    subplot_specs = (gs[x, y] for x, y in ((0, 0), (0, 1)))
    letters = (s.capitalize() for s in string.ascii_letters)

    for d, t in zip(data, titles):
        overall_one_condition(d, t,
                              f_name=f_name, letter=next(letters), exp=exp,
                              subplot_spec=next(subplot_specs), fig=fig)

    # plt.tight_layout()
    plt.savefig(f_name)


def overall_one_condition(data, title, f_name, exp=True, letter=None,
                          subplot_spec=None, fig=None):

    if subplot_spec:
        gs = grd.GridSpecFromSubplotSpec(ncols=2, nrows=2,
                                         width_ratios=[3, 1], height_ratios=[5, 1],
                                         subplot_spec=subplot_spec)

    else:
        fig = plt.figure(figsize=(10, 10))
        gs = grd.GridSpec(ncols=2, nrows=2, width_ratios=[3, 1], height_ratios=[5, 1])

    # --------------------- #

    _one_condition_monetary_behavior_all_goods(data['monetary_over_t'],
                                               n_side=len(data['repartition']),
                                               mean_plot=data.get('monetary_over_t_means'),
                                               fig=fig, subplot_spec=gs[0, 0], exp=exp)

    # --------------------- #

    _medium_over_t(data['medium_over_t'],
                  fig=fig, subplot_spec=gs[0, 1], mean_plot=data.get('medium_over_t_means'))

    # --------------------- #

    analysis.graph.monetary_and_medium_bar.one_condition_bar(
        means=data['monetary_bar'][0],
        err=data['monetary_bar'][1],
        sig=data['monetary_bar'][2],
        subplot_spec=gs[1, 0],
        title='',
        xlabel='Good',
        ylabel='Monetary behavior',
        fig=fig,
    )

    analysis.graph.monetary_and_medium_bar.one_condition_bar(
        means=data['medium_bar'][0],
        err=data['medium_bar'][1],
        sig=data['medium_bar'][2],
        subplot_spec=gs[1, 1],
        xlabel='Good',
        ylabel='Used as medium',
        title='',
        fig=fig,
    )

    _set_title_using_fake_fig(title=title, subplot_spec=gs[:, :], fig=fig, letter=letter)

    if f_name:
        plt.savefig(f_name)


def _set_title_using_fake_fig(title, subplot_spec, fig, letter):

    ax = fig.add_subplot(subplot_spec)

    for k in ax.spines.keys():
        ax.spines[k].set_visible(False)

    ax.patch.set_alpha(0)
    ax.set_xticks([])
    ax.set_yticks([])
    # ax.set_xtickslabel([])

    ax.text(s=title.replace('_', ' ').capitalize(), x=0.4, y=1.1, fontsize=10)
    ax.text(s=letter, x=0.05, y=0.05, fontsize=10)

    # ---------------------------------------------------- EXAMPLES ----------------------------------------------- #


def overall_one_condition_example():

    monetary_means, monetary_err = np.random.random((2, 3))
    money_sig = [(0, 1, False), (0, 2, True)]

    monetary_over_t = [
        np.ones((3, 3, 50)) * 0.1,
        np.ones((3, 3, 50)) * 0.8
    ]

    monetary_over_t_means = np.ones((3, 3, 50)) * 0.5

    medium_means, medium_err = np.random.random((2, 3))
    med_sig = [(0, 1, False), (0, 2, True)]

    med_over_t = [
        np.ones((3, 50)) * 0.1,
        np.ones((3, 50)) * 0.8
    ]

    medium_over_t_means = np.ones((3, 50)) * 0.5

    repartition = [10, 10, 10]

    example_data = {
        'monetary_bar': (monetary_means, monetary_err, money_sig),
        'monetary_over_t': monetary_over_t,
        'monetary_over_t_means': monetary_over_t_means,
        'medium_bar': (medium_means, medium_err, med_sig),
        'medium_over_t': med_over_t,
        'medium_over_t_means': medium_over_t_means,
        'repartition': repartition
    }

    overall_one_condition(data=example_data, title='tamere', f_name='fig/tonpere.pdf', exp=False)


def overall_one_good_example():

    for good in (3, 4):

        data = []
        titles = ('tamere', 'tonpere')

        for t in titles:

            monetary_means, monetary_err = np.random.random((2, good))
            money_sig = [(0, i+1, np.random.choice([False, True])) for i in range(good)]

            monetary_over_t = [
                np.ones((good, good, 50)) * 0.1,
                np.ones((good, good, 50)) * 0.8
            ]

            monetary_over_t_means = np.ones((good, good, 50)) * 0.5

            medium_means, medium_err = np.random.random((2, good))
            med_sig = [(0, i+1, np.random.choice([False, True])) for i in range(good)]

            med_over_t = [
                np.ones((good, 50)) * 0.1,
                np.ones((good, 50)) * 0.8
            ]

            medium_over_t_means = np.ones((good, 50)) * 0.5

            repartition = [10, ] * good

            example_data = {
                'monetary_bar': (monetary_means, monetary_err, money_sig),
                'monetary_over_t': monetary_over_t,
                'monetary_over_t_means': monetary_over_t_means,
                'medium_bar': (medium_means, medium_err, med_sig),
                'medium_over_t': med_over_t,
                'medium_over_t_means': medium_over_t_means,
                'repartition': repartition
            }

            data.append(example_data)

        overall_one_good(data=data, titles=titles, f_name=f'fig/tonpere{good}.pdf', exp=False)


if __name__ == '__main__':

    overall_one_condition_example()
