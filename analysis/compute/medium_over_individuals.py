import numpy as np
from scipy import stats

from analysis.tools.conversion import Converter
from analysis.tools import economy
from game.models import Room, User, Choice
from backup import backup

import scipy.stats
import os


"""
Medium matrices: n_good, agent
"""


def run(file_name='data/exp_strategy_count_pool.p'):

    if os.path.exists(file_name):
        return backup.load(file_name)

    output_data = {}

    print("******** Analysis of strategy *************")

    rooms = Room.objects.all().order_by('id')

    for r in rooms:

        print("\n", "*" * 5, f"Room {r.id}", "*" * 5)

        n_good = r.n_type

        data_room_mean = np.zeros(n_good)
        data_room_std = np.zeros(n_good)

        medium = np.ones((n_good, r.n_user)) * -1

        for g in range(n_good):

            g_reversed = Converter.reverse_value(g, n_good=n_good)

            users = User.objects.filter(room_id=r.id)\
                .exclude(production_good=g_reversed)\
                .exclude(consumption_good=g_reversed)

            n_users = len(users)

            data_good_mean = np.zeros(n_users)

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

                medium[g, i] = np.mean(data_user)

            data_room_mean[g] = np.mean(data_good_mean)

            data_room_std[g] = scipy.stats.sem(data_good_mean)

        label = economy.labels.get(r.id) #+ '_strategy_count_pool'
        output_data[label] = {
            'mean': data_room_mean,
            'std': data_room_std,
            'medium': medium
        }
        # print(medium)
    backup.save(output_data, file_name=file_name)

    return output_data
