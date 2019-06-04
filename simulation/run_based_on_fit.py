import os
import numpy as np

from backup import structure

from simulation.run import _run

SCRIPT_FOLDER = os.path.dirname(os.path.abspath(__file__))
DATA_FOLDER = f'{SCRIPT_FOLDER}/../data'

FILE_PATH = f'{DATA_FOLDER}/fit.p'


def get_data(xp_data_list, alpha, beta, gamma, eco, heterogeneous=True, t_max=None):

    alpha = np.array(alpha)
    beta = np.array(beta)
    gamma = np.array(gamma)
    eco = np.array(eco)

    np.random.seed(1234)

    n_rooms = len(xp_data_list)

    # list of DataXpSession
    data = np.zeros(n_rooms, dtype=object)

    for i, xp_d in enumerate(xp_data_list):

        n_good = xp_d.n_good

        prod = xp_d.prod
        cons = xp_d.cons

        if t_max is None:
            t_max = xp_d.t_max

        if heterogeneous:
            cognitive_parameters = [(a, b, g) for a, b, g in
                                    zip(alpha[eco == i], beta[eco == i], gamma[eco == i])]
        else:
            cognitive_parameters = alpha[eco == i].mean(), beta[eco == i].mean(), gamma[eco == i].mean()

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
