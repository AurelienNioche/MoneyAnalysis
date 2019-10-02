import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MoneyAnalysis.settings")

# Ensure settings are read
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

import analysis.first_revision_basile

import graph.exploratory.learning_curves


def revision_learning_curves():
    data = analysis.first_revision_basile.learning_curves_sim()
    graph.exploratory.learning_curves.plot(
        fig_data=data, f_name='fig/learning_curves_sim_{}.pdf')


if __name__ == '__main__':

    revision_learning_curves()
