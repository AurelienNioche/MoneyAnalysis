import matplotlib.pyplot as plt
import matplotlib.gridspec as grd
import numpy as np
import string
import os


def life_expectancy_over_t(data, fig, subplot_spec, letter=None):
    """
    :param data: (array n_good * t_max) data
    :param fig: (string) complete path
    :param subplot_spec: (SubPlotSpec) coordinates
    :param letter: (string) A, B, C....
    :return: None
    """

    keys = data.keys()
    n_good = data['n_g'].shape[0]
    n_plot = len(data)

    colors = [f'C{i}' for i in range(n_plot)]

    gs = grd.GridSpecFromSubplotSpec(subplot_spec=subplot_spec, ncols=1, nrows=n_good)

    for i in range(n_good):

        ax = fig.add_subplot(gs[i, 0])
        ax.set_ylim(0, 25)
        ax.set_xlim(0, 50)
        if i == (n_good - 1):
            ax.set_xlabel('$t$')
            ax.set_xticks([0, 50])

        else:
            ax.set_xticks([])

        ax.tick_params(labelsize=8)

        for j, k in enumerate(sorted(keys)):

            ax.plot(data[k][i, :], color=colors[j], linewidth=2)
            # ax.set_yticks([0, 1])
            # ax.set_yticklabels(['0', f'n/{n_good}'])

    ax0 = fig.add_subplot(gs[:, :])
    ax0.set_axis_off()


def plot(data, f_name=None):

    fig = plt.figure(figsize=(14, 13), dpi=200)
    fig.subplots_adjust(left=0.05, bottom=0.1, top=0.94, right=0.98)
    gs = grd.GridSpec(ncols=2, nrows=2)

    letter = (i.upper() for i in string.ascii_uppercase)

    for i, n in enumerate((3, 4)):

        col_idx = (i for i in range(4))

        life_expectancy_over_t(
            data=data[f'{n}_good_non_uniform_life_expectancy'],
            fig=fig, subplot_spec=gs[i, next(col_idx)], letter=next(letter))

        life_expectancy_over_t(
            data=data[f'{n}_good_uniform_life_expectancy'],
            fig=fig, subplot_spec=gs[i, next(col_idx)], letter=next(letter))

    if f_name is not None:
        os.makedirs(os.path.dirname(f_name), exist_ok=True)
        plt.savefig(f_name)
    plt.show()


if __name__ == '__main__':

    example_data = {
        "3_good_non_uniform_life_expectancy":
            {
                'n_g': np.random.random((3, 50)),
                'n_remaining': np.random.random((3, 50)),
                'n_prod': np.random.random((3, 50)),
                'n_cons': np.random.random((3, 50)),
            },

        "4_good_non_uniform_life_expectancy":
            {
                'n_g': np.random.random((4, 50)),
                'n_remaining': np.random.random((4, 50)),
                'n_prod': np.random.random((4, 50)),
                'n_cons': np.random.random((4, 50)),
            },

        "3_good_uniform_life_expectancy":
            {
                'n_g': np.random.random((3, 50)),
                'n_remaining': np.random.random((3, 50)),
                'n_prod': np.random.random((3, 50)),
                'n_cons': np.random.random((3, 50)),
            },
        "4_good_uniform_life_expectancy":
            {
                'n_g': np.random.random((4, 50)),
                'n_remaining': np.random.random((4, 50)),
                'n_prod': np.random.random((4, 50)),
                'n_cons': np.random.random((4, 50)),
            },
    }

    plot(example_data)
