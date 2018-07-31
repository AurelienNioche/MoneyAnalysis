import pickle
from tqdm import tqdm
import numpy as np
import os

import backup.structure
import analysis.graph.supplementary


import analysis.tools.format
import simulation.economy


def _run(param):

    e = simulation.economy.Economy(**param)
    return param, e.run()


def _get_parameters():

    parameters = []

    # ------------- #

    n_batch = 20

    base_cog = [
        (0.93, 0.67, 0.26), (0.97, 0.76, 0.25), (0.38, 0.78, 0.29), (0.65, 0.77, 0.23), (0.03, 0.86, 0.18),
        (0.02, 0.67, 0.08), (0.18, 0.81, 0.17), (0.97, 0.68, 0.08), (0.47, 0.76, 0.13)
    ]

    # ----- global params ------ #

    n_sim = len(base_cog) + 1

    n_good = 3
    t_max = 100
    economy_model = 'prod: i-1'
    agent_model = 'RLAgent'

    distribution = [
        (9, 9, 18) for _ in range(n_sim)
    ]

    seeds = np.random.randint(2**32-1, size=n_sim)

    heterogeneous_cog = [
        np.asarray(base_cog)
        [np.random.choice(
            range(len(base_cog)),
            size=np.sum(np.asarray(distribution[-1]))
        )]
    ]

    heterogeneous = (False, ) * len(base_cog) + (True,)

    cognitive_parameters = base_cog + heterogeneous_cog

    print(f'Treating {n_batch} batchs.')

    for i in range(n_sim):

        param = {
            'cognitive_parameters': cognitive_parameters[i],
            'seed': seeds[i],
            't_max': t_max,
            'economy_model': economy_model,
            'agent_model': agent_model,
            'n_good': n_good,
            'distribution': distribution[i],
            'heterogeneous': heterogeneous[i],
            'room_id': i,
        }

        parameters.append(param)

    return parameters


def _produce_data():

    params = _get_parameters()

    data = backup.structure.Data()

    for pr in params:
        pr, b = _run(pr)
        data.append(bkp=b, param=pr)

    return data


def _run_batches(n_batch=20):

    data = []

    for _ in tqdm(range(n_batch)):

        d = _produce_data()
        data.append(d)

    return data


def analyse(data):

    for m in range(3):

        n_batch = len(data)

        y = [[] for _ in range(n_batch)]

        for i, b in enumerate(data):

            n_sim = len(b.medium)

            for j in range(n_sim):

                mean, e = analysis.tools.format.exp_monetary_bhv_bar_plot(monetary_bhv=b.monetary_bhv[j])
                y[i].append(mean[m])

        y = np.asarray(y).transpose()

        analysis.graph.supplementary.box_plot(y, f_name=f"fig/supplementary{m}.pdf")


def main(force=False):

    f_name = 'data/supplementary.p'

    if os.path.exists(f_name) and not force:

        with open(f_name, 'rb') as f:
            b = pickle.load(f)

    else:

        b = _run_batches()
        with open(f_name, 'wb') as f:

            pickle.dump(b, f)

    analyse(b)
