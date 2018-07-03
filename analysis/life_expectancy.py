import numpy as np

from analysis.tools.conversion import Converter
from analysis.tools import economy_labels
from game.models import Room, User, Choice


def run():

    output_data = {}

    print('*' * 5)
    print('Life expectancy')
    print('*' * 5 + '\n')

    # -------------- #

    rooms = Room.objects.all().order_by('id')

    for r in rooms:

        print('=' * 20 + f'Room {r.id}' + '=' * 20)

        n_good = r.n_type

        n_g = np.zeros((n_good, r.t_max), dtype=int)
        n_prod = np.zeros((n_good, r.t_max), dtype=int)
        n_remaining = np.zeros((n_good, r.t_max), dtype=int)
        n_cons = np.zeros((n_good, r.t_max), dtype=int)

        for g in range(n_good):

            g_reversed = Converter.reverse_value(g, n_good=n_good)
            print(f"----------------------- g = {g} ------------------------")  # (g_reversed = {g_reversed})")

            for t in range(r.t_max):

                print(f'\n******* t = {t} *******\n')

                # ------------- #
                # Compute number of goods in circulation for g

                in_hands = Choice.objects.filter(
                    room_id=r.id, good_in_hand=g_reversed, t=t
                )

                n_g[g, t] = len(in_hands)  # for t > 0: n_g[g, t] = n_remaining[g, t-1] + n_prod[g, t]

                # ------------- #
                # Compute production for g

                if t == 0:
                    n_prod[g, t] = n_g[g, t]

                else:
                    users = User.objects.filter(
                        room_id=r.id,
                        production_good=g_reversed
                    )

                    choices = Choice.objects.filter(
                        room_id=r.id,
                        desired_good=users[0].consumption_good,
                        t=t,
                        success=True,
                        user_id__in=[u.id for u in users]
                    )

                    if (t+1) < r.t_max:
                        n_prod[g, t+1] = len(choices)

                # ---------- #
                # Compute number of consumption for g

                choices = Choice.objects.filter(
                    room_id=r.id, desired_good=g_reversed, t=t,
                    success=True
                )

                for c in choices:

                    u = User.objects.get(id=c.user_id)
                    cons = Converter.convert_value(u.consumption_good, n_good=n_good)

                    if cons == g:
                        # print(f"user id {u.id} has g in hand and consumes it")
                        n_cons[g, t] += 1

                    # else:
                    #     print(f"user id {u.id} has now g in hand")

                # --------------- #
                # Compute number of remaining for g

                n_remaining[g, t] = n_g[g, t] - n_cons[g, t]

                # --------------- #
                # Summary

                print('n_g', n_g[g, t])
                print('n_prod', n_prod[g, t])
                print('n_remaining', n_remaining[g, t])
                print('n_cons', n_cons[g, t])

                # --------------- #

        label = economy_labels.get(r.id) + "_life_expectancy"
        output_data[label] = {
            "n_g": n_g,
            "n_prod": n_prod,
            "n_cons": n_cons,
            "n_remaining": n_remaining
        }

    print()
    return output_data

