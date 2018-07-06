import numpy as np
from scipy import stats

from analysis.tools.conversion import Converter
from analysis.tools import economy
from game.models import Room, User, Choice
import scipy.stats


def run():

    output_data = {}

    print("******** Analysis of strategy *************")

    rooms = Room.objects.all().order_by('id')

    for r in rooms:

        print("\n", "*" * 5, f"Room {r.id}", "*" * 5)

        n_good = r.n_type

        data_room_mean = np.zeros(n_good)
        data_room_std = np.zeros(n_good)

        # ----- All users

        users = User.objects.filter(room_id=r.id)
        n_users = len(users)

        for g in range(n_good):

            data_good_mean = np.zeros(n_users)

            for i, u in enumerate(users):

                data_user = np.zeros(r.t_max, dtype=int)

                prod = Converter.convert_value(u.production_good, n_good=n_good)
                cons = Converter.convert_value(u.consumption_good, n_good=n_good)

                for t in range(r.t_max):

                    choice = Choice.objects.get(room_id=r.id, user_id=u.id, t=t)

                    in_hand = Converter.convert_value(choice.good_in_hand, n_good=n_good)
                    desired = Converter.convert_value(choice.desired_good, n_good=n_good)

                    # By default behavior in non monetary
                    v = 0

                    if prod != g and cons != g:

                        # ----- Users supposed to use g as a medium

                        if in_hand == prod:
                            if desired != cons and desired == g:
                                v = 1

                        else:
                            if desired == cons and in_hand == g:
                                v = 1

                    else:

                        # ---- Users are supposed to make indirect exchange

                        if in_hand == prod and desired == cons:
                            v = 1

                    data_user[t] = v

                data_good_mean[i] = np.mean(data_user)

            data_room_mean[g] = np.mean(data_good_mean)
            data_room_std[g] = scipy.stats.sem(data_good_mean)

        label = economy.labels.get(r.id) + '_monetary_behavior_pool'
        output_data[label] = {
            'mean': data_room_mean,
            'std': data_room_std
        }

    return output_data
