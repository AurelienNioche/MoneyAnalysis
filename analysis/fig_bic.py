import numpy as np
import matplotlib.pyplot as plt
import string
import scipy.stats

from simulation.model.RL.asymmetric_rl_agent import RLAsymmetric
from simulation.model.RL.rl_no_alpha_no_beta \
    import RLNoAlphaNoBeta
from simulation.model.RL.rl_hyperbolic_discounting \
    import RLHyperbolicDiscounting
from simulation.model.RL.rl_exponential_discounting \
    import RLExponentialDiscounting
from simulation.model.RL.rl_softmax import RLSoftmax
from simulation.model.RL.rl_agent import RLAgent

import analysis.supplementary
import analysis.metric.metric
import analysis.stats.stats
import analysis.fit.data

from graph.boxplot import boxplot
from graph.utils import save_fig

import statsmodels.stats.multitest

import re


def _format_model_name(model):
    title = re.sub(r'([A-Z])', r' \1', model.__name__)
    title = title.replace("R L", "RL")
    return title


def fig_bic(fig_folder='fig/sup'):

    agent_models = [
        RLAgent,
        RLNoAlphaNoBeta,
        RLSoftmax,
        RLHyperbolicDiscounting,
        RLExponentialDiscounting,
        RLAsymmetric,
    ]

    results = {}

    best_parameters = {}

    for agent_model in agent_models:

        bp, mean_p, lls, bic, eco = \
            analysis.fit.data.get(model=agent_model, verbose=False)

        print("-" * 20)
        print(f"{agent_model.__name__}: {np.mean(bic):.2f}(+/-{np.std(bic):.2f}STD)")
        print(f"{_format_model_name(agent_model)} & "
              f"${np.mean(bic):.2f} \pm {np.std(bic):.2f} STD$ & "
              f"${len(agent_model.bounds)}$ & "
              f"${len(list(bp.values())[0])}$" + r"\\")
        print("-" * 20)
        print()

        results[agent_model.__name__] = bic

        best_parameters[agent_model.__name__] = bp

        if agent_model == RLAsymmetric:
            d1, d2 = bp["alpha_minus"], \
                     bp["alpha_plus"]
            u, p = scipy.stats.mannwhitneyu(d1, d2)
            print(f"Comparison alpha - and alpha +: u={u:.1f}, p={p:.3f}")
            print("")
            print("")

    n_cols = 3.5
    n_rows = 4

    fig, axes = plt.subplots(nrows=len(best_parameters),
                             figsize=(3 * n_cols, 3 * n_rows))

    for i, m in enumerate(agent_models):

        ax = axes[i]

        title = _format_model_name(m)

        boxplot(results=best_parameters[m.__name__],
                y_label="best-fit value",
                y_lim=None,
                aspect=None,
                ax=ax,
                dot_size=7.5
                )

        ax.set_title(title)

        # Add letter
        ax.text(-0.02, 1.1, string.ascii_uppercase[i],
                transform=ax.transAxes,
                size=20, weight='bold')

    plt.tight_layout()
    save_fig("best_fit_value.pdf", fig_folder=fig_folder)

    fig, ax = plt.subplots(figsize=(12, 3))
    boxplot(results=results,
            dot_size=17,
            y_label="BIC",
            y_lim=None,
            aspect=None,
            ax=ax)
    save_fig(fig_name='bic.pdf', fig_folder=fig_folder)

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

    print("For latex:")
    for i in range(len(ns)):
        raw_p = f"{ps[i]:.3f}" if ps[i] >= 0.001 else '<0.001'
        p = f"{p_corr[i]:.3f}" if p_corr[i] >= 0.001 else '<0.001'
        print(f'{keys[i]} & ${raw_p}$ & ${p}{"^{*}" if valid[i] else ""}$')