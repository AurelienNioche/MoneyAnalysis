import numpy as np

from xp import xp
from backup import structure

from simulation.run import _run


def get_data(xp_data, economy_model='prod: i-1'):

    np.random.seed(1234)

    n_rooms = len(xp_data)

    # list of DataXpSession
    data = np.zeros(n_rooms, dtype=object)

    for i, xp_d in enumerate(xp_data):

        n_good = xp_d.n_good
        t_max = xp_d.t_max

        # prod = xp_d.prod
        cons = xp_d.cons

        dist = []
        for g in range(n_good):
            dist.append(np.sum(cons == g))

        alpha = np.random.uniform(0.1, 0.25)
        beta = np.random.uniform(0.8, 1.2)
        gamma = np.random.uniform(0.1, 0.15)

        agent_model = 'RLAgent'

        param, bkp = _run({
            'cognitive_parameters': (alpha, beta, gamma),
            'distribution': dist,
            't_max': t_max,
            'economy_model': economy_model,
            'agent_model': agent_model,
            'n_good': n_good,
            'seed': np.random.randint(2 ** 32 - 1)
        })

        sim_d = structure.DataXPSession(
            in_hand=bkp['in_hand'],
            desired=bkp['desired'],
            prod=bkp['prod'],
            cons=bkp['cons'],
            n_good=n_good,
            t_max=t_max
        )

        data[i] = sim_d

    return data
