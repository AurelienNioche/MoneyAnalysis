import numpy as np
# from scipy.optimize import minimize
from hyperopt import fmin, hp, tpe  # rand
import pickle
import matplotlib.pyplot as plt
import matplotlib.gridspec as grd
import itertools as it
import os
import argparse

from game.models import Room, User, Choice
from analysis.tools.conversion import Converter
from simulation.model.RL.rl_agent import RLAgent
from analysis.tools import economy


class Fit:

    def __init__(self, room, user):

        self.r = room
        self.u = user

        self.error = None

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

            v = 1 - p_choice
            data_user[t] = v

            # For t+1
            agent.learn_from_human_choice(in_hand=in_hand, desired=desired, successful=int(choice.success))

        error = np.sum(data_user)

        print('Error: ', error, end='\r')

        self.error = error
        return error


def produce_data(f_name):

    print("******** Analysis of strategy *************")

    rooms = Room.objects.all().order_by('id')

    data = {}

    space = [
        hp.uniform('alpha', 0.1, 1.),
        hp.uniform('beta', 0.75, 1.25),
        hp.uniform('gamma', 0.001,  1.)
    ]

    for r in rooms:

        label = economy.labels.get(r.id)

        data[label] = {
            'alpha': np.zeros(r.n_user),
            'beta': np.zeros(r.n_user),
            'gamma': np.zeros(r.n_user)
        }

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
                max_evals=1000,
            )

            alpha, beta, gamma = res['alpha'], res['beta'], res['gamma']

            for k, v in res.items():
                data[label][k][i] = v

            print(f"User {u.id}: error={f.error}, cognitive parameters: a={alpha:.2f}, b={beta:.2f}, g={gamma:.3f}")

    if not os.path.exists('data'):
        os.makedirs('data')

    pickle.dump(obj=data, file=open(f_name, 'wb'))

    return data


def hist(data, f_name):

    gs = grd.GridSpec(nrows=2, ncols=6)

    fig = plt.figure(figsize=(15, 12))

    coord = it.product(range(2), range(6))

    for room_title, room_value in data.items():

        for k, v in room_value.items():

            ax = fig.add_subplot(gs[next(coord)])

            ax.hist(v, bins='auto')

            ax.set_title(room_title + ' ' + k)

    if f_name is not None:
        os.makedirs('fig', exist_ok=True)
        plt.savefig(f'fig/{f_name}.pdf')
    plt.show()


def run(f_name=None):

    parser = argparse.ArgumentParser(description='Human vs RL agent fitting')

    parser.add_argument('-f', '--force', action="store_true", default=False,
                        help="Force creation of new data.")

    args = parser.parse_args()

    fit_file = 'data/fit.p'

    if args.force or not os.path.exists(fit_file):

        data = produce_data(f_name=fit_file)

    else:

        data = pickle.load(file=open(fit_file, 'rb'))

    hist(data, f_name)


if __name__ == "__main__":

    run()

    # parser = argparse.ArgumentParser(description='Human vs RL agent fitting')
    #
    # parser.add_argument('-f', '--force', action="store_true", default=False,
    #                     help="Force creation of new data.")
    #
    # parsed_args = parser.parse_args()
    #
    # main(parsed_args)

