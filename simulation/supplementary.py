import multiprocessing
import os
import numpy as np
from tqdm import tqdm

import simulation.economy

import backup.structure

import analysis.tools.format
import analysis.stats.mean_comparison


def _run(param):

    e = simulation.economy.Economy(**param)
    return param, e.run()


def _get_parameters():

    parameters = []

    n_sim = 2
    n_good = 3
    t_max = 100
    economy_model = 'prod: i-1'
    agent_model = 'RLAgent'
    distribution = [
        (9, 9, 18),
        (9, 9, 18),
        (9, 9, 18)
    ]

    heterogeneous = (False, False, True)

    seeds = np.random.randint(2**32-1, size=n_sim)

    # print(np.asarray(distribution[-1]).shape)
    cognitive_parameters = [
        (0.1, 1.2, 0.1), (0.25, 0.8, 0.15),
        np.random.choice(
            [
                (0.1, 1.2, 0.1), (0.25, 0.8, 0.15)
            ],
            size=np.sum(np.asarray(distribution[-1]))
        )

        # (0.1, 1.0, 0.125),
        # (0.1, 1.0, 0.125), (0.1, 1.2, 0.1),
        # (0.175, 1.0, 0.15), (0.175, 1.0, 0.125), (0.25, 1.2, 0.125), (0.1, 1.2, 0.15), (0.25, 1.2, 0.125)
    ]

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

    max_ = len(params)

    data = backup.structure.Data()

    with multiprocessing.Pool(processes=os.cpu_count()) as p:

        with tqdm(total=max_) as pbar:
            for pr, b in p.imap_unordered(_run, params):
                data.append(bkp=b, param=pr)
                pbar.update()

    return data


def main():

    bkp = _produce_data()

    monetary_bhv = bkp.monetary_bhv

    # reformat each economies to compress on agents
    monetary_over_user = [
        analysis.tools.format.monetary_bhv_over_user(m)
        for m in monetary_bhv
    ]

    # Now we can do stats
    sig = [analysis.stats.mean_comparison.run(i) for i in monetary_over_user]
    # print(sig)
    results = [
        i[0][-1] < 0.05 and i[1][-1] < 0.05
        for i in sig
    ]
    print(results)
    print(bkp.room_id)


if __name__ == "__main__":

    main()
