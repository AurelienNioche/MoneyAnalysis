import matplotlib.pyplot as plt

import graph.boxplot


import os


FIG_FOLDER = "fig"
os.makedirs(FIG_FOLDER, exist_ok=True)


def plot(data_gender):

    fig = plt.figure()
    ax = fig.add_subplot()
    graph.boxplot.boxplot(data_gender, ax=ax, y_label="Freq. dir. ex.")
    plt.savefig("fig/supplementary_gender.pdf")
