import argparse
import itertools
from tqdm import tqdm
import numpy as np
import multiprocessing
import os


import backup.backup
import backup.structure

import simulation.economy
import simulation.parameters

import analysis.tools.economy


def _get_phase_parameters(
        n_good=3,
        agent_model='RLAgent',
        constant_x_value=np.array([50, ]),
        constant_x_index=np.array([0, ]),
        t_max=100,
        economy_model='prod: i-1',
        range_repartition=range(10, 200, 20),
        n_cog_value=3):

    assert len(constant_x_value) == len(constant_x_index), \
        '"constant_x_value" and "constant_x_index" should have equal size!'
    assert agent_model in ('RLAgent', ), 'Bad argument for "agent_model"!'
    assert economy_model in ('prod: i-1', 'prod: i+1'), 'Bad argument for "economy_model"!'

    first_cog_range = np.linspace(0.1, 0.25, n_cog_value)
    second_cog_range = np.linspace(0.8, 1.2, n_cog_value)
    third_cog_range = np.linspace(0.1, 0.15, n_cog_value)

    # ------------------------------ #

    repartition = list(itertools.product(range_repartition, repeat=n_good-len(constant_x_index)))

    # ---------- #

    var_param = itertools.product(first_cog_range, second_cog_range, third_cog_range, repartition)

    # ----------- #

    parameters = []

    for alpha, beta, gamma, rpt in var_param:

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
            'cognitive_parameters': (alpha, beta, gamma),
            'distribution': complete_dist,
            't_max': t_max,
            'economy_model': economy_model,
            'agent_model': agent_model,
            'n_good': n_good,
            'seed': np.random.randint(2**32-1),
            'constant_x_index': constant_x_index,
            'constant_x_value': constant_x_value
        }
        parameters.append(param)

    return parameters


def _get_experiment_like_parameters():

    parameters = []

    rooms = (414, 415, 416, 417)

    distributions = [analysis.tools.economy.distributions.get(i) for i in rooms]

    i = 0
    for i_r in range(len(rooms)):

        for _ in range(simulation.parameters.n_sim):

            n_good = len(distributions[i_r])
            
            param = {
                'cognitive_parameters': simulation.parameters.cognitive_parameters[i],
                'seed': simulation.parameters.seeds[i],
                't_max': simulation.parameters.t_max,
                'economy_model': simulation.parameters.economy_model,
                'agent_model': simulation.parameters.agent_model,
                'n_good': n_good,
                'distribution': distributions[i_r],
                'room_id': rooms[i_r]
            }

            parameters.append(param)

            i += 1

    return parameters


def _run(param):

    e = simulation.economy.Economy(**param)
    return param, e.run()


def _produce_data(phase, n_good):

    tqdm.write("Run simulations.")

    if phase:

        params = _get_phase_parameters(
            n_good=n_good,
            agent_model='RLAgent',
            constant_x_index=np.array([0, ]) if n_good == 3 else np.array([0, 1]),
            constant_x_value=np.array([50, ]) if n_good == 3 else np.array([50, 50])
        )

    else:

        params = _get_experiment_like_parameters()

    max_ = len(params)

    data = backup.structure.Data()

    with multiprocessing.Pool(processes=os.cpu_count()) as p:

        with tqdm(total=max_) as pbar:
            for pr, b in p.imap_unordered(_run, params):
                data.append(bkp=b, param=pr)
                pbar.update()

    return data


def get_data(phase=None, n_good=None):

    parser = argparse.ArgumentParser(description='Run money simulations.')
    parser.add_argument('-f', '--force', action="store_true", default=False,
                        help="Force creation of new data.")
    args = parser.parse_args()

    force = args.force

    if phase:
        data_folder = f'data/phase_{n_good}_goods'

    else:
        data_folder = f'data/exp_like'

    if force or not os.path.exists(data_folder):

        bkp = _produce_data(phase, n_good)
        bkp.save(data_folder)

    else:
        bkp = backup.structure.Data()
        bkp.load(data_folder)

    return bkp
