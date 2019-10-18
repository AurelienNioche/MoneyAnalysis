import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MoneyAnalysis.settings")

# Ensure settings are read
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()


def phase_diagram():

    from analysis.fig_phase_diagram import all_phase_diagram
    all_phase_diagram()


def fig_bic():

    from analysis.fig_bic import fig_bic
    fig_bic()


def main_sim_and_xp():

    from analysis.fig_sim_xp_post import fig_sim_xp_post
    from analysis.fig_sim_xp_post import _fig
    import analysis.fit.data

    import simulation.run_based_on_fit
    import simulation.run_xp_like
    import numpy as np

    from simulation.model.RL.rl_agent import RLAgent
    import analysis.metric.metric

    import scipy.stats

    import xp.xp

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

    # --------------- #

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


if __name__ == '__main__':

    # fig_bic()
    main_sim_and_xp()
    # phase_diagram()
