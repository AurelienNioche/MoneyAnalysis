import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MoneyAnalysis.settings")

# Ensure settings are read
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()


import analysis.first_revision


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


def revision_phase_diagram():

    """
    plot phase diagram with asymmetric RL
    """
    agent_models = (RLAgentAsymmetric, )

    for agent_model in agent_models:

        f_name = f'phase_{agent_model.__name__}.pdf'

        data, labels = analysis.first_revision.phase_diagram(
            agent_model=agent_model)
        graph.phase_diagram.plot(data=data, labels=labels, f_name=f_name)


if __name__ == '__main__':

    revision_phase_diagram()
