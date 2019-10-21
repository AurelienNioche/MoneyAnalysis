import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MoneyAnalysis.settings")

# Ensure settings are read
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

import numpy as np
import inspect

import simulation.run_based_on_fit
import simulation.run_xp_like
from simulation.model.RL.rl_agent import RLAgent

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

from backup import backup

import xp.xp


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
            xp_data=data['Human'],
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
def sup_post_hoc():

    bkp_file = "data/sup_post_hoc.p"
    os.makedirs(os.path.dirname(bkp_file), exist_ok=True)

    if os.path.exists(bkp_file):
        (data, room_n_good, room_uniform) = backup.load(file_name=bkp_file)

    else:

        t_max = 10000

        model = RLAgent
        heterogeneous = True

        data_human, room_n_good, room_uniform = xp.xp.get_data()

        data = {}

        best_parameters, mean_p, lls, bic, eco = \
            analysis.fit.data.get(model=model)

        data["Post-Hoc Sim. Extended"] = simulation.run_based_on_fit.get_data(
            xp_data_list=data_human,
            best_parameters=best_parameters,
            eco=eco,
            heterogeneous=heterogeneous,
            t_max=t_max,
        )

        data["Post-Hoc Sim. Non-Het."] = simulation.run_based_on_fit.get_data(
            xp_data_list=data_human,
            best_parameters=best_parameters,
            eco=eco,
            heterogeneous=False)

        backup.save(obj=(data, room_n_good, room_uniform), file_name=bkp_file)

    category = ["Post-Hoc Sim. Non-Het.", "Post-Hoc Sim. Extended"]
    assert np.all([i in data.keys() for i in category])

    fig_sim_xp_post(
        room_n_good=room_n_good,
        room_uniform=room_uniform,
        category=category,
        data=data,
        fig_ind=False,
        stats=False,
        fig_folder="fig/sup",
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

    phase_diagram()
    main_sim_and_xp()
    sup_post_hoc()
    fig_bic()
    sup_sensitivity_analysis()
    sup_age()
    sup_gender()
