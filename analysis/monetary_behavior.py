import numpy as np
from scipy import stats

from analysis.tools.conversion import Converter
from analysis.tools import economy_labels
from game.models import Room, User, Choice


def run(m=0):

    output_data = {}

    # -------------- #

    print("******** Analysis of monetary behavior *************")

    rooms = Room.objects.all().order_by('id')

    for r in rooms:

        print("Room ", r.id)

        n_good = r.n_type

        room_data = np.zeros((n_good, r.t_max))

        good_list = [n_good - 1, ] + list(range(n_good - 1))

        for prod in good_list:

            users = [
                u for u in User.objects.filter(
                    room_id=r.id, production_good=Converter.reverse_value(prod, n_good=n_good))]

            for t in range(r.t_max):

                monetary_conform_list = []

                choices = Choice.objects.filter(room_id=r.id, t=t, player_id__in=[u.player_id for u in users])

                assert len(choices) == len(users)

                for c in choices:

                    desired = Converter.convert_value(c.desired_good, n_good=n_good)
                    in_hand = Converter.convert_value(c.good_in_hand, n_good=n_good)

                    cons = Converter.convert_value(
                        [u for u in users if u.player_id == c.player_id][0].consumption_good,
                        n_good=n_good)

                    if m in (prod, cons):
                        monetary_conform = (in_hand, desired) == (prod, cons)

                    else:
                        monetary_conform = (in_hand, desired) in [(prod, m), (m, cons)]

                    monetary_conform_list.append(monetary_conform)

                room_data[prod, t] = np.mean(monetary_conform_list)

        label = economy_labels.get(r.id)

        mean = np.mean(room_data.flatten())
        sem = stats.sem(room_data.flatten())

        keys = label + '_mean', label + '_sem', label + '_monetary_behavior'
        values = mean, sem, room_data

        for k, v in zip(keys, values):
            output_data[k] = v

    print()
    return output_data


if __name__ == '__main__':
    run()
