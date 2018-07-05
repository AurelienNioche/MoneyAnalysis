import numpy as np
from scipy import stats

from analysis.tools.conversion import Converter
from analysis.tools import economy_labels
from game.models import Room, User, Choice


class WWSAgent:

    def __init__(self, n_good, prod, cons):

        self.n_good = n_good
        self.prod = prod
        self.cons = cons

    def choose(self, in_hand):

        desired = 0
        return desired


def compute_error(r, u):

    data_user = np.zeros(r.t_max, dtype=int)

    n_good = r.n_type

    prod = Converter.convert_value(u.production_good, n_good=n_good)
    cons = Converter.convert_value(u.consumption_good, n_good=n_good)

    agent = WWSAgent(prod=prod, cons=cons, n_good=n_good)

    for t in range(r.t_max):

        choice = Choice.objects.get(room_id=r.id, user_id=u.id, t=t)

        in_hand = Converter.convert_value(choice.good_in_hand, n_good=n_good)
        desired = Converter.convert_value(choice.desired_good, n_good=n_good)

        v = desired != agent.choose(in_hand=in_hand)

        data_user[t] = v

    return np.sum(data_user)


def run():

    print("******** Analysis of strategy *************")

    rooms = Room.objects.all().order_by('id')

    for r in rooms:

        print("\n", "*" * 5, f"Room {r.id}", "*" * 5)

        users = User.objects.filter(room_id=r.id)

        for i, u in enumerate(users):

            r = compute_error(r, u)

            print(f"User {u.id}: error = {r}")

        break