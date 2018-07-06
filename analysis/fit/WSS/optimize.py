import numpy as np

from analysis.tools.conversion import Converter
from game.models import Room, User, Choice
from simulation.model.WSS.wss_agent import WSSAgent


def compute_error(r, u):

    data_user = np.zeros(r.t_max, dtype=int)

    n_good = r.n_type

    prod = Converter.convert_value(u.production_good, n_good=n_good)
    cons = Converter.convert_value(u.consumption_good, n_good=n_good)

    agent = WSSAgent(prod=prod, cons=cons, n_good=n_good)

    previous_success = None

    for t in range(r.t_max):

        choice = Choice.objects.get(room_id=r.id, user_id=u.id, t=t)

        in_hand = Converter.convert_value(choice.good_in_hand, n_good=n_good)
        desired = Converter.convert_value(choice.desired_good, n_good=n_good)

        v = desired != agent.choose(in_hand=in_hand, previous_success=previous_success)

        data_user[t] = v

        # For t + 1
        previous_success = choice.success

    return np.mean(data_user)


def run():

    print("******** Analysis: Win, Stay or Switch *************")

    rooms = Room.objects.all().order_by('id')

    for r in rooms:

        print("\n", "*" * 5, f"Room {r.id}", "*" * 5)

        users = User.objects.filter(room_id=r.id)

        errors = np.zeros(len(users))

        for i, u in enumerate(users):

            error = compute_error(r, u)

            print(f"User {u.id}: error = {error}")

            errors[i] = error

        print(f"Mean error = {np.mean(errors):.2f} (+/- {np.std(errors):.2f})")
        print()
