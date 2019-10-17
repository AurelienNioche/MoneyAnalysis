import matplotlib.pyplot as plt

import graph.boxplot


import os


FIG_FOLDER = "fig"
os.makedirs(FIG_FOLDER, exist_ok=True)


def plot(data):

    fig = plt.figure()
    ax = fig.add_subplot()
    graph.boxplot.boxplot(data, n_good=3, ax=ax, y_label="Freq. ind. ex.")
    f_name = f"fig/supplementary_cross_validation.pdf"
    plt.savefig(f_name)
    print(f'Figure {f_name} has been produced.')
