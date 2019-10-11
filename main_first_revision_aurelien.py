import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MoneyAnalysis.settings")

# Ensure settings are read
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

import numpy as np

import analysis.first_revision_aurelien
import analysis.first_revision_basile


import graph.sim_and_xp
import graph.phase_diagram
import graph.supplementary.individual_behavior
import graph.supplementary.age
import graph.supplementary.gender
import graph.supplementary.sensitivity_analysis
import graph.supplementary.parameter_recovery
import graph.exploratory.learning_curves
import graph.exploratory.cross_validation

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


if __name__ == '__main__':

    asymmetric_learning()
