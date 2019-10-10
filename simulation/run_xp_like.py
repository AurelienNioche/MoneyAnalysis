import numpy as np

from backup import structure

from simulation.run import _run


def get_data(xp_data, agent_model=None, t_max=None, alpha_minus=.175, alpha_plus=.175, beta=1, gamma=.125,
             random_cognitive_param=False, seed=123):

    np.random.seed(seed)

    n_rooms = len(xp_data)

    # list of DataXpSession
    data = np.zeros(n_rooms, dtype=object)

    for i, xp_d in enumerate(xp_data):

        n_good = xp_d.n_good

        if t_max is None:
            t_max = xp_d.t_max

        prod = xp_d.prod
        cons = xp_d.cons

        if random_cognitive_param:
            alpha = np.random.uniform(0.1, 0.25)
            beta = np.random.uniform(0.8, 1.2)
            gamma = np.random.uniform(0.1, 0.15)

        param, bkp = _run({
            'cognitive_parameters': (alpha_minus, alpha_plus, beta, gamma),
            'cons': cons,
            'prod': prod,
            't_max': t_max,
            'seed': seed,
            'agent_model': agent_model.__name__
        })

        sim_d = structure.DataXPSession(
            in_hand=bkp['in_hand'],
            desired=bkp['desired'],
            prod=bkp['prod'],
            cons=bkp['cons'],
            success=bkp['success'],
            acceptance=bkp['acceptance'],
            n_good=n_good,
            t_max=t_max
        )

        data[i] = sim_d

    return data
