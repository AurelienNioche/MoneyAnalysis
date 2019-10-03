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
from simulation.model.RL.rl_no_alpha_no_beta import RLNoAlphaNoBeta
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


def revision_phase_diagram():

    """
    plot phase diagram with other agent models
    """
    agent_models = (
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
        RLAgent,
        RLAgentAsymmetric,
        RLNoAlphaNoBeta,
        RLHyperbolicDiscounting,
        RLExponentialDiscounting,
        RLSoftmax,
    )

    for agent_model in agent_models:

        best_parameters, mean_p, lls, bic, eco = \
            analysis.fit.data.get(model=agent_model)

        print("-" * 20)
        print(f"{agent_model.__name__}: {np.mean(bic)}(+/-{np.std(bic)}STD)")
        print("-" * 20)
        print()


if __name__ == '__main__':

    fit()
