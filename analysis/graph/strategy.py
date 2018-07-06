import matplotlib.pyplot as plt
import matplotlib.gridspec as grd
from matplotlib.colors import LinearSegmentedColormap
import numpy as np
import itertools as it
import os

data_keys = \
    "3_good_non_uniform_strategy", \
    "3_good_uniform_strategy", \
    "4_good_non_uniform_strategy", \
    "4_good_uniform_strategy"


def plot(data, f_name=None, m_color='C1'):

    cm = LinearSegmentedColormap.from_list('', ['C7', 'white', m_color], N=3)

    fig = plt.figure(figsize=(15, 15))
    gs = grd.GridSpec(nrows=2, ncols=2, width_ratios=[1, 1], height_ratios=[3, 4])

    coord = it.product(range(2), repeat=2)

    for i, k in enumerate(data_keys):

        room_data = data[k]

        c = next(coord)

        sub_gs = grd.GridSpecFromSubplotSpec(subplot_spec=gs[c[0], c[1]], ncols=1, nrows=len(room_data),
                                             height_ratios=[len(d) for d in room_data])

        for j, d in enumerate(room_data):

            ax = fig.add_subplot(sub_gs[j, 0])
            ax.imshow(d, vmin=-1, vmax=1, cmap=cm)

            if not j + 1 == len(room_data):
                ax.set_xticks([])
            else:
                ax.set_xticks([])
                ax.set_xlabel("t")

            ax.set_yticks([])
    plt.tight_layout()

    if f_name is not None:
        os.makedirs(os.path.dirname(f_name), exist_ok=True)
        plt.savefig(f_name)

    plt.show()


def main():

    data = {}

    for i, k in enumerate(data_keys):

        data_room = []
        for j in range(int(k[0])):

            n_agents = np.random.choice((10, 20))

            data_type = np.random.choice((-1, 0, 1), (n_agents, 50))
            data_room.append(data_type)

        data[k] = data_room

    plot(data)


if __name__ == "__main__":

    main()
