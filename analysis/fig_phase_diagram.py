import simulation.run
import simulation.run_xp_like
from analysis.metric import metric

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MoneyAnalysis.settings")

# Ensure settings are read
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

import numpy as np

import simulation.run_based_on_fit
import simulation.run_xp_like

import graph.boxplot
import graph.phase_diagram

import graph.supplementary.age
import graph.supplementary.gender
import graph.supplementary.sensitivity_analysis
import graph.parameter_recovery
import graph.learning_curves
import graph.exploratory.cross_validation
import graph.learning_curves

from simulation.model.RL.asymmetric_rl_agent import RLAsymmetric
from simulation.model.RL.rl_no_alpha_no_beta \
    import RLNoAlphaNoBeta, RLNoAlphaNoBetaV2
from simulation.model.RL.rl_hyperbolic_discounting \
    import RLHyperbolicDiscounting
from simulation.model.RL.rl_exponential_discounting \
    import RLExponentialDiscounting
from simulation.model.RL.rl_softmax import RLSoftmax
from simulation.model.RL.rl_agent import RLAgent

import simulation.run

from backup import backup

import simulation.run_asymmetric_learning

DATA_FOLDER = "data"


def _data_for_phase_diagram(agent_model, n_good_condition, m=0):

    data_file = os.path.join(
        DATA_FOLDER,
        f'formatted_phase_diagram_'
        f'{agent_model.__name__}_'
        f'{"_".join(str(i) for i in n_good_condition)}.p')

    if os.path.exists(data_file):

        data, labels = backup.load(data_file)
        return data, labels
    data = {}

    labels = None
    for n_good in n_good_condition:

        d = simulation.run.get_data(
            agent_model=agent_model,
            n_good=n_good)

        dist = d.distribution

        n = len(dist)  # Number of economies in this batch

        observation = metric.get_multi_eco_statistic(in_hand=d.in_hand,
                                                     desired=d.desired,
                                                     prod=d.prod,
                                                     cons=d.cons,
                                                     m=m)

        unq_repartition = np.unique(dist, axis=0)
        labels = np.unique([i[-1] for i in unq_repartition])

        n_side = len(labels)

        scores = np.array([
            np.mean([observation[i] for i in range(n) if np.all(dist[i] == r)])
            for r in unq_repartition
        ])

        formatted_d = scores.reshape(n_side, n_side).T

        data[n_good] = formatted_d

    backup.save((data, labels), data_file)

    return data, labels


def all_phase_diagram():

    """
    plot phase diagram with other agent models
    """
    agent_models = (
        RLAgent,
        RLNoAlphaNoBetaV2,
        RLAsymmetric,
        RLNoAlphaNoBeta,
        RLHyperbolicDiscounting,
        RLExponentialDiscounting,
        RLSoftmax,
    )

    # Different agent models

    for agent_model in agent_models:

        fig_name = f'phase_{agent_model.__name__}.pdf'
        fig_folder = "fig/main" if agent_model == RLAgent else "fig/sup"

        print(f'Producing data for model "{agent_model.__name__}"...')

        data, labels = _data_for_phase_diagram(
            agent_model=agent_model, n_good_condition=(3, 4))

        graph.phase_diagram.plot(data=data, labels=labels,
                                 fig_name=fig_name, fig_folder=fig_folder)

    # Multiple goods
    fig_name = f'phase_diagram_n_good.pdf'
    fig_folder = "fig/sup"

    print(f'Producing data for multiple goods...')

    data, labels = _data_for_phase_diagram(
        agent_model=RLAgent, n_good_condition=(5, 6))

    graph.phase_diagram.plot(data=data,
                             labels=labels,
                             fig_name=fig_name,
                             fig_folder=fig_folder)

    # Asymmetric
    fig_name = f'phase_diagram_asymmetric.pdf'
    data, labels = simulation.run_asymmetric_learning.phase_diagram(
        force=False
    )

    graph.phase_diagram.plot(
        data=data, labels=labels,
        fig_name=fig_name,
        fig_folder=fig_folder,
        x_label='alpha_plus',
        y_label='alpha_minus',
        ticks_index=[0, 5, 9],
    )

