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

        self.med = [i for i in range(n_good) if i not in (prod, cons)]

        self.possible_strategies = ['direct', ] + [f'indirect_{i}' for i in range(n_good-2)]

        self.current_strategy = None

    def choose(self, in_hand, previous_success):

        if not previous_success:
            possible = [i for i in self.possible_strategies if i != self.current_strategy]
            self.current_strategy = np.random.choice(possible)

        if self.current_strategy == 'direct':

            if in_hand == self.prod:
                desired = self.cons

            else:
                desired = self.prod

        else:

            for i in range(len(self.med)):

                if self.current_strategy == f'indirect_{i}':

                    if in_hand == self.prod:
                        desired = self.med[i]

                    elif in_hand == self.med[i]:
                        desired = self.cons

                    else:
                        desired = self.prod

                    break

        return desired


def compute_error(r, u):

    data_user = np.zeros(r.t_max, dtype=int)

    n_good = r.n_type

    prod = Converter.convert_value(u.production_good, n_good=n_good)
    cons = Converter.convert_value(u.consumption_good, n_good=n_good)

    agent = WWSAgent(prod=prod, cons=cons, n_good=n_good)

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
