import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as grd
import itertools as it
import string

import analysis.graph.monetary_and_medium_bar
import analysis.graph.monetary_and_medium_over_time

def _one_condition_monetary_behavior_all_goods(data, mean_plot, n_side, fig, subplot_spec, exp):

    coord = it.product(range(n_side), range(n_side))
    gs = grd.GridSpecFromSubplotSpec(nrows=1, ncols=n_side, subplot_spec=subplot_spec)

    for i in range(n_side):

        analysis.graph.monetary_and_medium_over_time.monetary_behavior_over_t(
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
                                               n_side=len(data['distribution']),
                                               mean_plot=data.get('monetary_over_t_means'),
                                               fig=fig, subplot_spec=gs[0, 0], exp=exp)

    # --------------------- #

    analysis.graph.monetary_and_medium_over_time.medium_over_t(data['medium_over_t'],
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

    distribution = [10, 10, 10]

    example_data = {
        'monetary_bar': (monetary_means, monetary_err, money_sig),
        'monetary_over_t': monetary_over_t,
        'monetary_over_t_means': monetary_over_t_means,
        'medium_bar': (medium_means, medium_err, med_sig),
        'medium_over_t': med_over_t,
        'medium_over_t_means': medium_over_t_means,
        'distribution': distribution
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

            distribution = [10, ] * good

            example_data = {
                'monetary_bar': (monetary_means, monetary_err, money_sig),
                'monetary_over_t': monetary_over_t,
                'monetary_over_t_means': monetary_over_t_means,
                'medium_bar': (medium_means, medium_err, med_sig),
                'medium_over_t': med_over_t,
                'medium_over_t_means': medium_over_t_means,
                'distribution': distribution
            }

            data.append(example_data)

        overall_one_good(data=data, titles=titles, f_name=f'fig/tonpere{good}.pdf', exp=False)


if __name__ == '__main__':

    overall_one_condition_example()
