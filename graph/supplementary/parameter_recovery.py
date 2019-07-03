import os
import string

import matplotlib.pyplot as plt
import numpy as np

from graph.parameters import SUP_FIG_FOLDER


def _subplot(ax, title, values, r_values, n_subplot=None):

    # Add letter
    ax.text(-0.1, 1.01, string.ascii_uppercase[n_subplot],
            transform=ax.transAxes,
            size=20, weight='bold')

    ax.scatter(values, r_values, alpha=0.5)
    ax.set_title(title)

    min_value = min(min(values), min(r_values))
    max_value = max(max(values), max(r_values))

    a = np.linspace(min_value, max_value, 10)

    ax.plot(a, a, linestyle='--', alpha=0.5, zorder=-1, color='black')

    ax.set_xlim(min_value, max_value)
    ax.set_ylim(min_value, max_value)

    ax.set_xlabel('Fitted')
    ax.set_ylabel('Recovered')

    ax.set_aspect(1)


def plot(data):

    fig, axes = plt.subplots(ncols=len(data.keys()),
                             figsize=(15, 5))

    i = 0
    for title, (values, r_values) in sorted(data.items()):

        ax = axes[i]
        _subplot(ax=ax, title=title,
                 values=values, r_values=r_values, n_subplot=i)
        i += 1

    plt.tight_layout()
    f_name = "parameter_recovery.pdf"
    fig_path = os.path.join(SUP_FIG_FOLDER, f_name)
    plt.savefig(fig_path)
    print(f"Figure '{fig_path}' created.\n")
