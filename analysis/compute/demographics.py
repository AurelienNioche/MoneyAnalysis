import numpy as np

from game.models import User


def run():

    print("\n********* Demographics ***********\n")
    users = User.objects.all()
    ages = [u.age for u in users]
    print(f'Age = {np.mean(ages):.2f} (+/- {np.std(ages):.2f} STD)')
    sex = [u.gender for u in users]
    print(f'Female = {sex.count("female") / len(sex) * 100:.2f}%')
    print()
