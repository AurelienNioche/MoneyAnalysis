import numpy as np

from backup import structure

import simulation.economy


def _run(param):

    e = simulation.economy.Economy(**param)
    return param, e.run()


def get_data(xp_data, agent_model, t_max=None,
             random_cognitive_param=False, seed=123, **cognitive_parameters):

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

            cog_param = (alpha, beta, gamma)

        elif not len(cognitive_parameters):
            alpha = .175
            beta = 1
            gamma = .125

            cog_param = (alpha, beta, gamma)
        else:
            cog_param = [cognitive_parameters[k]
                         for k in sorted(cognitive_parameters.keys())]

        param, bkp = _run({
            'cognitive_parameters': cog_param,
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
