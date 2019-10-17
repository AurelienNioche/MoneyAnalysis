import string

import matplotlib.pyplot as plt
import numpy as np

# import matplotlib.gridspec as grd

# from graph.labelling import agent_labeling
from graph.utils import save_fig


def boxplot(
        results, ax=None, chance_level=None,
        y_ticks=None,
        colors=None, color=None, tick_labels=None,
        y_label=None,
        y_lim=(-0.02, 1.02),
        fontsize=10, aspect=3, title=None,
        n_subplot=None,
        fig_name=None,
        fig_folder=None
):

    sorted_keys = sorted(results.keys())

    if not ax:
        fig, ax = plt.subplots(figsize=(20, 5))

    if tick_labels is None:
        tick_labels = sorted_keys

    if colors is None:
        if color is None:
            color = 'black'
        colors = [color for _ in range(len(sorted_keys))]

    if title:
        ax.set_title(title, fontsize=fontsize)

    if n_subplot is not None:
        # Add letter
        ax.text(-0.2, 1.2, string.ascii_uppercase[n_subplot],
                transform=ax.transAxes,
                size=20, weight='bold')

    n = len(sorted_keys)

    # For boxplot
    positions = list(range(n))
    values_box_plot = [[] for _ in range(n)]

    # For scatter
    x_scatter = []
    y_scatter = []
    colors_scatter = []

    for i, cond in enumerate(sorted_keys):

        for v in results[cond]:

            # For boxplot
            values_box_plot[i].append(v)

            # For scatter
            x_scatter.append(i)
            y_scatter.append(v)
            colors_scatter.append(colors[i])

    # For scatter
    ax.scatter(x_scatter+np.random.random(size=len(x_scatter)) * 0.05 *
               np.random.choice([-1, 1], size=len(x_scatter)),
               y_scatter, c=colors_scatter, s=30, alpha=0.5,
               linewidth=0.0, zorder=1)

    if chance_level:
        # For horizontal line
        ax.axhline(chance_level, linestyle='--', color='0.3', zorder=-10,
                   linewidth=0.5)

    try:
        if y_ticks is not None:
            ax.set_yticks(y_ticks)
    except ValueError:
        ax.set_yticks(y_ticks)

    ax.set_ylim(y_lim)

    # For boxplot
    bp = ax.boxplot(values_box_plot, positions=positions,
                    labels=tick_labels, showfliers=False, zorder=2)

    # Warning: only one box, but several whiskers by plot
    for e in ['boxes', 'caps', 'whiskers', 'medians']:
        for b in bp[e]:
            b.set(color='black')
            # b.set_alpha(1)

    ax.tick_params(axis='both', labelsize=fontsize)
    ax.set_ylabel(y_label, fontsize=fontsize)

    if aspect:
        ax.set_aspect(aspect)

    save_fig(fig_folder=fig_folder, fig_name=fig_name)


# def plot(fig_data, fig_folder, name_extension=''):
#
#     post_hoc = 'fit' in name_extension
#
#     n_good_cond = sorted(list(fig_data.keys()))
#
#     category = sorted(fig_data[n_good_cond[0]].keys())
#     if not post_hoc:
#         # Simulation would on the left column
#         category = category[::-1]
#
#     for n_good in n_good_cond:
#
#         n_rows = n_good-2
#
#         fig = plt.figure(figsize=(7, 4*n_rows))
#         gs = grd.GridSpec(ncols=len(category), nrows=n_rows)
#
#         n = 0
#
#         for col, cat in enumerate(category):
#
#             agent_type = sorted(fig_data[n_good][cat].keys())
#             for row, at in enumerate(agent_type):
#
#                 ax = fig.add_subplot(gs[row, col])
#
#                 al = agent_labeling(n_good)
#                 at_label = al[at]
#
#                 results = fig_data[n_good][cat][at]
#
#                 if post_hoc and cat == 'Simulation':
#                     cat_label = 'Post hoc simulation'
#                 else:
#                     cat_label = cat
#
#                 title = f'{cat_label} - Type {at_label}'
#
#                 chance_level = 1/(n_good-1)
#                 y_ticks = np.linspace(0, 1, n_good)
#
#                 # if n_good == 3:
#                 #     chance_level = 0.5
#                 #     y_ticks = [0, 0.5, 1]
#                 # elif n_good == 4:
#                 #     chance_level = 0.33
#                 #     y_ticks = [0, 0.33, 0.66, 1]
#                 # else:
#                 #     raise NotImplementedError
#
#                 boxplot(results=results,
#                         chance_level=chance_level,
#                         y_ticks=y_ticks,
#                         ax=ax,
#                         title=title,
#                         y_label='Freq. ind. ex. with good 1',
#                         colors=('C0', 'C1'),
#                         n_subplot=n)
#
#                 n += 1
#
#         plt.tight_layout()
#
#         fig_name = f'xp_{n_good}{name_extension}.pdf'
#         save_fig(fig_folder=fig_folder, fig_name=fig_name)
