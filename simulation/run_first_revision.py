import itertools
from tqdm import tqdm
import numpy as np
import multiprocessing
import os


import backup.backup
import backup.structure

import simulation.economy


def _get_phase_parameters(
        agent_model,
        n_good=3,
        constant_x_value=np.array([50, ]),
        constant_x_index=np.array([0, ]),
        t_max=100,
        economy_model='prod: i-1',
        range_repartition=range(10, 210, 10),
        n_cog_value=3):

    assert len(constant_x_value) == len(constant_x_index), \
        '"constant_x_value" and "constant_x_index" should have equal size!'
    assert agent_model in ('RLAgent', ), 'Bad argument for "agent_model"!'
    assert economy_model in ('prod: i-1', 'prod: i+1'), \
        'Bad argument for "economy_model"!'

    ranges = []
    for b in agent_model.bounds:
        ranges.append(
            np.linspace(b[1], b[2], n_cog_value)
        )
    # ------------------------------ #

    repartition = list(itertools.product(range_repartition,
                                         repeat=n_good-len(constant_x_index)))

    # ---------- #

    ranges.append(repartition)

    var_param = itertools.product(*ranges)

    # ----------- #

    parameters = []

    for v in var_param:

        cog_param = v[:-1]
        rpt = v[-1]

        complete_dist = np.zeros(n_good, dtype=int)
        gen_rpt = (i for i in rpt)
        gen_cst = (i for i in constant_x_value)
        for i in range(n_good):
            if i in constant_x_index:
                complete_dist[i] = next(gen_cst)
            else:
                complete_dist[i] = next(gen_rpt)
        complete_dist = tuple(complete_dist)

        param = {
            'cognitive_parameters': cog_param,
            'distribution': complete_dist,
            't_max': t_max,
            'economy_model': economy_model,
            'agent_model': agent_model.__name__,
            'seed': np.random.randint(2**32-1)
        }
        parameters.append(param)

    return parameters


def _run(param):

    e = simulation.economy.Economy(**param)
    return param, e.run()


def _produce_data(n_good, agent_model, fake=False):

    tqdm.write("Compute parameters...", end=' ')

    params = _get_phase_parameters(
        n_good=n_good,
        agent_model=agent_model,
        constant_x_index=np.array([0, ]) if n_good == 3
        else np.array([0, 1]),
        constant_x_value=np.array([50, ]) if n_good == 3
        else np.array([50, 50])
    )
    print('Done!')

    max_ = len(params)

    if fake:
        print(f"I would have compute the results of {max_} economies")
        return

    data = backup.structure.Data()

    with multiprocessing.Pool(processes=os.cpu_count()) as p:

        with tqdm(total=max_) as pbar:
            for pr, b in p.imap_unordered(_run, params):
                data.append(bkp=b, param=pr)
                pbar.update()

    return data


def get_data(n_good, agent_model,
             force=False, fake=False):

    data_folder = os.path.join('data',
                               f'phase_{n_good}_goods_{agent_model.__name__}')

    if fake:
        _produce_data(n_good, agent_model, fake=True)
        return None

    elif force or not os.path.exists(data_folder):

        bkp = _produce_data(n_good, agent_model)
        bkp.save(data_folder)

    else:
        bkp = backup.structure.Data()
        bkp.load(data_folder)

    return bkp
