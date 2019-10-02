import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MoneyAnalysis.settings")

# Ensure settings are read
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()


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


def revision_learning_curves():
    data = analysis.first_revision_basile.learning_curves_sim()
    graph.exploratory.learning_curves.plot(
        fig_data=data, f_name='fig/learning_curves_sim_{}.pdf')


if __name__ == '__main__':

    #revision_phase_diagram()
    revision_learning_curves()
