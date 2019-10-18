import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MoneyAnalysis.settings")

# Ensure settings are read
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()


def phase_diagram():

    from analysis.fig_phase_diagram import all_phase_diagram
    all_phase_diagram()


def fig_bic():

    from analysis.fig_bic import fig_bic
    fig_bic()


def main_sim_and_xp():

    from analysis.fig_sim_xp_post import fig_sim_xp_post
    fig_sim_xp_post()


if __name__ == '__main__':

    fig_bic()
    main_sim_and_xp()
    phase_diagram()
