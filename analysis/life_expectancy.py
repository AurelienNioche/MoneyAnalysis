import numpy as np
from scipy import stats

from analysis.tools.conversion import Converter
from analysis.tools import economy_labels
from game.models import Room, User, Choice


def run():

    output_data = {}

    print('*' * 5)
    print('Life expectancy')
    print('*' * 5)
    # -------------- #

    rooms = Room.objects.all().order_by('id')

    for r in rooms:

        print('*' * 5 + f'Room {r.id}' + '*' * 5)

        n_good = r.n_type

        room_data = np.zeros(n_good)

        good_list = [n_good - 1, ] + list(range(n_good - 1))

        for g in good_list:

            n_g = np.zeros(r.t_max)
            n_prod = np.zeros(r.t_max)
            n_remaining = np.zeros(r.t_max)
            n_cons = np.zeros(r.t_max)

            for t in range(r.t_max):

                print('t=', t)

                in_hands = Choice.objects.filter(
                    room_id=r.id, good_in_hand=Converter.reverse_value(g, n_good=n_good), t=t

                )

                if t == 0:

                    n_prod[t] = len(in_hands)
                    n_g[t] = len(in_hands)

                else:

                    n_prod[t] = n_cons[t-1]
                    n_g[t] = n_remaining[t-1] + n_prod[t]

                assert n_g[t] == len(in_hands), f'{n_g[t]}, {len(in_hands)}'

                choices = Choice.objects.filter(
                    room_id=r.id, desired_good=Converter.reverse_value(g, n_good=n_good), t=t,
                    success=True
                )

                for c in choices:

                    u_cons_good = User.objects.get(id=c.user_id).consumption_good

                    cons = Converter.convert_value(u_cons_good, n_good=n_good)
                    desired = Converter.convert_value(c.desired_good, n_good=n_good)

                    if cons == desired:
                        n_cons[t] += 1

                n_remaining[t] = n_g[t] - n_cons[t]

                print('prod', n_prod[t])
                print('remaining', n_remaining[t])
                print('cons', n_cons[t])

            # print()
            # room_data[prod] = np.mean(n_remaining)


        # label = economy_labels.get(r.id)
        #
        # mean = np.mean(room_data.flatten())
        # sem = stats.sem(room_data.flatten())
        #
        # keys = label + '_mean', label + '_sem', label + '_monetary_behavior'
        # values = mean, sem, room_data
        #
        # for k, v in zip(keys, values):
        #     output_data[k] = v

    print()
    return output_data

