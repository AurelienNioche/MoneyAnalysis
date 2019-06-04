import matplotlib.pyplot as plt

import graph.sim_and_xp


import os


FIG_FOLDER = "fig"
os.makedirs(FIG_FOLDER, exist_ok=True)


def plot(data):

    fig = plt.figure()
    ax = fig.add_subplot()
    graph.sim_and_xp.boxplot(data, n_good=3, ax=ax, y_label="Freq. ind. ex.")
    plt.savefig(f"fig/supplementary_cross_validation.pdf")
