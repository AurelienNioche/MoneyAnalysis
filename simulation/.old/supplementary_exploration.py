import multiprocessing
import os
import numpy as np
from tqdm import tqdm
import pickle

import simulation.economy

import backup.structure

import analysis.old.format
import analysis.stats.mean_comparison


def _run(param):

    e = simulation.economy.Economy(**param)
    return param, e.run()


def _get_parameters():

    parameters = []

    n_sim = 10
    n_good = 3
    t_max = 100
    economy_model = 'prod: i-1'
    agent_model = 'RLAgent'
    distribution = [
        (9, 9, 18) for _ in range(n_sim)
    ]

    seeds = np.random.randint(2**32-1, size=n_sim)

    base_cog = [
        (
            np.random.randint(1, 99) / 100,
            np.random.randint(60, 90) / 100,
            np.random.randint(8, 30) / 100
        ) for _ in range(n_sim - 1)
    ]

    # base_cog = [(0.54, 0.69, 0.27), (0.05, 0.73, 0.12), (0.45, 0.63, 0.11)]

    # base_cog = [
    #     [0.87, 0.65, 0.18],
    #     [0.01, 0.73, 0.11],
    #     [0.92, 0.64, 0.22]
    # ]

    heterogeneous_cog = [
        np.asarray(base_cog)
        [np.random.choice(
            range(len(base_cog)),
            size=np.sum(np.asarray(distribution[-1]))
        )]
    ]

    heterogeneous = (False, ) * len(base_cog) + (True,)

    print("*" * 10)
    print(base_cog)
    print("*" * 10)
    print(heterogeneous_cog)

    cognitive_parameters = base_cog + heterogeneous_cog

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

        print(param)

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

    f_name = 'data/supplementary.p'

    i = 0

    success = []
    max_success = 20

    while True:

        print("*" * 10, i, "*" * 10)

        bkp = _produce_data()

        monetary_bhv = bkp.monetary_bhv

        # reformat each economies to compress on agents
        monetary_over_user = [
            analysis.old.format.monetary_bhv_over_user(m)
            for m in monetary_bhv
        ]

        # Now we can do stats
        sig = [analysis.stats.mean_comparison.run(i) for i in monetary_over_user]
        # print(sig)
        results = np.asarray([
            i[0][-1] < 0.05 and i[1][-1] < 0.05
            for i in sig
        ])[np.asarray(bkp.room_id)]

        print(results)

        if np.sum(results[:-1]) == len(results) -1 and not results[-1]:
            success.append(bkp)

        if len(success) == max_success:
            with open(f_name, 'wb') as f:
                pickle.dump(success, f)

            break

        i += 1


if __name__ == "__main__":

    main()
