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

N_DEMOGRAPHIC_VAR = 2
N_STATIC_VAR = 3
N_DYNAMIC_VAR = 1

GENDER_IDX = 0
AGE_IDX = 1

ROOM_IDX = 2
PROD_IDX = 3
CONS_IDX = 4


def individual_data():

    # Static data
    users = User.objects.all().order_by('id')
    n = len(users)

    static_data = np.zeros((n, N_DEMOGRAPHIC_VAR + N_STATIC_VAR))

    for i, u in enumerate(users):

        n_good = Room.objects.get(id=u.room_id).n_type

        static_data[i, CONS_IDX] = Converter.convert_value(u.consumption_good, n_good=n_good)
        static_data[i, PROD_IDX] = Converter.convert_value(u.production_good, n_good=n_good)

        static_data[i, GENDER_IDX] = 0 if u.gender == 'male' else 1
        static_data[i, AGE_IDX] = u.age

    # Dynamic data
    user_id = [u.id for u in users]

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
                        dynamic_data[i, -1] = direct
                    else:
                        indirect_with_g = (in_hand, desired) in [(prod, g), (g, cons)]
                        dynamic_data[i, g] = indirect_with_g









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


if __name__ == "__main__":

    individual_data()
