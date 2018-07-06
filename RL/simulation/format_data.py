import os
import pickle
import numpy as np

import RL.optimize


def run():

    f_name = 'data/fit.p'

    if os.path.exists(f_name):

        data = pickle.load(open(f_name, 'rb'))

    else:

        print(
            'data/fit.p does not exist, I am going to run RL.optimize.py\
             in order to produce the required data'
        )

        data = RL.optimize.run(f_name)

    return format_data(data)


def format_data(data):

    # Input data structure
    #  data = {
    #  '<economy_label>': {'<parameter>': np.array with size n_user
    #                       ...
    #}

    # output data structure
    #  np.array([np.array([<param1>, <param2>, <param3>]) * n_user])

    # total_user = np.sum([len(data[k]['alpha']) for k, v in data.items()])

    formatted_data = {}

    for k, v in data.items():

        # assert len(v['alpha']) == len(v['beta']) == len(v['gamma'])

        # for j in range(len(v['alpha'])):
        #
        #     users[i] = np.array(
        #
        #         [v['alpha'][j], v['beta'][j], v['gamma'][j]]
        #     )
        #
        #     i += 1

        n = len(v['alpha'])
        room_data = np.zeros((n, len(v)))

        for i in range(n):
            # for param_label, param_value in v.items():

            room_data[i] = v["alpha"][i], v["beta"][i], v["gamma"][i]

        formatted_data[k] = room_data

    return formatted_data














