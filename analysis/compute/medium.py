from game.models import Room, User, Choice

import numpy as np

from analysis.tools.conversion import Converter
from analysis.tools import economy


def run():

    output_data = {}

    # -------------------------------- #

    print("******** Analysis of medium *************")

    rooms = Room.objects.all().order_by('id')

    for r in rooms:

        print("Room ", r.id)

        n_good = r.n_type

        users = User.objects.filter(room_id=r.id)

        room_data = np.zeros((n_good, r.t_max), dtype=int)

        for t in range(r.t_max):

            for u in users:

                choice = Choice.objects.get(room_id=r.id, user_id=u.id, t=t)

                in_hand = Converter.convert_value(choice.good_in_hand, n_good=n_good)
                desired = Converter.convert_value(choice.desired_good, n_good=n_good)

                prod = Converter.convert_value(u.production_good, n_good=n_good)
                cons = Converter.convert_value(u.consumption_good, n_good=n_good)

                if in_hand == prod:
                    if desired != cons:
                        room_data[desired, t] += 1

                else:
                    if desired == cons:
                        room_data[in_hand, t] += 1

        label = economy.labels.get(r.id) + '_medium'
        output_data[label] = room_data / (len(users) / n_good)

    return output_data
