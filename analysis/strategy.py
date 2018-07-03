import numpy as np
from scipy import stats

from analysis.tools.conversion import Converter
from analysis.tools import economy_labels
from game.models import Room, User, Choice


def run(m=0, order_by_m=True):

    output_data = {}

    # -------------------------------- #

    print("******** Analysis of strategy *************")

    rooms = Room.objects.all().order_by('id')

    for r in rooms:

        print("Room ", r.id)

        n_good = r.n_type

        good_list = [n_good - 1, ] + list(range(n_good - 1))

        room_data = []

        for prod in good_list:

            users = User.objects.filter(
                room_id=r.id, production_good=Converter.reverse_value(prod, n_good=n_good))

            data_one_type = np.zeros((len(users), r.t_max), dtype=int)

            for t in range(r.t_max):

                for i, u in enumerate(users):

                    choice = Choice.objects.get(room_id=r.id, user_id=u.id, t=t)

                    in_hand = Converter.convert_value(choice.good_in_hand, n_good=n_good)
                    desired = Converter.convert_value(choice.desired_good, n_good=n_good)

                    prod = Converter.convert_value(u.production_good, n_good=n_good)
                    cons = Converter.convert_value(u.consumption_good, n_good=n_good)

                    if in_hand == prod:
                        if desired != cons:
                            if desired == m:
                                v = 1
                            else:
                                v = 0
                        else:
                            v = -1

                    else:
                        if desired == cons and in_hand == m:
                            v = 1
                        else:
                            v = 0

                    data_one_type[i, t] = v

            direct_count = np.zeros(len(users))
            if order_by_m:
                cond = 1
            else:
                cond = -1
            direct_count[:] = [np.sum(data_one_type[i, :] == cond) for i in range(len(users))]
            order = np.argsort(direct_count)[::-1]

            room_data.append(data_one_type[order, :])

        label = economy_labels.get(r.id) + '_strategy'
        output_data[label] = room_data

    return output_data
