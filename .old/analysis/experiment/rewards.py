import numpy as np

from game.models import User


def run():

    print("\n********* Rewards ***********\n")
    users = User.objects.all()
    var = 10 + 0.20*np.array([u.score for u in users])
    print(f'Reward = {np.mean(var):.2f} (+/- {np.std(var):.2f} STD)')
    print()