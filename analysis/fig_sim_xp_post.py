import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MoneyAnalysis.settings")

# Ensure settings are read
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

import string

import numpy as np
import matplotlib.pyplot as plt

# import analysis.first_revision_aurelien
# import analysis.first_revision_basile
import analysis.supplementary
import analysis.metric.metric
import analysis.stats.stats

import simulation.run_based_on_fit
import simulation.run_xp_like

import xp.xp


import graph.boxplot
import graph.phase_diagram
# import graph.supplementary.individual_behavior
# import graph.supplementary.age
# import graph.supplementary.gender
# import graph.supplementary.sensitivity_analysis
# import graph.supplementary.parameter_recovery
import graph.learning_curves


from graph.labelling import agent_labeling
import graph.learning_curves
from graph.boxplot import boxplot

from simulation.model.RL.rl_agent import RLAgent


import simulation.run
import analysis.fit.data

import scipy.stats

import simulation.run_asymmetric_learning

from graph.utils import save_fig


def _fig(room_n_good, category, fig_data, learning_curve_data):

    for n_good in room_n_good:

        n_rows = len(category)

        n_cols = (n_good - 2) * 2

        fig, axes = plt.subplots(
            figsize=(3.5 * n_cols, 4 * n_rows), ncols=n_cols, nrows=n_rows)

        for row, cat in enumerate(category):

            agent_types = sorted(fig_data[n_good][cat].keys())

            col = 0

            for at in agent_types:

                if n_rows == 1:
                    print("Unique row")
                    ax = axes[col]
                elif n_cols == 1:
                    print("Unique column")
                    ax = axes[row]
                else:
                    ax = axes[row, col]

                al = agent_labeling(n_good)

                at_label = al[at]
                cat_label = cat

                title = f'{cat_label} - Type {at_label}'
                ylabel = 'Freq. ind. ex. with good 1'

                fig_d = learning_curve_data[n_good][cat][at]

                for cond in fig_d.keys():
                    d = fig_d[cond]

                    # x = fig_d[cond]['mean']
                    # if use_std:
                    #     dsp = fig_d[cond]['std']
                    # else:
                    #     dsp = fig_d[cond]['sem']

                    graph.learning_curves.curve(
                        n_good=n_good, cond=cat, agent_type=at,
                        ax=ax, ylabel=ylabel,
                        q1=d['q1'], q3=d['q3'], median=d['median'],
                        title=title
                    )

                # Add letter
                if col == 0:
                    ax.text(-0.2, 1.2, string.ascii_uppercase[row],
                            transform=ax.transAxes,
                            size=20, weight='bold')

                col += 1

                if n_rows == 1:
                    print("Unique row")
                    ax = axes[col]
                elif n_cols == 1:
                    print("Unique column")
                    ax = axes[row]
                else:
                    ax = axes[row, col]

                results = fig_data[n_good][cat][at]

                chance_level = 1 / (n_good - 1)
                y_ticks = np.linspace(0, 1, n_good)

                boxplot(results=results,
                        chance_level=chance_level,
                        y_ticks=y_ticks,
                        ax=ax,
                        title=title,
                        y_label=ylabel,
                        colors=('C0', 'C1'))

                col += 1

        plt.tight_layout()

        fig_name = f'xp_{n_good}.pdf'
        save_fig(fig_name=fig_name, fig_folder=fig_folder)


