import matplotlib.pyplot as plt

import graph.sim_and_xp


import os


FIG_FOLDER = "fig"
os.makedirs(FIG_FOLDER, exist_ok=True)


def plot(data_gender):

    for n_good in data_gender.keys():

        fig = plt.figure()
        ax = fig.add_subplot()
        graph.sim_and_xp.boxplot(data_gender[n_good], n_good=n_good, ax=ax, y_label="Freq. dir. ex.")
        plt.savefig(f"fig/supplementary_gender_{n_good}.pdf")
