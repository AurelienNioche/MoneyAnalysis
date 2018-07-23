import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as grd
import string

import analysis.graph.monetary_and_medium_bar
import analysis.graph.monetary_and_medium_over_time


def experiment(data, titles, f_name, exp=True):

    """
    Conditions uniform and non-uniform for a specific number of goods (3 or 4)
    :param data:
    :param titles:
    :param f_name:
    :param exp:
    :return:
    """

    fig = plt.figure(figsize=(15, 9), dpi=200)
    gs = grd.GridSpec(ncols=2, nrows=1)

    subplot_specs = (gs[x, y] for x, y in ((0, 0), (0, 1)))
    letters = (s.capitalize() for s in string.ascii_letters)

    for d, t in zip(data, titles):
        experiment_subplot(d, t,
                           f_name=f_name, letter=next(letters), exp=exp,
                           subplot_spec=next(subplot_specs), fig=fig)

    plt.subplots_adjust(bottom=0.1, right=0.98, top=0.9, left=0.04)
    # plt.tight_layout()
    plt.savefig(f_name)


def experiment_subplot(data, title, f_name, exp=True, letter=None,
                       subplot_spec=None, fig=None):

    if subplot_spec:
        gs = grd.GridSpecFromSubplotSpec(ncols=2, nrows=2,
                                         width_ratios=[3, 1], height_ratios=[5, 1],
                                         subplot_spec=subplot_spec)

    else:
        fig = plt.figure(figsize=(10, 10))
        gs = grd.GridSpec(ncols=2, nrows=2, width_ratios=[3, 1], height_ratios=[5, 1])

    # --------------------- #

    analysis.graph.monetary_and_medium_over_time.monetary_bhv_over_t(
        data['monetary_over_t'],
        n_side=len(data['distribution']),
        mean_plot=data.get('monetary_over_t_means'),
        fig=fig, subplot_spec=gs[0, 0], exp=exp)

    # --------------------- #

    analysis.graph.monetary_and_medium_over_time.medium_over_t(
        data['medium_over_t'],
        fig=fig, subplot_spec=gs[0, 1], mean_plot=data.get('medium_over_t_means'))

    # --------------------- #

    analysis.graph.monetary_and_medium_bar.plot(
        means=data['monetary_bar'][0],
        errors=data['monetary_bar'][1],
        sig=data['monetary_bar'][2],
        subplot_spec=gs[1, 0],
        title='',
        xlabel='Good',
        ylabel='Monetary behavior',
        fig=fig,
    )

    analysis.graph.monetary_and_medium_bar.plot(
        means=data['medium_bar'][0],
        errrors=data['medium_bar'][1],
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

    ax.text(s=title.replace('_', ' ').replace('good', 'goods').upper(), x=0.4, y=1.07, fontsize=10)
    ax.text(s=letter, x=-0.05, y=-0.1, fontsize=20)


# ---------------------------------------------------- EXAMPLE ----------------------------------------------- #


def experiment_example(n_good=3):

    data = []
    titles = ('Uniform', 'Non uniform')

    for _ in titles:

        monetary_means, monetary_err = np.random.random((2, n_good))
        money_sig = [(0, i+1, np.random.choice([False, True])) for i in range(n_good)]

        monetary_over_t = [
            np.random.random((n_good, n_good, 50)),
            np.random.random((n_good, n_good, 50))
        ]

        monetary_over_t_means = np.random.random((n_good, n_good, 50))

        medium_means, medium_err = np.random.random((2, n_good))
        med_sig = [(0, i+1, np.random.choice([False, True])) for i in range(n_good)]

        med_over_t = [
            np.random.random((n_good, 50)),
            np.random.random((n_good, 50))
        ]

        medium_over_t_means = np.random.random((n_good, 50)) * 0.5

        distribution = [10, ] * n_good

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

    experiment(data=data, titles=titles, f_name=f'../../fig/exp_{n_good}_example.pdf', exp=False)


if __name__ == '__main__':

    experiment_example()
