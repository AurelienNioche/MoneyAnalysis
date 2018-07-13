import argparse
import itertools
from tqdm import tqdm
import numpy as np
import multiprocessing
import os


import backup.backup
import backup.structure

import simulation.economy
import analysis.tools.economy
import analysis.graph.phase_diagram


def get_parameters(
        n_good=3,
        agent_model='RLAgent',
        m=0,
        constant_x_value=np.array([50, ]),
        constant_x_index=np.array([0, ]),
        t_max=200,
        economy_model='prod: i-1',
        range_repartition=range(10, 200, 20),
        n_cog_value=3):

    assert len(constant_x_value) == len(constant_x_index), \
        '"constant_x_value" and "constant_x_index" should have equal size!'
    assert agent_model in ('RLAgent', 'QLearner'), 'Bad argument for "agent_model"!'
    assert economy_model in ('prod: i-1', 'prod: i+1'), 'Bad argument for "economy_model"!'

    if agent_model == 'RLAgent':
        first_cog_range = np.linspace(0.1, 0.5, n_cog_value)
        second_cog_range = np.linspace(0.75, 1.5, n_cog_value)
        third_cog_range = np.linspace(0.01, 0.15, n_cog_value)

    else:
        first_cog_range = np.linspace(0.1, 0.5, n_cog_value)
        second_cog_range = np.linspace(0.01, 0.1, n_cog_value)
        third_cog_range = np.linspace(0.1, 0.5, n_cog_value)

    # ------------------------------ #

    repartition = list(itertools.product(range_repartition, repeat=n_good-len(constant_x_index)))

    # ---------- #

    var_param = itertools.product(first_cog_range, second_cog_range, third_cog_range, repartition)

    # ----------- #

    parameters = []

    for alpha, beta, gamma, rpt in var_param:

        complete_rpt = np.zeros(n_good, dtype=int)
        gen_rpt = (i for i in rpt)
        gen_cst = (i for i in constant_x_value)
        for i in range(n_good):
            if i in constant_x_index:
                complete_rpt[i] = next(gen_cst)
            else:
                complete_rpt[i] = next(gen_rpt)
        complete_rpt = tuple(complete_rpt)

        param = {
            'cognitive_parameters': (alpha, beta, gamma),
            'repartition': complete_rpt,
            't_max': t_max,
            'economy_model': economy_model,
            'agent_model': agent_model,
            # 'm': m,
            'n_good': n_good,
            'seed': np.random.randint(2**32-1),
            'constant_x_index': constant_x_index,
            'constant_x_value': constant_x_value
        }
        parameters.append(param)

    return parameters


def get_experiment_like_parameters():

    parameters = []

    rooms = (414, 415, 416, 417)
    n_sim = 20

    t_max = 50
    economy_model = 'prod: i-1'

    repartitions = [analysis.tools.economy.repartitions.get(i) for i in rooms]

    n_cog_value = 3
    first_cog_range = np.linspace(0.1, 0.5, n_cog_value)
    second_cog_range = np.linspace(0.75, 1.5, n_cog_value)
    third_cog_range = np.linspace(0.01, 0.15, n_cog_value)

    for i in range(len(rooms)):

        for n in range(n_sim):

            n_good = len(repartitions[i])

            alpha, beta, gamma = \
                np.random.choice(first_cog_range),\
                np.random.choice(second_cog_range),\
                np.random.choice(third_cog_range)

            alpha = 0.1
            beta = 1
            gamma = 0.01

            param = {
                'cognitive_parameters': (alpha, beta, gamma),
                'repartition': repartitions[i],
                't_max': t_max,
                'economy_model': economy_model,
                'agent_model': 'RLAgent',
                'n_good': n_good,
                'seed': np.random.randint(2**32-1),
                'room_id': rooms[i]
            }

            parameters.append(param)

    return parameters


def _run(param):

    e = simulation.economy.Economy(**param)
    return param, e.run()


def _produce_data(exp, n_good):

    tqdm.write("Run simulations.")

    if exp:

        params = get_experiment_like_parameters()

    else:

        params = get_parameters(
            n_good=n_good,
            agent_model='RLAgent',
            constant_x_index=np.array([0, ]) if n_good == 3 else np.array([0, 1]),
            constant_x_value=np.array([50, ]) if n_good == 3 else np.array([50, 50])
        )

    max_ = len(params)

    data = backup.structure.Data(n=len(params))

    with multiprocessing.Pool(processes=os.cpu_count()) as p:

        with tqdm(total=max_) as pbar:
            for pr, b in p.imap_unordered(_run, params):
                data.append(backup=b, param=pr)
                pbar.update()

    return data


def get_pool_data(force=False, exp_like=False, n_good=3):

    if exp_like:
        data_file = 'data/exp_like.p'

    else:
        data_file = f'data/phase_{n_good}_goods.p'

    if force or not os.path.exists(data_file):

        bkp = _produce_data(exp_like, n_good)

        backup.backup.save(obj=bkp, file_name=data_file)

    else:
        bkp = backup.backup.load(data_file)

    return bkp


def run(exp_like=False):

    parser = argparse.ArgumentParser(description='Run money simulations.')

    parser.add_argument('-f', '--force', action="store_true", default=False,
                        help="Force creation of new data.")

    parser.add_argument('-e', '--exp', action="store_true", default=False,
                        help="Experiment like simulations")

    parser.add_argument('-n', '--n_good', type=int, help="number of goods", default=3)

    args = parser.parse_args()

    if not exp_like:
        bkp = get_pool_data(force=args.force, exp_like=args.exp, n_good=args.n_good)
    else:

        bkp = get_pool_data(force=args.force, exp_like=exp_like, n_good=args.n_good)

    return bkp


if __name__ == "__main__":
    run()
