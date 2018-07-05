import numpy as np
from scipy.optimize import minimize
from hyperopt import fmin, rand, hp, tpe

from game.models import Room, User,Choice
from analysis.tools.conversion import Converter
from RL.model.rl_agent import RLAgent


class Fit:

    def __init__(self, room, user):

        self.r = room
        self.u = user

    def compute_score(self, cognitive_parameters):

        data_user = np.zeros(self.r.t_max)

        n_good = self.r.n_type

        prod = Converter.convert_value(self.u.production_good, n_good=n_good)
        cons = Converter.convert_value(self.u.consumption_good, n_good=n_good)

        agent = RLAgent(prod=prod, cons=cons, n_goods=n_good, cognitive_parameters=cognitive_parameters)

        for t in range(self.r.t_max):

            choice = Choice.objects.get(room_id=self.r.id, user_id=self.u.id, t=t)

            in_hand = Converter.convert_value(choice.good_in_hand, n_good=n_good)
            desired = Converter.convert_value(choice.desired_good, n_good=n_good)

            # agent.choose(in_hand)

            p_choice = agent.get_p_choose(in_hand, desired)

            v = - p_choice
            data_user[t] = v

            # For t+1
            agent.learn_from_human_choice(in_hand=in_hand, desired=desired, successful=int(choice.success))

        error = np.mean(data_user)

        print('Error: ', error, end='\r')

        return error


def run():

    print("******** Analysis of strategy *************")

    rooms = Room.objects.all().order_by('id')

    space = [
        hp.uniform('alpha', 0.1, 1.),
        hp.uniform('beta', 0.75, 1.25),
        hp.uniform('gamma', 0.1,  1.)
    ]

    for r in rooms:

        print("\n", "*" * 5, f"Room {r.id}", "*" * 5)

        users = User.objects.filter(room_id=r.id)

        for i, u in enumerate(users):

            f = Fit(user=u, room=r)

            # res = minimize(fun=compute_score, x0=cognitive_parameters, args=(r, u),
            #                bounds=[(0., .99), (0.5, 1.5), (0., 1.)])
            # alpha, beta, gamma = res.x

            res = fmin(
                fn=f.compute_score,
                space=space,
                algo=tpe.suggest,
                max_evals=40,
            )

            alpha, beta, gamma = res['alpha'], res['beta'], res['gamma']

            print(f"User {u.id}: score = {r}, cognitive parameters: a={alpha}, b={beta}, g={gamma}")

        break


if __name__ == "__main__":
    run()
