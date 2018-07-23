import matplotlib.gridspec as grd
import itertools as it


def _sub_monetary_bhv_over_t(
        data, fig, subplot_spec,
        letter=None, title=None, ylabel=True,
        mean_plot=None, thick_linewidth=2, thin_linewidth=0.5,
        alpha=0.3):
    """
    :param data: either one (array n_good * t_max) data/ or a list [(array n_good * tmax), ...]
    :param fig:
    :param subplot_spec:
    :param letter:
    :param title:
    :param ylabel:
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

        if ylabel:
            ax.set_yticks([0, 1])
        else:
            ax.set_yticks([])

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

    if ylabel:
        ax0.text(
            s="Monetary behavior", x=-0.3, y=0.5, horizontalalignment='center', verticalalignment='center',
            transform=ax0.transAxes, fontsize=10, rotation='vertical')

    if letter:
        ax0.text(
            s=letter, x=-0.1, y=-0.1, horizontalalignment='center', verticalalignment='center',
            transform=ax0.transAxes,
            fontsize=20)

    if title is not None:
        ax0.set_title(title)


def monetary_bhv_over_t(data, mean_plot, n_side, fig, subplot_spec, exp):

    coord = it.product(range(n_side), range(n_side))
    gs = grd.GridSpecFromSubplotSpec(nrows=1, ncols=n_side, subplot_spec=subplot_spec)

    for i in range(n_side):

        _sub_monetary_bhv_over_t(
            # If the graph is generated from experiment data, each column (the good considered as money) is one 'i'.
            # If the graph is generated from simulation data, 'i' stills represents one column
            # (the good considered as money),
            # but there are multiple economies so multiple curves (each curves representing
            # one simulated economy and the mean plot is the mean computed from these economies)
            data=data[i] if exp else [j[i] for j in data],
            mean_plot=mean_plot[i] if mean_plot is not None else None,
            fig=fig, subplot_spec=gs[next(coord)],
            title=f'm={i+1}',
            ylabel=i == 0
        )


def medium_over_t(
        data, fig, subplot_spec, thick_linewidth=2, thin_linewidth=0.5, alpha=0.3,
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
