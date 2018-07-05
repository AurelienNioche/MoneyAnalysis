import numpy as np
from scipy.optimize import minimize

from game.models import Room, User,Choice
from analysis.tools.conversion import Converter
from model.rl_agent import RLAgent


def compute_score(cognitive_parameters, *args):

    r, u = args

    data_user = np.zeros(r.t_max, dtype=int)

    n_good = r.n_type

    prod = Converter.convert_value(u.production_good, n_good=n_good)
    cons = Converter.convert_value(u.consumption_good, n_good=n_good)

    agent = RLAgent(prod=prod, cons=cons, n_goods=n_good, cognitive_parameters=cognitive_parameters)

    for t in range(r.t_max):

        choice = Choice.objects.get(room_id=r.id, user_id=u.id, t=t)

        in_hand = Converter.convert_value(choice.good_in_hand, n_good=n_good)
        desired = Converter.convert_value(choice.desired_good, n_good=n_good)

        agent.choose(in_hand)
        agent.learn(int(choice.success))

        exchange_v = agent.get_exchange_value(in_hand, desired)

        v = 1 - exchange_v

        data_user[t] = v

    return np.sum(data_user)


def run():

    print("******** Analysis of strategy *************")

    rooms = Room.objects.all().order_by('id')

    cognitive_parameters = np.array([0.5, 0.5, 0.5])

    for r in rooms:

        print("\n", "*" * 5, f"Room {r.id}", "*" * 5)

        users = User.objects.filter(room_id=r.id)

        for i, u in enumerate(users):

            alpha, beta, gamma = minimize(fun=compute_score, x0=cognitive_parameters, args=(r, u)).x

            print(f"User {u.id}: score = {r}, cognitive parameters: a={alpha}, b={beta}, g={gamma}")


if __name__ == "__main__":
    run()
