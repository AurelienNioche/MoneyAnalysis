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

# from analysis.experiment.evolution import evolution_direct
# from analysis.experiment.graph import fig_evo

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MoneyAnalysis.settings")

# Ensure settings are read
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()


from game.models import User, Room, Choice

import enum

import numpy as np
import pickle

from analysis.tools.conversion import Converter
from analysis.experiment.metric import exchange, monetary


SCRIPT_FOLDER = os.path.dirname(os.path.abspath(__file__))
ROOT_FOLDER = f"{SCRIPT_FOLDER}/../../"

DATA_FOLDER = f"{ROOT_FOLDER}/data"
FIG_FOLDER = f"{ROOT_FOLDER}/fig"

INDIVIDUAL_DATA = f"{DATA_FOLDER}/individual_data.p"

N_STATIC_VAR = 11
N_DYNAMIC_VAR = 6


class Dyn:

    IND_0 = 0  # Cumulative number of indirect exchange with good 0
    IND_1 = 1
    IND_2 = 2
    IND_3 = 3
    DIRECT = 4  # Cumulative number of direct exchange with production good in hand
    NP = 5  # Cumulative number of timesteps with production good in hand
    MONEY_0 = 6
    MONEY_1 = 7
    MONEY_2 = 8
    MONEY_3 = 9


class Stc:
    GENDER = 0
    AGE = 1
    ROOM = 2
    PROD = 3
    CONS = 4
    IND_0 = 5
    IND_1 = 6
    IND_2 = 7
    IND_3 = 8
    DIRECT = 9


def load_individual_data_from_db():

    # Static data
    users = User.objects.all().order_by('id')
    n = len(users)

    static_data = np.zeros((n, N_STATIC_VAR))

    for i, u in enumerate(users):
        n_good = Room.objects.get(id=u.room_id).n_type

        static_data[i, Stc.ROOM] = u.room_id

        static_data[i, Stc.CONS] = Converter.convert_value(u.consumption_good, n_good=n_good)
        static_data[i, Stc.PROD] = Converter.convert_value(u.production_good, n_good=n_good)

        static_data[i, Stc.GENDER] = u.gender == 'female'
        static_data[i, Stc.AGE] = u.age

    rooms = Room.objects.all().order_by('id')

    # Assume the t_max is similar for every room
    assert len(np.unique([r.t_max for r in rooms]) == 1)
    t_max = rooms[0].t_max

    dynamic_data = np.zeros((n, t_max, N_DYNAMIC_VAR))

    for i, u in enumerate(users):

        r = Room.objects.get(id=u.room_id)
        n_good = r.n_type

        prod = static_data[i, Stc.PROD]
        cons = static_data[i, Stc.CONS]

        in_hand = np.zeros(t_max, dtype=int)
        desired = np.zeros(t_max, dtype=int)

        # Preprocess the data
        for t in range(t_max):

            c = Choice.objects.get(room_id=r.id, t=t, user_id=u.id)

            in_hand[t] = Converter.convert_value(c.good_in_hand, n_good=n_good)
            desired[t] = Converter.convert_value(c.desired_good, n_good=n_good)

        # Analysis
        dir_ex, ind_ex, n_p = exchange(n_good=n_good, in_hand=in_hand, desired=desired, prod=prod, cons=cons)
        dynamic_data[i, :, :n_good] = ind_ex
        dynamic_data[i, :, Dyn.DIRECT] = dir_ex
        dynamic_data[i, :, Dyn.NP] = n_p

        m_bh, n_p = \
            monetary(n_good=n_good, in_hand=in_hand, desired=desired, prod=prod, cons=cons)
        dynamic_data[i, :, Dyn.MONEY_0: Dyn.MONEY_0+n_good] = m_bh

        #     for g in range(n_good):
        #
        #         if g in (prod, cons):
        #             direct = (in_hand, desired) == (prod, cons)
        #             dynamic_data[i, t, -1] = direct
        #         else:
        #             indirect_with_g = (in_hand, desired) in [(prod, g), (g, cons)]
        #             dynamic_data[i, t, g] = indirect_with_g
        #
        # for g in range(n_good):
        #     static_data[i, globals()[f"S_IND_{g}"]] = np.mean(dynamic_data[i, :, globals()[f"D_IND_{g}"]])

    return static_data, dynamic_data


def individual_data(force=False):

    if not os.path.exists(INDIVIDUAL_DATA) or force:
        static_data, dynamic_data = load_individual_data_from_db()
        pickle.dump(obj=(static_data, dynamic_data), file=open(INDIVIDUAL_DATA, 'wb'))

    else:
        static_data, dynamic_data = pickle.load(open(INDIVIDUAL_DATA, 'rb'))

    return static_data, dynamic_data


# def main():
#
#     static_data, dynamic_data = individual_data()
#     data_evo = evolution_direct(static_data, dynamic_data)
#     fig_evo(data_evo)
#
#
# if __name__ == "__main__":
#
#     main()


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
