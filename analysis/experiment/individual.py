# MoneyAnalysis
# Copyright (C) 2018  Aurélien Nioche, Basile Garcia & Nicolas Rougier
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
# Django specific settings
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MoneyAnalysis.settings")

# Ensure settings are read
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()


from game.models import User, Room, Choice


from analysis.tools.conversion import Converter

import numpy as np
import matplotlib.pyplot as plt

import pickle

SCRIPT_FOLDER = os.path.dirname(os.path.abspath(__file__))
DATA_FOLDER = f"{SCRIPT_FOLDER}/../../data"
INDIVIDUAL_DATA = f"{DATA_FOLDER}/individual_data.p"

N_DEMOGRAPHIC_VAR = 2
N_STATIC_VAR = 11
N_DYNAMIC_VAR = 5

# Demographic variables
GENDER_IDX = 0
AGE_IDX = 1

# Static variables
ROOM_IDX = 2
PROD_IDX = 3
CONS_IDX = 4
S_IND_0 = 5
S_IND_1 = 6
S_IND_2 = 7
S_IND_3 = 8
S_DIRECT = 9

# Dynamic variables
D_IND_O = 0
D_IND_1 = 1
D_IND_2 = 2
D_IND_3 = 3
D_DIRECT = 4


def running_mean(x, N):
    return np.convolve(x, np.ones(N) / N, mode='valid')

# def running_mean(l, N):
#     sum = 0
#     result = list(0 for x in l)
#
#     for i in range(0, N):
#         sum = sum + l[i]
#         result[i] = sum / (i + 1)
#
#     for i in range(N, len(l)):
#         sum = sum - l[i - N] + l[i]
#         result[i] = sum / N
#
#     return result


def load_individual_data_from_db():
    # Static data
    users = User.objects.all().order_by('id')
    n = len(users)

    static_data = np.zeros((n, N_DEMOGRAPHIC_VAR + N_STATIC_VAR))

    for i, u in enumerate(users):
        n_good = Room.objects.get(id=u.room_id).n_type

        static_data[i, ROOM_IDX] = u.room_id

        static_data[i, CONS_IDX] = Converter.convert_value(u.consumption_good, n_good=n_good)
        static_data[i, PROD_IDX] = Converter.convert_value(u.production_good, n_good=n_good)

        static_data[i, GENDER_IDX] = u.gender == 'female'
        static_data[i, AGE_IDX] = u.age

    # Dynamic data
    # user_id = [u.id for u in users]

    rooms = Room.objects.all().order_by('id')

    # Assume the t_max is similar for every room
    assert len(np.unique([r.t_max for r in rooms]) == 1)
    t_max = rooms[0].t_max

    dynamic_data = np.zeros((n, t_max, N_DYNAMIC_VAR))

    for i, u in enumerate(users):

        r = Room.objects.get(id=u.room_id)
        n_good = r.n_type

        prod = static_data[i, PROD_IDX]
        cons = static_data[i, CONS_IDX]

        for t in range(t_max):

            choices = Choice.objects.filter(room_id=r.id, t=t, user_id=u.id)

            for c in choices:

                desired = Converter.convert_value(c.desired_good, n_good=n_good)
                in_hand = Converter.convert_value(c.good_in_hand, n_good=n_good)

                for g in range(n_good):

                    if g in (prod, cons):
                        direct = (in_hand, desired) == (prod, cons)
                        dynamic_data[i, t, -1] = direct
                    else:
                        indirect_with_g = (in_hand, desired) in [(prod, g), (g, cons)]
                        dynamic_data[i, t, g] = indirect_with_g

    return static_data, dynamic_data


def individual_data():

    if os.path.exists(INDIVIDUAL_DATA):
        static_data, dynamic_data = pickle.load(open(INDIVIDUAL_DATA, 'rb'))

    else:
        static_data, dynamic_data = load_individual_data_from_db()
        pickle.dump(obj=(static_data, dynamic_data), file=open(INDIVIDUAL_DATA, 'wb'))

    return static_data, dynamic_data