def fig_sim_xp_post(fig_folder="main"):

    alpha, beta, gamma = .175, 1, .125
    model = RLAgent
    heterogeneous = True
    m = 0
    learning_window = 25
    boxplot_window = 50

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
    n_good_cond = np.unique(room_n_good)
    cond_labels = "Uniform", "Non-uniform"

    fig_data = {
        n_good: {
            cat: {} for cat in category
        } for n_good in n_good_cond
    }

    learning_curve_data = {
        n_good: {
            cat: {} for cat in category
        } for n_good in n_good_cond
    }

    ind_learning_curve_data = {
        n_good: {
            cat: {} for cat in category
        } for n_good in n_good_cond
    }

    for n_good in room_n_good:

        for uniform in True, False:

            # Find the good indexes
            cond_n_good = room_n_good == n_good
            cond_uniform = room_uniform == uniform

            xp_cond = cond_n_good * cond_uniform
            assert (np.sum(xp_cond) == 1)
            d_idx = np.where(xp_cond == 1)[0][0]

            cond = cond_labels[int(uniform)]

            for cat in category:

                # Get formatted data
                d = data[cat][d_idx]

                t_max = d.t_max

                prod = d.prod
                cons = d.cons
                desired = d.desired
                in_hand = d.in_hand
                # n_good = d.n_good

                # # Potential users of m
                agent_types = tuple(range(2, n_good))  # 2: prod + cons of m

                p_choices_mean = {at: np.zeros(t_max) for at in agent_types}
                p_choices_sem = {at: np.zeros(t_max) for at in agent_types}
                p_choices_std = {at: np.zeros(t_max) for at in agent_types}
                p_choices_median = {at: np.zeros(t_max) for at in agent_types}
                p_choices_q1 = {at: np.zeros(t_max) for at in agent_types}
                p_choices_q3 = {at: np.zeros(t_max) for at in agent_types}

                for at in agent_types:

                    agents = np.arange(len(cons))[cons == at]
                    n_agent = len(agents)

                    ind_matrix = np.zeros((n_agent, t_max))

                    boxplot_data = np.zeros(n_agent)

                    for i, agent_idx in enumerate(agents):

                        _, ex, n = analysis.metric.metric.exchange(
                            n_good=n_good,
                            prod=prod[agent_idx],
                            cons=cons[agent_idx],
                            desired=desired[agent_idx],
                            in_hand=in_hand[agent_idx],
                            m=m
                        )

                        for t in range(t_max):
                            ind_matrix[i, t] = \
                                analysis.metric.metric.statistic(
                                    ex=ex, n=n, t=t, window=learning_window
                                )

                        boxplot_data[i] = \
                            analysis.metric.metric.statistic(
                                ex=ex, n=n, t=t_max - 1, window=boxplot_window
                            )

                    if at not in fig_data[n_good][cat].keys():
                        fig_data[n_good][cat][at] = {}

                    fig_data[n_good][cat][at][cond] = \
                        boxplot_data

                    for t in range(t_max):
                        x_t = ind_matrix[:, t]

                        p_choices_mean[at][t] = np.mean(x_t)
                        p_choices_sem[at][t] = scipy.stats.sem(x_t)
                        p_choices_std[at][t] = np.std(x_t)

                        q1, med, q3 = np.nanpercentile(x_t, [25, 50, 75])
                        p_choices_median[at][t] = med
                        p_choices_q1[at][t] = q1
                        p_choices_q3[at][t] = q3

                    if at not in learning_curve_data[n_good][cat].keys():
                        learning_curve_data[n_good][cat][at] = {}

                    if at not in ind_learning_curve_data[n_good][cat].keys():
                        ind_learning_curve_data[n_good][cat][at] = \
                            ind_matrix

                    dic = {
                        'mean': p_choices_mean[at],
                        'sem': p_choices_sem[at],
                        'std': p_choices_std[at],
                        'median': p_choices_median[at],
                        'q1': p_choices_q1[at],
                        'q3': p_choices_q3[at]
                    }

                    learning_curve_data[n_good][cat][at][cond] = dic

    # for n_good in room_n_good:
    #     for cat in category:
    #         agent_types = fig_data[n_good][cat].keys()
    #         for at in agent_types:
    #             u, p = scipy.stats.mannwhitneyu(
    #                 *fig_data[n_good][cat][at].values())
    #             print(f"G={n_good}; cat={cat}; at={at}")
    #             print(f"u={u}; p={p} {'*' if p <= 0.05 else ''}")
    #             print()

    _fig(room_n_good=room_n_good, category=category,
         fig_data=fig_data, learning_curve_data=learning_curve_data)

    # graph.sim_and_xp.plot(fig_data)
    analysis.stats.stats.sim_and_xp(fig_data)