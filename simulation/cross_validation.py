import os
import numpy as np

from backup import structure

from simulation.run import _run

SCRIPT_FOLDER = os.path.dirname(os.path.abspath(__file__))
DATA_FOLDER = f'{SCRIPT_FOLDER}/../data'

FILE_PATH = f'{DATA_FOLDER}/fit.p'


def get_data(n_good, prod, cons, alpha, beta, gamma, t_max, heterogeneous=True):

    alpha = np.array(alpha)
    beta = np.array(beta)
    gamma = np.array(gamma)

    np.random.seed(1234)

    if heterogeneous:
        cognitive_parameters = [(a, b, g) for a, b, g in
                                zip(alpha, beta, gamma)]
    else:
        cognitive_parameters = alpha.mean(), beta.mean(), gamma.mean()

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

    return sim_d
