import matplotlib.pyplot as plt
import matplotlib.gridspec

import os


FIG_FOLDER = "fig"
os.makedirs(FIG_FOLDER, exist_ok=True)


def plot(age, y):

    fig = plt.figure(figsize=(5, 8), dpi=200)

    gs = matplotlib.gridspec.GridSpec(nrows=1, ncols=1)
    ax = fig.add_subplot(gs[0, 0])

    ax.scatter(
        age,
        y,
        facecolor="black", edgecolor='white', s=15, alpha=0.5)

    ax.set_ylabel("Freq. dir. ex.")
    ax.set_ylim((-0.01, 1.01))
    ax.set_yticks((0, 0.5, 1.0))
    ax.set_xlabel('Age')
    ax.set_aspect(35)

    plt.tight_layout()
    plt.savefig('fig/supplementary_age.pdf')
