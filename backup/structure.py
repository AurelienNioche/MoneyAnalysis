import numpy as np


class Data:

    def __init__(self, n):

        self.medium = np.zeros(n, dtype=object)
        self.monetary_bhv = np.zeros(n, dtype=object)

        self.repartition = np.zeros(n, dtype=object)
        self.cognitive_parameters = np.zeros(n, dtype=object)
        self.agent_model = np.zeros(n, dtype=object)
        # self.m = np.zeros(n, dtype=object)
        self.economy_model = np.zeros(n, dtype=object)
        self.constant_x_value = np.zeros(n, dtype=object)
        self.constant_x_index = np.zeros(n, dtype=object)
        self.n_good = np.zeros(n, dtype=object)
        self.room_id = np.zeros(n, dtype=object)

        self.i = 0

    def append(self, backup, param):

        self.medium[self.i] = backup['medium']
        self.monetary_bhv[self.i] = backup['monetary_bhv']
        self.n_good[self.i] = param['n_good']

        self.repartition[self.i] = param['repartition']
        self.cognitive_parameters[self.i] = param['cognitive_parameters']
        self.agent_model[self.i] = param['agent_model']
        # self.m[self.i] = param['m']
        self.economy_model[self.i] = param['economy_model']

        if param.get('constant_x_value') is not None:
            self.constant_x_value[self.i] = param['constant_x_value']

        if param.get('constant_x_index') is not None:
            self.constant_x_index[self.i] = param['constant_x_index']

        if param.get('room_id') is not None:
            self.room_id[self.i] = param['room_id']

        self.i += 1

