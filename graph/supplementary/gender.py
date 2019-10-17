import string

import matplotlib.pyplot as plt
import matplotlib.gridspec as grd

import graph.boxplot
from graph.utils import save_fig


def plot(data_gender, obs_type, fig_name='gender.pdf', fig_folder="sup"):

    assert obs_type in ('dir', 'ind0'), "Observation type not recognized"

    if obs_type == 'dir':
        y_label = 'Freq. direct ex.'
    else:
        y_label = 'Freq. ind. ex. with good 1'

    fig = plt.figure(figsize=(6, 4))
    gs = grd.GridSpec(nrows=1, ncols=2)

    for i, n_good in enumerate(sorted(list(data_gender.keys()))):

        if n_good == 3:
            chance_level = 0.5
            y_ticks = (0, 0.5, 1.0)
        elif n_good == 4:
            chance_level = 0.33
            y_ticks = (0, 0.33, 0.66, 1.00)
        else:
            raise NotImplementedError

        ax = fig.add_subplot(gs[0, i])
        graph.boxplot.boxplot(data_gender[n_good],
                              chance_level=chance_level,
                              y_ticks=y_ticks,
                              ax=ax,
                              y_label=y_label, color='C0',
                              title=f'{n_good} goods')

        # Add letter
        ax.text(-0.3, 1.1, string.ascii_uppercase[i],
                transform=ax.transAxes,
                size=20, weight='bold')

    plt.tight_layout()

    save_fig(fig_folder=fig_folder, fig_name=fig_name)
