import numpy as np

from analysis.tools.conversion import Converter
from analysis.tools import economy_labels
from game.models import Room, User, Choice

m = 0


def run():

    global m
    data = {}

    rooms = Room.objects.all().order_by('id')

    for r in rooms:

        label = economy_labels.get(r.id) + '_monetary_behavior'

        n_good = r.n_type

        data[label] = np.zeros((n_good, r.t_max), dtype=int)

        good_list = [n_good - 1, ] + list(range(n_good - 1))

        for prod_good in good_list:

            users = [u for u in
                User.objects.filter(room_id=r.id, production_good=Converter.reverse_value(prod_good, n_good=n_good))]

            for t in range(r.t_max):

                monetary_conform_list = []

                choices = Choice.objects.filter(room_id=r.id, t=t, player_id__in=[u.player_id for u in users])

                print(len(choices))
                print(len(users))
                assert len(choices) == len(users)

                for c in choices:

                    desired_good = Converter.convert_value(c.desired_good, n_good=n_good)
                    in_hand = Converter.convert_value(c.good_in_hand, n_good=n_good)
                    cons_good = Converter.convert_value(
                        [u for u in users if u.player_id == c.player_id][0].consumption_good,
                        n_good=n_good)

                    if m in (prod_good, cons_good):

                        monetary_conform = (in_hand, desired_good) == (prod_good, cons_good)

                    else:

                        monetary_conform = (in_hand, desired_good) in [(prod_good, m), (m, cons_good)]

                    monetary_conform_list.append(monetary_conform)

                data[label][prod_good, t] = np.mean(monetary_conform_list)

    return data


if __name__ == '__main__':
    run()
