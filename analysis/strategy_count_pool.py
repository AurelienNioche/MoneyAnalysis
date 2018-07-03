import numpy as np
from scipy import stats

from analysis.tools.conversion import Converter
from analysis.tools import economy_labels
from game.models import Room, User, Choice
import scipy.stats

from graph.tools.bar import bar
import matplotlib.pyplot as plt
import matplotlib.gridspec as grd
import itertools as it

def run():

    output_data = {}

    print("******** Analysis of strategy *************")

    rooms = Room.objects.all().order_by('id')

    for r in rooms:

        print("\n", "*" * 5, f"Room {r.id}", "*" * 5)

        n_good = r.n_type

        data_room_mean = np.zeros(n_good)
        data_room_std = np.zeros(n_good)

        for g in range(n_good):

            g_reversed = Converter.reverse_value(g, n_good=n_good)

            users = User.objects.filter(room_id=r.id)\
                .exclude(production_good=g_reversed)\
                .exclude(consumption_good=g_reversed)

            n_users = len(users)

            data_good_mean = np.zeros(n_users)
            # data_good_std = np.zeros(n_users)

            for i, u in enumerate(users):

                prod = Converter.convert_value(u.production_good, n_good=n_good)
                cons = Converter.convert_value(u.consumption_good, n_good=n_good)

                data_user = np.zeros(r.t_max, dtype=int)

                for t in range(r.t_max):

                    choice = Choice.objects.get(room_id=r.id, user_id=u.id, t=t)

                    in_hand = Converter.convert_value(choice.good_in_hand, n_good=n_good)
                    desired = Converter.convert_value(choice.desired_good, n_good=n_good)

                    v = 0

                    if in_hand == prod:
                        if desired != cons and desired == g:
                            v = 1

                    else:
                        if desired == cons and in_hand == g:
                            v = 1

                    data_user[t] = v

                data_good_mean[i] = np.mean(data_user)
                # data_good_std[i] = scipy.stats.sem(data_user)

            data_room_mean[g] = np.mean(data_good_mean)
            data_room_std[g] = scipy.stats.sem(data_good_mean)

        output_data[economy_labels.get(r.id)] = {
            'mean': data_room_mean,
            'std': data_room_std
        }

    # ----------------- #

    data_keys = \
        "3_good_non_uniform", \
        "3_good_uniform", \
        "4_good_non_uniform", \
        "4_good_uniform"

    fig = plt.figure(figsize=(15, 15))
    gs = grd.GridSpec(nrows=2, ncols=2, width_ratios=[1, 1], height_ratios=[3, 4])

    coord = it.product(range(2), repeat=2)

    for i, k in enumerate(data_keys):
        c = next(coord)

        bar(
            means=output_data[k]['mean'], errors=output_data[k]['std'], subplot_spec=gs[c[0], c[1]], fig=fig,
            labels=[str(i) for i in range(len(output_data[k]['mean']))], title=k,
            color="C7"
        )

    plt.show()

    # ------------- #

    return output_data
