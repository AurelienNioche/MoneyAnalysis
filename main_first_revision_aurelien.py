import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MoneyAnalysis.settings")

# Ensure settings are read
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

import string

import numpy as np
import matplotlib.pyplot as plt

import analysis.first_revision_aurelien
import analysis.first_revision_basile
import analysis.supplementary
import analysis.metric.metric
import analysis.stats.stats

import simulation.run_based_on_fit
import simulation.run_xp_like

import xp.xp


import graph.sim_and_xp
import graph.phase_diagram
import graph.supplementary.individual_behavior
import graph.supplementary.age
import graph.supplementary.gender
import graph.supplementary.sensitivity_analysis
import graph.supplementary.parameter_recovery
import graph.exploratory.learning_curves
import graph.exploratory.cross_validation
from graph.parameters import FIG_FOLDER, SUP_FIG_FOLDER
from graph.labelling import agent_labeling
import graph.exploratory.learning_curves

from simulation.model.RL.asymmetric_rl_agent import RLAgentAsymmetric
from simulation.model.RL.rl_no_alpha_no_beta \
    import RLNoAlphaNoBeta, RLNoAlphaNoBetaV2
from simulation.model.RL.rl_hyperbolic_discounting \
    import RLHyperbolicDiscounting
from simulation.model.RL.rl_exponential_discounting \
    import RLExponentialDiscounting
from simulation.model.RL.rl_softmax import RLSoftmax
from simulation.model.RL.rl_agent import RLAgent

import analysis.main
import simulation.run_first_revision
import analysis.fit.data

from backup import backup

from graph.sim_and_xp import boxplot
import scipy.stats

import statsmodels.stats.multitest

import simulation.run_asymmetric_learning


def revision_phase_diagram():

    """
    plot phase diagram with other agent models
    """
    agent_models = (
        RLNoAlphaNoBetaV2,
        RLAgentAsymmetric,
        RLNoAlphaNoBeta,
        RLHyperbolicDiscounting,
        RLExponentialDiscounting,
        RLSoftmax,
    )

    for agent_model in agent_models:

        f_name = f'phase_{agent_model.__name__}.pdf'

        print(f'Producing data for model "{agent_model.__name__}"...')

        data, labels = analysis.first_revision_aurelien.phase_diagram(
            agent_model=agent_model)

        graph.phase_diagram.plot(data=data, labels=labels, f_name=f_name)


def phase_diagram_n_good():
    data_path = os.path.join("data", "phase_diagram_n_good.p")
    if os.path.exists(data_path):
        (data, labels) = backup.load(data_path)
    else:
        data = {}

        for n_good in (5, 6):
            d = \
                simulation.run_first_revision.get_data(
                    n_good=n_good,
                    agent_model=RLAgent)
            data_f, labels = analysis.main.format_for_phase_diagram(d=d, m=0)

            data[n_good] = data_f
        backup.save((data, labels), data_path)

    graph.phase_diagram.plot(
        data=data, labels=labels,
        f_name=f'phase_diagram_more_good.pdf')


def fit():

    agent_models = (
        RLNoAlphaNoBetaV2,
        RLAgent,
        RLAgentAsymmetric,
        RLNoAlphaNoBeta,
        RLHyperbolicDiscounting,
        RLExponentialDiscounting,
        RLSoftmax,
    )

    results = {}

    for agent_model in agent_models:

        best_parameters, mean_p, lls, bic, eco = \
            analysis.fit.data.get(model=agent_model, verbose=False)

        print("-" * 20)
        print(f"{agent_model.__name__}: {np.mean(bic)}(+/-{np.std(bic)}STD)")
        print("-" * 20)
        print()

        results[agent_model.__name__] = bic

        boxplot(results=best_parameters,
                y_label="best-fit value",
                f_name=f'best_parameters_{agent_model.__name__}.pdf',
                y_lim=None,
                aspect=None)
        if agent_model.__name__ == 'RLAgentAsymmetric':
            d1, d2 = best_parameters["alpha_minus"], \
                     best_parameters["alpha_plus"]
            u, p = scipy.stats.mannwhitneyu(d1, d2)
            print(f"Comparison alpha - and alpha +: u={u:.1f}, p={p:.3f}")
            print("")
            print("")

    boxplot(results=results, y_label="BIC", f_name='bic.pdf', y_lim=None,
            aspect=None)

    # f, p = scipy.stats.f_oneway(*results.values())
    # print(f, p)

    ns = []

    ps = []
    us = []

    keys = []

    for key in sorted(results.keys()):
        for second_key in sorted(results.keys()):
            if key != second_key:
                d1 = results[key]
                d2 = results[second_key]
                u, p = scipy.stats.mannwhitneyu(d1, d2)
                n = len(d1) + len(d2)
                ps.append(p)
                us.append(u)
                ns.append(n)
                keys.append((key, second_key))

    valid, p_corr, alpha_c_sidak, alpha_c_bonf = \
        statsmodels.stats.multitest.multipletests(pvals=ps, alpha=0.05,
                                                  method="b")

    for i in range(len(ns)):
        print(f'{keys[i]}: p={ps[i]:.3f}, p_cor={p_corr[i]:.3f}, '
              f'valid={valid[i]}')


def asymmetric_learning():

    data, labels = simulation.run_asymmetric_learning.phase_diagram(
        force=False
    )
    graph.phase_diagram.plot(
        data=data, labels=labels,
        f_name=f'phase_diagram_asymmetric.pdf',
        x_label='alpha_plus',
        y_label='alpha_minus',
        ticks_index=[0, 5, 9],
    )


