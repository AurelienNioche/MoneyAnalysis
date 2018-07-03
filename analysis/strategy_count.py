import numpy as np
from scipy import stats

from analysis.tools.conversion import Converter
from analysis.tools import economy_labels
from game.models import Room, User, Choice


def run():

    output_data = {}

    print("******** Analysis of strategy *************")

    rooms = Room.objects.all().order_by('id')

    for r in rooms:

        print("\n", "*" * 5, f"Room {r.id}", "*" * 5)

        n_good = r.n_type

        good_list = [n_good - 1, ] + list(range(n_good - 1))

        for prod in good_list:

            print(f"\nProducers of {prod}")

            users = User.objects.filter(
                room_id=r.id, production_good=Converter.reverse_value(prod, n_good=n_good))

            n_users = len(users)

            cons = Converter.convert_value(users[0].consumption_good, n_good=n_good)

            for g in range(n_good):

                data = np.zeros((n_users, r.t_max), dtype=int)

                for t in range(r.t_max):

                    for i, u in enumerate(users):

                        choice = Choice.objects.get(room_id=r.id, user_id=u.id, t=t)

                        in_hand = Converter.convert_value(choice.good_in_hand, n_good=n_good)
                        desired = Converter.convert_value(choice.desired_good, n_good=n_good)

                        v = 0

                        if in_hand == prod:
                            if desired != cons and desired == g:
                                v = 1

                        else:
                            if desired == cons and in_hand == g:
                                v = 1

                        data[i, t] = v

                mean = np.mean(data)
                print(f"mean for {g} = {mean * 100:.2f}")
