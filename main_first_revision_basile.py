import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MoneyAnalysis.settings")

# Ensure settings are read
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

import analysis.first_revision_basile

import graph.exploratory.learning_curves


def revision_learning_curves():

    t_max = 300

    ind0_freq = analysis.first_revision_basile.learning_curves_sim_ind0_freq(t_max=t_max)
    exchange_value = analysis.first_revision_basile.learning_curves_sim_exchange_values(t_max=t_max)

    graph.exploratory.learning_curves.plot(
        fig_data=ind0_freq, f_name='fig/first_revision_basile/learning_curves_sim_ind0_freq_{}.pdf')

    graph.exploratory.learning_curves.plot(
        fig_data=exchange_value, ylabel='Qvalue',
        f_name='fig/first_revision_basile/learning_curves_sim_exchange_value_{}.pdf')


if __name__ == '__main__':

    revision_learning_curves()
