import os
import string

import matplotlib.pyplot as plt
import matplotlib.gridspec as grd


from graph.parameters import SUP_FIG_FOLDER
import graph.sim_and_xp


def plot(data_gender, f_name='gender.pdf',
         y_label='Freq. direct ex.'):

    fig = plt.figure(figsize=(6, 4))
    gs = grd.GridSpec(nrows=1, ncols=2)

    for i, n_good in enumerate(sorted(list(data_gender.keys()))):

        ax = fig.add_subplot(gs[0, i])
        graph.sim_and_xp.boxplot(data_gender[n_good], n_good=n_good, ax=ax,
                                 y_label=y_label, color='C0',
                                 title=f'{n_good} goods')

        # Add letter
        ax.text(-0.3, 1.1, string.ascii_uppercase[i],
                transform=ax.transAxes,
                size=20, weight='bold')

    plt.tight_layout()

    fig_path = os.path.join(SUP_FIG_FOLDER, f_name)
    plt.savefig(fig_path)
    print(f"Figure '{fig_path}' created.\n")