def evolution_direct(static_data, dynamic_data, window_size=15):

    data = {}
    # print(static_data[:, CONS_IDX])
    rooms = Room.objects.all().order_by('id')
    rooms_id = [r.id for r in rooms]
    for r_id in rooms_id:

        r = Room.objects.get(id=r_id)
        n_good = r.n_type
        # t_max = r.t_max
        # n = r.counter

        # ns = [int(i) for i in r.types.split("/")]
        # print(ns)

        data_room = []

        for g in range(n_good):

            cons_g_bool = static_data[:, CONS_IDX] == g
            belong_r_bool = static_data[:, ROOM_IDX] == r_id

            cons_belong_r_bool = cons_g_bool*belong_r_bool
            n = int(np.sum(cons_belong_r_bool))

            raw = dynamic_data[cons_belong_r_bool, :, D_DIRECT]

            data_good = []

            for i in range(n):
                # print(raw[i].shape)
                # print(len(raw[i]))
                r_mean = running_mean(raw[i], N=window_size)
                # print(len(r_mean))
                data_ind = r_mean
            # for i in range(ns[g]):
            #     pass
                data_good.append(data_ind)

            data_room.append(data_good)

        data[r_id] = data_room

    return data


def fig_evo(data_evo):

    rooms_id = list(data_evo.keys())
    rooms_id.sort()

    colors = [f"C{i}" for i in range(4)]

    fig, ax = plt.subplots(ncols=1, nrows=4, figsize=(6, 20))

    for idx, r_id in enumerate(rooms_id):

        # print(data)
        data_room = data_evo[r_id]

        n_good = len(data_room)

        for g in range(n_good):

            data_good = data_room[g]

            n = len(data_good)
            for i in range(n):
                ax[idx].plot(data_good[i], color=colors[g], alpha=0.5)

    plt.show()

    # for r in rooms:
    #
    #     n_good = r.n_type
    #     print(r.id)
    #
    #     monetary_behavior = np.zeros((n_good, r.n_user, r.t_max))
    #     medium = np.ones((n_good, r.n_user, r.t_max)) * -1
    #
    #     ordered_goods = [n_good - 1, ] + list(range(n_good - 1))
    #
    #     group_users = [
    #         User.objects.filter(
    #             room_id=r.id, production_good=Converter.reverse_value(g, n_good)).order_by('id')
    #         for g in ordered_goods
    #     ]
    #
    #     for m in range(n_good):
    #
    #         for t in range(r.t_max):
    #
    #             i = 0
    #             for users in group_users:
    #
    #                 for u in users:
    #
    #                     choices = Choice.objects.filter(room_id=r.id, t=t, user_id=u.id)
    #
    #                     for c in choices:
    #
    #                         desired = Converter.convert_value(c.desired_good, n_good=n_good)
    #                         in_hand = Converter.convert_value(c.good_in_hand, n_good=n_good)
    #
    #                         prod = Converter.convert_value(
    #                             u.production_good,
    #                             n_good=n_good)
    #
    #                         cons = Converter.convert_value(
    #                             u.consumption_good,
    #                             n_good=n_good)
    #
    #                         if m in (prod, cons):
    #                             monetary_conform = (in_hand, desired) == (prod, cons)
    #                             medium[m, i, t] = - 1
    #
    #                         else:
    #                             monetary_conform = (in_hand, desired) in [(prod, m), (m, cons)]
    #                             medium[m, i, t] = monetary_conform
    #
    #                         monetary_behavior[m, i, t] = monetary_conform
    #
    #                     i += 1


def main():

    static_data, dynamic_data = individual_data()
    data_evo = evolution_direct(static_data, dynamic_data)
    fig_evo(data_evo)


if __name__ == "__main__":

    main()
