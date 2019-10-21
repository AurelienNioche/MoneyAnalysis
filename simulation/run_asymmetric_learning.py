import itertools

import numpy as np
import os


import backup.backup
import backup.structure

from simulation.model.RL.asymmetric_rl_agent import RLAsymmetric
from simulation.run import Run

import analysis.metric.metric as metric

DATA_FOLDER = "data"


class RunAsymmetric(Run):

    t_max = 100
    economy_model = 'prod: i-1'
    n_cog_value_alpha = 10
    n_cog_value = 3

    assert economy_model in ('prod: i-1', 'prod: i+1'), \
        'Bad argument for "economy_model"!'

    # noinspection PyMethodOverriding
    @classmethod
    def _get_phase_parameters(cls, n_good):

        ranges = []

        bounds_alpha = {}
        for key in 'alpha_minus', "alpha_plus":
            bounds_alpha[key] = RLAsymmetric.fit_bounds[
                [b[0] for b in RLAsymmetric.fit_bounds].index(key)
            ]
        for b in RLAsymmetric.bounds:
            if "alpha" in b[0]:
                r = np.linspace(
                    bounds_alpha[b[0]][1],
                    bounds_alpha[b[0]][2],
                    cls.n_cog_value_alpha)
            else:
                r = np.linspace(b[1], b[2], cls.n_cog_value)

            ranges.append(r)
        # ------------------------------ #

        repartition = np.array([50, ] * 2 + [100, ] * (n_good-2))

        # ---------- #

        var_param = itertools.product(*ranges)

        # ----------- #

        parameters = []

        for v in var_param:

            cog_param = v

            complete_dist = np.zeros(n_good, dtype=int)
            complete_dist[:] = repartition

            param = {
                'cognitive_parameters': cog_param,
                'distribution': complete_dist,
                't_max': cls.t_max,
                'economy_model': cls.economy_model,
                'agent_model': RLAsymmetric.__name__,
                'seed': np.random.randint(2**32-1)
            }
            parameters.append(param)

        return parameters

    # noinspection PyMethodOverriding
    def get_data(self, n_good, force=False, fake=False):

        data_folder = os.path.join(
            'data',
            f'phase_{n_good}_goods_asymmetric')

        params = \
            self._get_phase_parameters(n_good=n_good)

        if fake:
            self._produce_data(params=params, fake=True)
            return None

        elif force or not os.path.exists(data_folder):

            bkp = self._produce_data(params=params)
            bkp.save(data_folder)

        else:
            bkp = backup.structure.Data()
            bkp.load(data_folder)

        return bkp


def get_data(**kwargs):

    return RunAsymmetric().get_data(**kwargs)


def format_for_phase_diagram(d, m):

    idx_alpha_minus = [b[0] for b in
                       RLAsymmetric.bounds].index("alpha_minus")
    idx_alpha_plus = [b[0] for b in
                      RLAsymmetric.bounds].index("alpha_plus")

    observation = metric.get_multi_eco_statistic(in_hand=d.in_hand,
                                                 desired=d.desired,
                                                 prod=d.prod,
                                                 cons=d.cons,
                                                 m=m)

    alpha_minus = np.array(
        [pr[idx_alpha_minus] for pr in d.cognitive_parameters])
    alpha_plus = np.array(
        [pr[idx_alpha_plus] for pr in d.cognitive_parameters])

    unq_alpha_minus = np.unique(alpha_minus)
    unq_alpha_minus.sort()

    unq_alpha_plus = np.unique(alpha_plus)
    unq_alpha_plus.sort()

    assert np.all(unq_alpha_minus == unq_alpha_plus)

    labels = unq_alpha_minus

    n_side = len(labels)

    scores = np.zeros((n_side, n_side))

    for i in range(n_side):
        for j in range(n_side):
            good_alpha_minus = alpha_minus == unq_alpha_minus[i]
            good_alpha_plus = alpha_plus == unq_alpha_plus[j]
            to_select = good_alpha_minus*good_alpha_plus
            scores[i, j] = np.mean(observation[to_select])

    return scores, labels


def phase_diagram(m=0, force=False):

    data_file = f'{DATA_FOLDER}/phase_diagram_asymmetric.p'

    if os.path.exists(data_file) and not force:
        data, labels = backup.backup.load(data_file)
        return data, labels

    data = {}

    for n_good in (4, 3):

        d = get_data(n_good=n_good, force=force)

        formatted_d, labels = format_for_phase_diagram(d, m)

        data[n_good] = formatted_d

    backup.backup.save((data, labels), data_file)

    return data, labels
