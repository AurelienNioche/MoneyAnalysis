import os

from backup import backup


class Data:

    def __init__(self):

        self.in_hand = []
        self.desired = []
        self.prod = []
        self.cons = []
        self.acceptance = []

        self.distribution = []
        self.cognitive_parameters = []

        self.n_good = []
        self.room_id = []
        self.seed = []

    def append(self, bkp, param):

        self.in_hand.append(bkp['in_hand'])
        self.desired.append(bkp['desired'])
        self.prod.append(bkp['prod'])
        self.cons.append(bkp['cons'])
        self.n_good.append(bkp['n_good'])
        self.acceptance.append(bkp['acceptance'])

        self.distribution.append(param['distribution'])
        self.cognitive_parameters.append(param['cognitive_parameters'])
        self.seed.append(param['seed'])

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


class DataXPSession:

    def __init__(self, in_hand, desired, prod, cons, n_good, t_max,
                 acceptance=None,
                 success=None, gender=None, age=None):

        self.age = age
        self.gender = gender

        self.in_hand = in_hand
        self.desired = desired
        self.success = success

        self.acceptance = acceptance

        self.prod = prod
        self.cons = cons

        self.n_good = n_good
        self.t_max = t_max
