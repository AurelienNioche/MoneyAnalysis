import matplotlib.pyplot as plt

import os


FIG_FOLDER = "fig"
os.makedirs(FIG_FOLDER, exist_ok=True)


def plot(data):

    fig, axes = plt.subplots(nrows=len(data.keys()))

    i = 0
    for title, (values, r_values) in sorted(data.items()):
        ax = axes[i]
        ax.scatter(values, r_values, alpha=0.5)
        ax.set_title(title)
        i += 1

    plt.tight_layout()
    f_name = "parameter_recovery.pdf"
    fig_path = os.path.join(FIG_FOLDER, f_name)
    plt.savefig(fig_path)
    print(f"Figure '{fig_path}' created.\n")
