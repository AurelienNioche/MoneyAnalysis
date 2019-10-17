import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MoneyAnalysis.settings")

# Ensure settings are read
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

import analysis.first_revision_basile

from simulation.model.RL.asymmetric_rl_agent import RLAgentAsymmetric
from simulation.model.RL.rl_agent import RLAgent
import graph.exploratory.learning_curves


def revision_learning_curves():
    ind0_freq = analysis.first_revision_basile.learning_curves_xp()
    graph.exploratory.learning_curves.plot(
        fig_data=ind0_freq,
        use_std=True,
        f_name='fig/learning_curve_xp_{}.pdf')

    t_max = 300

    alpha = .175

    factor = 0.66
    alpha_strong = alpha+factor*alpha
    alpha_weak = alpha-factor*alpha

    # 'Old' model
    ind0_freq = analysis.first_revision_basile.learning_curves_sim_ind0_freq(
        t_max=t_max, alpha=alpha, beta=1, gamma=.125, agent_model=RLAgent)

    graph.exploratory.learning_curves.plot(
        fig_data=ind0_freq,
        f_name='fig/learning_curves_sim_ind0_{}.pdf')

    # Optimism bias
    ind0_freq = analysis.first_revision_basile.learning_curves_sim_ind0_freq(
        t_max=t_max, agent_model=RLAgentAsymmetric,
        alpha_minus=alpha_weak, alpha_plus=alpha_strong,
        beta=1, gamma=.125,
    )
    #exchange_value = analysis.first_revision_basile.learning_curves_sim_exchange_values(t_max=t_max)

    graph.exploratory.learning_curves.plot(
        fig_data=ind0_freq,
        f_name='fig/learning_curves_sim_ind0_freq_optimism_{}.pdf')

    # Pessimism bias
    ind0_freq = analysis.first_revision_basile.learning_curves_sim_ind0_freq(
        t_max=t_max, agent_model=RLAgentAsymmetric,
        alpha_minus=alpha_strong, alpha_plus=alpha_weak,
        beta=1, gamma=.125,
    )
    #exchange_value = analysis.first_revision_basile.learning_curves_sim_exchange_values(t_max=t_max)

    graph.exploratory.learning_curves.plot(
        fig_data=ind0_freq, f_name='fig/learning_curves_sim_ind0_freq_pessimism_{}.pdf')


    #graph.exploratory.learning_curves.plot(
    #    fig_data=exchange_value, ylabel='Qvalue',
    #    f_name='fig/first_revision_basile/learning_curves_sim_exchange_value_{}.pdf')


if __name__ == '__main__':

    revision_learning_curves()
