import os

from backup import backup


class Data:

    def __init__(self):

        self.medium = []
        self.monetary_bhv = []

        self.distribution = []
        self.cognitive_parameters = []

        self.n_good = []
        self.room_id = []
        self.seed = []

        # self.medium_over_agents = np.zeros(n, dtype=object)
        # self.constant_x_value = np.zeros(n, dtype=object)
        # self.constant_x_index = np.zeros(n, dtype=object)
        # self.agent_model = np.zeros(n, dtype=object)
        # self.economy_model = np.zeros(n, dtype=object)
        # self.medium_over_time = np.zeros(n, dtype=object)

    def append(self, bkp, param):

        self.medium.append(bkp['medium'])  # n_good, agent, time

        self.monetary_bhv.append(bkp['monetary_bhv'])  # n_good, agent, time
        self.n_good.append(param['n_good'])

        self.distribution.append(param['distribution'])
        self.cognitive_parameters.append(param['cognitive_parameters'])

        self.seed.append(param['seed'])

        # self.medium_over_time.append(backup['medium_over_time']   # n_good, time

        # self.agent_model.append(param['agent_model']
        # self.economy_model.append(param['economy_model']

        # if param.get('constant_x_value') is not None:
        #     self.constant_x_value.append(param['constant_x_value']
        #
        # if param.get('constant_x_index') is not None:
        #     self.constant_x_index.append(param['constant_x_index']

        if param.get('room_id') is not None:
            self.room_id.append(param['room_id'])

    def _files_mapping(self, data_folder):

        return {f'{data_folder}/{v}.p': v for v in vars(self) if not v.startswith("_")}

    def save(self, data_folder):

        os.makedirs(data_folder, exist_ok=True)

        for k, v in self._files_mapping(data_folder).items():
            backup.save(obj=getattr(self, v), file_name=k)

    def load(self, data_folder):

        for k, v in self._files_mapping(data_folder).items():
            setattr(self, v, backup.load(file_name=k))
