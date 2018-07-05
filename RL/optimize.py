import numpy as np
from scipy.optimize import minimize

from game.models import Room, User,Choice
from analysis.tools.conversion import Converter
from RL.model.rl_agent import RLAgent


def compute_score(cognitive_parameters, *args):

    cognitive_parameters = np.asarray(cognitive_parameters)[::-1]

    r, u = args

    data_user = np.zeros(r.t_max)

    n_good = r.n_type

    prod = Converter.convert_value(u.production_good, n_good=n_good)
    cons = Converter.convert_value(u.consumption_good, n_good=n_good)

    agent = RLAgent(prod=prod, cons=cons, n_goods=n_good, cognitive_parameters=cognitive_parameters)

    for t in range(r.t_max):

        choice = Choice.objects.get(room_id=r.id, user_id=u.id, t=t)

        in_hand = Converter.convert_value(choice.good_in_hand, n_good=n_good)
        desired = Converter.convert_value(choice.desired_good, n_good=n_good)

        # agent.choose(in_hand)

        p_choice = agent.get_p_choose(in_hand, desired)

        v = - p_choice
        data_user[t] = v

        # For t+1
        agent.learn_from_human_choice(in_hand=in_hand, desired=desired, successful=int(choice.success))

    error = np.sum(data_user)
    print(cognitive_parameters, error)
    return error


def run():

    print("******** Analysis of strategy *************")

    rooms = Room.objects.all().order_by('id')

    cognitive_parameters = np.array([0.8, 1, 0.01])

    for r in rooms:

        print("\n", "*" * 5, f"Room {r.id}", "*" * 5)

        users = User.objects.filter(room_id=r.id)

        for i, u in enumerate(users):

            res = minimize(fun=compute_score, x0=cognitive_parameters, args=(r, u),
                           bounds=[(0., 1.), (0.5, 1.5), (0.01, 1.)], tol=1e-6, method='BFGS')
            alpha, beta, gamma = res.x
            print(f"User {u.id}: score = {r}, cognitive parameters: a={alpha}, b={beta}, g={gamma}")
            print(res)


if __name__ == "__main__":
    run()