def main_sim_and_xp():

    alpha, beta, gamma = .175, 1, .125
    model = RLAgent
    heterogeneous = True
    m = 0

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
                d_formatted = \
                    analysis.metric.metric.dynamic_data(data_xp_session=d)

                agent_types = d_formatted.keys()

                for agent_type in sorted(agent_types):
                    if agent_type not in fig_data[n_good][cat].keys():
                        fig_data[n_good][cat][agent_type] = {}

                    fig_data[n_good][cat][agent_type][cond] = \
                        d_formatted[agent_type]

                t_max = d.t_max

                prod = d.prod
                cons = d.cons
                desired = d.desired
                in_hand = d.in_hand
                #
                # n_good = d.n_good
                #
                # # Potential users of m
                agent_types = tuple(range(2, n_good))  # 2: prod + cons of m
                #
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

                    for i, agent_idx in enumerate(agents):

                        _, ex, n = analysis.metric.metric.exchange(
                            n_good=n_good,
                            prod=prod[agent_idx],
                            cons=cons[agent_idx],
                            desired=desired[agent_idx],
                            in_hand=in_hand[agent_idx],
                            m=m
                        )

                        window = int(t_max/3)
                        for t in range(t_max):

                            sup = t
                            inf = max(-1, sup - window)

                            # Number of attempts
                            begin_n = n[inf] if inf != -1 else 0
                            last_n = n[sup]

                            diff_n = last_n-begin_n

                            assert diff_n >= 0

                            begin_ex = ex[inf] if inf != -1 else 0
                            last_ex = ex[sup]

                            diff_ex = last_ex - begin_ex

                            assert diff_ex >= 0

                            assert diff_ex <= diff_n

                            # print("Idx", i)
                            # print("t", t)
                            # print("inf", inf)
                            # print("sup", sup)
                            # print("diff n", diff_n)
                            # print("diff ex", diff_ex)
                            if diff_n > 0:
                                st = diff_ex / diff_n
                            else:
                                st = np.nan
                            ind_matrix[i, t] = st

                        # print(ind_matrix[i, :])
                        plt.plot(range(t_max), ind_matrix[i, :])
                        plt.show()
                        # raise Exception

                    for t in range(t_max):

                        x_t = ind_matrix[:, t]

                        p_choices_mean[at][t] = np.nanmean(x_t)
                        p_choices_sem[at][t] = 0 #scipy.stats.sem(x_t, nan_policy='omit')
                        p_choices_std[at][t] = np.nanstd(x_t)

                        q1, med, q3 = np.nanpercentile(x_t, [25, 50, 75])
                        p_choices_median[at][t] = med
                        p_choices_q1[at][t] = q1
                        p_choices_q3[at][t] = q3

                    if at not in learning_curve_data[n_good][cat].keys():
                        learning_curve_data[n_good][cat][at] = {}

                    dic = {
                            'mean': p_choices_mean[at],
                            'sem': p_choices_sem[at],
                            'std': p_choices_std[at],
                            'median': p_choices_median[at],
                            'q1': p_choices_q1[at],
                            'q3': p_choices_q3[at]
                        }

                    learning_curve_data[n_good][cat][at][cond] = dic

    for n_good in room_n_good:

        n_rows = len(category)

        n_cols = (n_good - 2) * 2

        fig, axes = plt.subplots(
            figsize=(3.5*n_cols, 4 * n_rows), ncols=n_cols, nrows=n_rows)

        n = 0

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

                # # if n_good == 3:
                # #     chance_level = 0.5
                # #     y_ticks = [0, 0.5, 1]
                # # elif n_good == 4:
                # #     chance_level = 0.33
                # #     y_ticks = [0, 0.33, 0.66, 1]
                # # else:
                # #     raise NotImplementedError
                #
                # ax = fig.add_subplot(gs[row, col])
                #

                fig_d = learning_curve_data[n_good][cat][at]

                # exchange_type = fig_d.get('exchange_type')
                # use_std = True
                ylabel = 'Freq. ind. ex. with good 1'

                for cond in fig_d.keys():

                    d = fig_d[cond]

                    # x = fig_d[cond]['mean']
                    # if use_std:
                    #     dsp = fig_d[cond]['std']
                    # else:
                    #     dsp = fig_d[cond]['sem']

                    graph.exploratory.learning_curves.curve(
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
                # if exchange_type is not None:
                #     for ex_t in exchange_type:
                #         x = fig_d['mean'][ex_t]
                #
                #         if use_std:
                #             dsp = fig_d['std'][ex_t]
                #         else:
                #             dsp = fig_d['sem'][ex_t]
                #
                #         graph.exploratory.learning_curves.curve(x, dsp,
                #               n_good=n_good, cond=cat, agent_type=at,
                #               ax=ax, ylabel=ylabel, legend=str(ex_t))
                #         ax.legend()
                #
                # else:


                # ----------------------------- #
                n += 1

        plt.tight_layout()

        f_name = f'xp_{n_good}.pdf'
        f_path = os.path.join(SUP_FIG_FOLDER, f_name)
        plt.savefig(f_path)
        print(f'{f_name} created.')

    # graph.sim_and_xp.plot(fig_data)
    analysis.stats.stats.sim_and_xp(fig_data)


if __name__ == '__main__':

    main_sim_and_xp()
