from matplotlib import pyplot as plt

from analysis.experiment.individual import FIG_FOLDER


def fig_evo(data_evo):

    rooms_id = list(data_evo.keys())
    rooms_id.sort()

    colors = [f"C{i}" for i in range(4)]

    fig, ax = plt.subplots(ncols=1, nrows=4, figsize=(6, 20))

    for idx, r_id in enumerate(rooms_id):

        data_room = data_evo[r_id]

        n_good = len(data_room)

        for g in range(n_good):

            data_good = data_room[g]

            n = len(data_good)
            for i in range(n):
                ax[idx].plot(data_good[i], color=colors[g], alpha=0.5)

    plt.show()


def fig_evo_scatter(data_evo, title, f_name=None):

    rooms_id = list(data_evo.keys())
    rooms_id.sort()

    rooms_id = [416, 414, 415, 417]

    colors = [f"C{i}" for i in range(4)]

    fig, ax = plt.subplots(ncols=4, nrows=4, figsize=(20, 20))

    ax[0, 0].set_title(title)
    print(f'Doing {title}')

    for idx, r_id in enumerate(rooms_id):

        data_room = data_evo[r_id]

        n_good = len(data_room)
        n_split = len(data_room[0])

        for g in range(n_good):

            n_sub = len(data_room[g][0])
            print(f'Room={r_id}, ngood={n_good}, good={g}, nsub={n_sub}')

            for n in range(n_sub):

                sub = []

                for s in range(n_split):

                    data_sub = data_room[g][s][n]
                    sub.append(data_sub)

                    ax[idx, g].scatter([s], [data_sub], color=colors[g], alpha=0.5)

                assert len(sub) == n_split
                ax[idx, g].plot(range(n_split), sub, color=colors[g], alpha=0.5)
                ax[idx, g].set_xlim([-0.15, n_split-0.85])
                ax[idx, g].set_ylim([-.02, 1.02])
                ax[idx, g].set_xticks([])
                ax[idx, g].set_yticks([0, 0.25, 0.5, 0.75, 1.])

    plt.tight_layout()

    if f_name:
        plt.show()
        plt.savefig(f"{FIG_FOLDER}/{f_name}")
    else:
        plt.show()
