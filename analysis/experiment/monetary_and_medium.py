import numpy as np
import os

from game.models import Room, User, Choice
from analysis.tools import economy
from analysis.tools.conversion import Converter

import backup.backup as backup

"""
Medium matrices: n_good, agent, time
Monetary behavior matrices: n_good, agent, time  
"""


def run(file_name='data/exp.p'):

    if os.path.exists(file_name):
        return backup.load(file_name)

    rooms = Room.objects.all().order_by('id')

    data = {}

    for r in rooms:

        n_good = r.n_type
        print(r.id)

        monetary_behavior = np.zeros((n_good, r.n_user, r.t_max))
        medium = np.ones((n_good, r.n_user, r.t_max)) * -1

        ordered_goods = [n_good-1, ] + list(range(n_good-1))

        group_users = [
            User.objects.filter(
                room_id=r.id, production_good=Converter.reverse_value(g, n_good)).order_by('id')
            for g in ordered_goods
        ]

        for m in range(n_good):

            for t in range(r.t_max):

                i = 0
                for users in group_users:

                    for u in users:

                        choices = Choice.objects.filter(room_id=r.id, t=t, user_id=u.id)

                        for c in choices:

                            desired = Converter.convert_value(c.desired_good, n_good=n_good)
                            in_hand = Converter.convert_value(c.good_in_hand, n_good=n_good)

                            prod = Converter.convert_value(
                                u.production_good,
                                n_good=n_good)

                            cons = Converter.convert_value(
                                u.consumption_good,
                                n_good=n_good)

                            if m in (prod, cons):
                                monetary_conform = (in_hand, desired) == (prod, cons)
                                medium[m, i, t] = - 1

                            else:
                                monetary_conform = (in_hand, desired) in [(prod, m), (m, cons)]
                                medium[m, i, t] = monetary_conform

                            monetary_behavior[m, i, t] = monetary_conform

                        i += 1

        distribution = economy.distributions.get(r.id)

        label = economy.labels.get(r.id)
        data[label] = {
            'monetary_bhv': monetary_behavior,
            'medium': medium,
            'distribution': distribution
        }

    backup.save(data, file_name=file_name)

    return data
