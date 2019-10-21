# import string

import numpy as np
# import matplotlib.pyplot as plt

# import analysis.first_revision_aurelien
# import analysis.first_revision_basile
import analysis.supplementary
import analysis.metric.metric
import analysis.stats.stats


from simulation.model.RL.asymmetric_rl_agent import RLAgentAsymmetric
from simulation.model.RL.rl_no_alpha_no_beta \
    import RLNoAlphaNoBeta, RLNoAlphaNoBetaV2
from simulation.model.RL.rl_hyperbolic_discounting \
    import RLHyperbolicDiscounting
from simulation.model.RL.rl_exponential_discounting \
    import RLExponentialDiscounting
from simulation.model.RL.rl_softmax import RLSoftmax
from simulation.model.RL.rl_agent import RLAgent

import analysis.fit.data

from graph.boxplot import boxplot
import scipy.stats

import statsmodels.stats.multitest


def fig_bic(fig_folder='fig/sup'):

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
                y_lim=None,
                aspect=None,
                fig_name=f'best_parameters_{agent_model.__name__}.pdf',
                fig_folder=fig_folder
                )
        if agent_model.__name__ == 'RLAgentAsymmetric':
            d1, d2 = best_parameters["alpha_minus"], \
                     best_parameters["alpha_plus"]
            u, p = scipy.stats.mannwhitneyu(d1, d2)
            print(f"Comparison alpha - and alpha +: u={u:.1f}, p={p:.3f}")
            print("")
            print("")

    boxplot(results=results,
            y_label="BIC",
            y_lim=None,
            aspect=None,
            fig_name='bic.pdf',
            fig_folder=fig_folder)

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