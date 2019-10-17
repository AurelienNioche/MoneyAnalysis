import os
import numpy as np

from backup import structure

import simulation.economy

SCRIPT_FOLDER = os.path.dirname(os.path.abspath(__file__))
DATA_FOLDER = f'{SCRIPT_FOLDER}/../data'

FILE_PATH = f'{DATA_FOLDER}/fit.p'


def _run(param):

    e = simulation.economy.Economy(**param)
    return param, e.run()


def get_data(xp_data_list, best_parameters, eco,
             heterogeneous=True, t_max=None, seed=123):

    eco = np.array(eco)

    np.random.seed(seed=seed)

    n_rooms = len(xp_data_list)

    # list of DataXpSession
    data = np.zeros(n_rooms, dtype=object)

    for i, xp_d in enumerate(xp_data_list):

        n_good = xp_d.n_good

        prod = xp_d.prod
        cons = xp_d.cons

        if t_max is None:
            t_max = xp_d.t_max

        param = []
        for k in sorted(best_parameters):
            param.append(
                np.asarray(best_parameters[k])[eco == i]
            )

        if heterogeneous:
            cognitive_parameters = list(zip(*param))
        else:
            cognitive_parameters = [p.mean() for p in param]

        param, bkp = _run({
            'cognitive_parameters': cognitive_parameters,
            'prod': prod,
            'cons': cons,
            't_max': t_max,
            'heterogeneous': heterogeneous,
            'seed': np.random.randint(2 ** 32 - 1)
        })

        sim_d = structure.DataXPSession(
            in_hand=bkp['in_hand'],
            desired=bkp['desired'],
            success=bkp['success'],
            prod=bkp['prod'],
            cons=bkp['cons'],
            n_good=n_good,
            t_max=t_max
        )

        data[i] = sim_d

    return data
