import matplotlib.pyplot as plt
import matplotlib.gridspec as grd
import numpy as np


def curve(mean, sem, cond='', n_good='', agent_type='', ax=None,
          ylabel=None, legend=None):

    if ax is None:
        fig = plt.figure(figsize=(15, 12))
        ax = fig.subplots()

    ax.plot(mean, lw=1.5, label=legend)
    ax.fill_between(
        range(len(mean)),
        y1=mean - sem,
        y2=mean + sem,
        alpha=0.5
    )

    # ax.spines['right'].set_visible(0)
    # ax.spines['top'].set_visible(0)
    ax.set_xlabel('t')
    ax.set_ylabel(ylabel)
    ax.set_ylim((0, 1))

    if n_good == 3:
        chance_level = 0.5
        y_ticks = [0, 0.5, 1]
    elif n_good == 4:
        chance_level = 0.33
        y_ticks = [0, 0.33, 0.66, 1]
    else:
        raise NotImplementedError

    x_ticks = np.zeros(4, dtype=int)
    x_ticks[:] = np.linspace(0, len(mean), 4)

    ax.set_xticks(x_ticks)
    ax.set_yticks(y_ticks)

    ax.set_xlim((0, len(mean)))

    # For horizontal line
    ax.axhline(chance_level, linestyle='--', color='0.3',
               zorder=-10, linewidth=0.5)

    ax.set_title(f'{n_good} - {cond} - type{agent_type}')


def plot(fig_data, ylabel='ind. ex. frequency with good 0',
         f_name=None,
         use_std=False):

    n_good_cond = fig_data.keys()

    for n_good in n_good_cond:

        n_rows = n_good - 2

        fig = plt.figure(figsize=(10, 4 * n_rows))
        gs = grd.GridSpec(ncols=2, nrows=n_rows)

        cond_labels = sorted(fig_data[n_good].keys())

        for col, cond in enumerate(cond_labels[::-1]):

            agent_types = sorted(fig_data[n_good][cond].keys())

            for row, at in enumerate(agent_types):
                ax = fig.add_subplot(gs[row, col])

                exchange_type = fig_data[n_good][cond][at].get('exchange_type')

                if exchange_type is not None:
                    for ex_t in exchange_type:
                        x = fig_data[n_good][cond][at]['mean'][ex_t]

                        if use_std:
                            dsp = fig_data[n_good][cond][at]['std'][ex_t]
                        else:
                            dsp = fig_data[n_good][cond][at]['sem'][ex_t]

                        curve(x, dsp,
                              n_good=n_good, cond=cond, agent_type=at,
                              ax=ax, ylabel=ylabel, legend=str(ex_t))
                        ax.legend()

                else:
                    x = fig_data[n_good][cond][at]['mean']
                    if use_std:
                        dsp = fig_data[n_good][cond][at]['std']
                    else:
                        dsp = fig_data[n_good][cond][at]['sem']

                    curve(x,
                          dsp,
                          n_good=n_good, cond=cond, agent_type=at,
                          ax=ax, ylabel=ylabel)

        plt.tight_layout()

        if f_name is None:
            to_save = f"fig/learning_curves_{n_good}.pdf"
        else:

            to_save = f_name.format(n_good)

        plt.savefig(to_save)
        print(f'{to_save} has been produced')
