import os
import numpy as np

from simulation.model.RL.rl_agent import RLAgent

from backup import backup
from analysis.fit import fit
from xp import xp

# SCRIPT_FOLDER = os.path.dirname(os.path.abspath(__file__))
DATA_FOLDER = f'data'


class PProvider:

    def __init__(self, xp_data, agent_idx, model):

        self.xp_data = xp_data
        self.agent_idx = agent_idx
        self.model = model

    def get_p_choices(self, parameters):

        prod = self.xp_data.prod[self.agent_idx]
        cons = self.xp_data.cons[self.agent_idx]
        n_good = self.xp_data.n_good

        t_max = len(self.xp_data.in_hand[self.agent_idx])

        agent = self.model(
            prod=prod,
            cons=cons,
            n_goods=n_good,
            cognitive_parameters=parameters)

        p_choices = np.zeros(t_max)

        for t in range(t_max):

            in_hand = self.xp_data.in_hand[self.agent_idx, t]
            desired = self.xp_data.desired[self.agent_idx, t]
            success = self.xp_data.success[self.agent_idx, t]

            p = agent.p_choice(in_hand=in_hand, desired=desired)
            agent.learn_from_result(in_hand=in_hand, desired=desired,
                                    success=success)

            if p == 0:
                return None
            p_choices[t] = p

        return p_choices

    @staticmethod
    def model_name():
        return "RL"


def produce_fit(xp_data_list, room_n_good, room_uniform, model):

    bounds = model.fit_bounds

    best_parameters = {b[0]: [] for b in bounds}
    mean_p, lls, bic, eco = [], [], [], []

    eco_idx = 0

    for d, n_good, uniform in zip(xp_data_list, room_n_good, room_uniform):

        print(n_good, "UNIF:", uniform)
        for i in range(len(d.prod)):
            print("agent", i)

            p_provider = PProvider(xp_data=d, agent_idx=i, model=model)

            fitter = fit.Fit()
            best_param, mean_p_, lls_, bic_ = \
                fitter.evaluate(bounds=bounds,
                                p_provider=p_provider)

            for key in best_param:
                best_parameters[key].append(best_param[key])

            mean_p.append(mean_p_)
            lls.append(lls_)
            bic.append(bic_)
            eco.append(eco_idx)
            print("***")

        eco_idx += 1
        print("___\n")

    return best_parameters, mean_p, lls, bic, eco


def get(model,
        xp_data_list=None, room_n_good=None, room_uniform=None, extension=''):

    if xp_data_list is None:
        xp_data_list, room_n_good, room_uniform = xp.get_data()

    file_path = f'{DATA_FOLDER}/fit{extension}_{model.__name__}.p'

    if not os.path.exists(file_path):
        best_parameters, mean_p, lls, bic, eco = \
            produce_fit(
                model=model,
                xp_data_list=xp_data_list,
                room_n_good=room_n_good,
                room_uniform=room_uniform)
        backup.save(obj=(best_parameters, mean_p, lls, bic, eco),
                    file_name=file_path)

    else:
        best_parameters, mean_p, lls, bic, eco = \
            backup.load(file_name=file_path)

    return best_parameters, mean_p, lls, bic, eco
