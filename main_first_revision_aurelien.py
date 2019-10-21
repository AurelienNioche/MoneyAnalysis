import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MoneyAnalysis.settings")

# Ensure settings are read
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

import numpy as np

import simulation.run_based_on_fit
import simulation.run_xp_like
from simulation.model.RL.rl_agent import RLAgent
from simulation.model.RL.asymmetric_rl_agent import RLAsymmetric

import analysis.metric.metric
from analysis.fig_phase_diagram import all_phase_diagram
from analysis.fig_sim_xp_post import fig_sim_xp_post
import analysis.fit.data
import analysis.exploratory
import analysis.supplementary
from analysis.stats import stats


import graph.boxplot
import graph.phase_diagram
import graph.supplementary.age
import graph.supplementary.gender
import graph.supplementary.sensitivity_analysis
import graph.parameter_recovery
import graph.learning_curves
import graph.exploratory.cross_validation
from graph.labelling import agent_labeling

from backup import backup

import xp.xp

from analysis.stats.stats import mann_whitney


def print_info(func, ):

    def inner(*args, **kwargs):
        print("-" * 20)
        print(func.__name__.upper())
        print("-" * 20)
        func(*args, **kwargs)
        print()

    return inner


@print_info
def phase_diagram():
    all_phase_diagram()


@print_info
def fig_bic():

    from analysis.fig_bic import fig_bic
    fig_bic(fig_folder="fig/sup")


@print_info
def main_sim_and_xp():

    alpha, beta, gamma = .175, 1, .125
    model = RLAgent
    heterogeneous = True

    data = {}
    data["Human"], room_n_good, room_uniform = xp.xp.get_data()

    data['Simulation'] = \
        simulation.run_xp_like.get_data(
            agent_model=RLAgent,
            xp_data_list=data['Human'],
            alpha=alpha, beta=beta, gamma=gamma)

    best_parameters, mean_p, lls, bic, eco = \
        analysis.fit.data.get(model=model)

    data["Post-Hoc Sim."] = simulation.run_based_on_fit.get_data(
        xp_data_list=data["Human"],
        best_parameters=best_parameters,
        eco=eco,
        heterogeneous=heterogeneous)

    category = ["Simulation", "Human", "Post-Hoc Sim."]
    assert np.all([i in data.keys() for i in category])

    fig_sim_xp_post(
        room_n_good=room_n_good,
        room_uniform=room_uniform,
        category=category,
        data=data,
        fig_ind=True,
        stats=True,
        fig_folder="fig/main",
        m=0,
    )


@print_info
def sup_post_hoc(force=False):

    bkp_file = "data/sup_post_hoc.p"
    os.makedirs(os.path.dirname(bkp_file), exist_ok=True)

    if os.path.exists(bkp_file) and not force:
        (data, room_n_good, room_uniform) = backup.load(file_name=bkp_file)

    else:

        model = RLAgent

        data_human, room_n_good, room_uniform = xp.xp.get_data()

        data = {}

        best_parameters, mean_p, lls, bic, eco = \
            analysis.fit.data.get(model=model)

        data["Post-Hoc Sim. Extended"] = simulation.run_based_on_fit.get_data(
            xp_data_list=data_human,
            best_parameters=best_parameters,
            eco=eco,
            heterogeneous=True,
            t_max=1000,
        )

        data["Post-Hoc Sim. Non-Het."] = simulation.run_based_on_fit.get_data(
            xp_data_list=data_human,
            best_parameters=best_parameters,
            eco=eco,
            heterogeneous=False)

        backup.save(obj=(data, room_n_good, room_uniform), file_name=bkp_file)

    category = ["Post-Hoc Sim. Non-Het.", "Post-Hoc Sim. Extended"]
    assert np.all([i in data.keys() for i in category])

    fig_data = fig_sim_xp_post(
        room_n_good=room_n_good,
        room_uniform=room_uniform,
        category=category,
        data=data,
        fig_ind=False,
        stats=False,
        fig_folder="fig/sup",
        fig_extension="non_het_extended",
        m=0,
    )

    # fig_data: n_good: category: agent_type: condition
    for n_good in fig_data.keys():
        for cat in fig_data[n_good].keys():
            to_compare = []
            for agent_type in fig_data[n_good][cat].keys():
                to_compare.append(
                    {
                        "data":
                            [
                                fig_data[n_good][cat][agent_type][k] \
                                for k in fig_data[n_good][cat][agent_type].keys()
                        ],
                        "comparison":
                            f'Agent type dist. in artificial agents of type {agent_labeling(int(n_good))[agent_type]}',
                    }
                )

            mann_whitney(to_compare=to_compare,
                print_latex=True,
                measure='Ind. good 1',
                xp_label=f'{n_good}_{cat}'
    )


@print_info
def sup_asymmetric():

    bkp_file = "data/sup_asymmetric.p"
    os.makedirs(os.path.dirname(bkp_file), exist_ok=True)

    if os.path.exists(bkp_file):
        (data, room_n_good, room_uniform) = backup.load(file_name=bkp_file)

    else:

        alpha = .175
        gamma = .125
        beta = 1.

        factor = 0.66
        alpha_strong = alpha + factor * alpha
        alpha_weak = alpha - factor * alpha

        data_human, room_n_good, room_uniform = xp.xp.get_data()

        data = {}

        # Optimism bias
        data["Post-Hoc Sim. Opt. bias"] = simulation.run_xp_like.get_data(
            xp_data_list=data_human,
            agent_model=RLAsymmetric,
            alpha_minus=alpha_weak, alpha_plus=alpha_strong,
            beta=beta, gamma=gamma,
        )

        data["Post-Hoc Sim. Pess. Bias"] = simulation.run_xp_like.get_data(
            xp_data_list=data_human,
            agent_model=RLAsymmetric,
            alpha_minus=alpha_strong, alpha_plus=alpha_weak,
            beta=beta, gamma=gamma,)

        backup.save(obj=(data, room_n_good, room_uniform), file_name=bkp_file)

    category = ["Post-Hoc Sim. Opt. bias", "Post-Hoc Sim. Pess. Bias"]
    assert np.all([i in data.keys() for i in category])

    fig_sim_xp_post(
        room_n_good=room_n_good,
        room_uniform=room_uniform,
        category=category,
        data=data,
        fig_ind=False,
        stats=False,
        fig_folder="fig/sup",
        fig_extension="asymmetric",
        m=0,
    )


@print_info
def sup_sensitivity_analysis():

    data = analysis.supplementary.sensitivity_analysis()
    graph.supplementary.sensitivity_analysis.plot(data)
    stats.sensitivity_analysis(data)


@print_info
def sup_gender():

    print("-")

    data = analysis.supplementary.gender()
    graph.supplementary.gender.plot(data)
    analysis.stats.stats.supplementary_gender(data)


@print_info
def sup_age():

    print("-" * 10)
    print("SUP AGE")
    print("-" * 10)

    data = analysis.supplementary.age()
    graph.supplementary.age.plot(data)
    analysis.stats.stats.supplementary_age(data)


@print_info
def sup_parameter_recovery():

    print("-" * 10)
    print("SUP PARAMETER RECOVERY")
    print("-" * 10)

    fig_data = analysis.supplementary.parameter_recovery(model=RLAgent)
    graph.parameter_recovery.plot(fig_data)
    analysis.stats.stats.parameter_recovery(fig_data)

    print()


if __name__ == '__main__':

    sup_parameter_recovery()
    sup_post_hoc()
    sup_asymmetric()
    phase_diagram()
    main_sim_and_xp()
    fig_bic()
    sup_sensitivity_analysis()
    sup_age()
    sup_gender()
