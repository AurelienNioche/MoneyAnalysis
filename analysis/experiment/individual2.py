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
N_STATIC_VAR = 3
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

        static_data[i, GENDER_IDX] = 0 if u.gender == 'male' else 1
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

        for t in range(t_max):

            choices = Choice.objects.filter(room_id=r.id, t=t, user_id=u.id)

            for c in choices:

                desired = Converter.convert_value(c.desired_good, n_good=n_good)
                in_hand = Converter.convert_value(c.good_in_hand, n_good=n_good)

                prod = static_data[i, PROD_IDX]
                cons = static_data[i, CONS_IDX]

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


def evolution_direct_split(static_data, dynamic_data, n_split, const):

    data = {}
    rooms = Room.objects.all().order_by('id')
    rooms_id = [r.id for r in rooms]

    for r_id in rooms_id:

        r = Room.objects.get(id=r_id)
        n_good = r.n_type

        data_room = []

        for g in range(n_good):

            cons_g_bool = static_data[:, CONS_IDX] == g
            belong_r_bool = static_data[:, ROOM_IDX] == r_id

            cons_belong_r_bool = cons_g_bool*belong_r_bool
            n = int(np.sum(cons_belong_r_bool))

            raw = dynamic_data[cons_belong_r_bool, :, const]
            tmax = len(dynamic_data[0, :])
            spl = tmax//n_split
            bnds = np.arange(tmax+1, step=spl)

            points = [[] for _ in range(n_split)]

            for i in range(n):
                for j, k in enumerate(bnds):
                    if k != bnds[-1]:
                        data_ind = np.mean(raw[i, k:bnds[j+1]])
                        points[j].append(data_ind)

            data_room.append(points)

        data[r_id] = data_room

    return data


def evolution_direct(static_data, dynamic_data, window_size=25):

    data = {}
    rooms = Room.objects.all().order_by('id')
    rooms_id = [r.id for r in rooms]
    for r_id in rooms_id:

        r = Room.objects.get(id=r_id)
        n_good = r.n_type

        data_room = []

        for g in range(n_good):

            cons_g_bool = static_data[:, CONS_IDX] == g
            belong_r_bool = static_data[:, ROOM_IDX] == r_id

            cons_belong_r_bool = cons_g_bool*belong_r_bool
            n = int(np.sum(cons_belong_r_bool))

            raw = dynamic_data[cons_belong_r_bool, :, -1]

            data_good = []

            for i in range(n):
                r_mean = running_mean(raw[i], N=window_size)
                data_ind = r_mean
                data_good.append(data_ind)

            data_room.append(data_good)

        data[r_id] = data_room

    return data


def fig_evo_scatter(data_evo, title):

    rooms_id = list(data_evo.keys())
    rooms_id.sort()

    colors = [f"C{i}" for i in range(4)]

    fig, ax = plt.subplots(ncols=4, nrows=4, figsize=(20, 20))
    fig.suptitle(title)

    for idx, r_id in enumerate(rooms_id):

        data_room = data_evo[r_id]

        n_good = len(data_room)
        n_split = len(data_room[0])
        n_sub = len(data_room[0][0])

        for g in range(n_good):

            for n in range(n_sub):

                sub = []

                for s in range(n_split):

                    data_sub = data_room[g][s][n]
                    sub.append(data_sub)

                    ax[idx, g].scatter([s], [data_sub], color=colors[g])

                assert len(sub) == n_split
                ax[idx, g].plot(range(n_split), sub, color=colors[g])
                ax[idx, g].set_xlim([-1, n_split+1])

    plt.show()


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


def main():

    static_data, dynamic_data = individual_data()

    for const in (D_IND_O, D_IND_1, D_IND_2, D_IND_3, D_DIRECT):
        data_evo = evolution_direct_split(static_data, dynamic_data, n_split=3, const=const)
        fig_evo_scatter(data_evo, title=const)


if __name__ == "__main__":

    main()
