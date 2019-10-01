# MoneyAnalysis
# Copyright (C) 2018  Aurélien Nioche, Basile Garcia & Nicolas Rougier
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
# Django specific settings
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MoneyAnalysis.settings")

# Ensure settings are read
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

import simulation.run

import analysis.exploratory
import analysis.main
import analysis.supplementary

from analysis.stats import stats

import graph.sim_and_xp
import graph.phase_diagram
import graph.supplementary.individual_behavior
import graph.supplementary.age
import graph.supplementary.gender
import graph.supplementary.sensitivity_analysis
import graph.supplementary.parameter_recovery
import graph.exploratory.learning_curves
import graph.exploratory.cross_validation


def main_phase_diagram(f_name='phase.pdf'):

    """
    plot phase diagrams
    with 3 and 4 goods
    """

    data, labels = analysis.main.phase_diagram()
    graph.phase_diagram.plot(data=data, labels=labels, f_name=f_name)


def main_sim_and_xp():

    data = analysis.main.sim_and_xp()
    graph.sim_and_xp.plot(data)
    analysis.stats.stats.sim_and_xp(data)


# ------------------------------------------------- #



def exploratory_parameters():

    # With gamma = 0.225 simulations fail statistically with 4 goods
    data = analysis.exploratory.sim_and_xp_exploration(beta=1e+20)
    graph.sim_and_xp.plot(data)
    analysis.stats.stats.sim_and_xp(data, name_extension="_exploration")


def exploratory_learning_curves():

    fig_data = analysis.exploratory.learning_curves()
    graph.exploratory.learning_curves.plot(fig_data)


# def ind0_freq_over_time():
#
#     data = analysis.exploratory.ind0_freq_over_time()
#     graph.supplementary.learning_curves.plot(
#         data,
#         f_name='fig/ind0_freq_over_time_{}.pdf')


def exploratory_cross_validation():

    data = analysis.exploratory.cross_validation()
    graph.exploratory.cross_validation.plot(data)
    analysis.stats.stats.cross_validation(data)


def exploratory_median_split():

    ext = '_median_split'
    fig_data = analysis.exploratory.agent_selection()
    graph.sim_and_xp.plot(fig_data,
                          name_extension=ext)
    analysis.stats.stats.sim_and_xp(fig_data,
                                    data_type=('SIM', 'SIM_SELECT'),
                                    name_extension=ext)


if __name__ == '__main__':

    # n_eco()

    # # # Uncomment for running simulations used for phase diagram
    main_phase_diagram()
    #
    # # For stats about reward
    # main_reward()
    #
    # # # Uncomment for experiment analysis and experiment-like simulations
    # main_sim_and_xp()
    #
    # # # Uncomment for sensitivity analysis
    # #
    # # # # Uncomment demographic analysis
    # sup_gender()
    # sup_age()
    # #
    # # # Uncomment for supplementary analysis
    # sup_individual_behavior()
    #
    # # # Uncomment for supplementary analysis related to fit
    # sup_fit()
    # sup_parameter_recovery()
    # sup_effect_of_heterogeneous()
    # sup_effect_of_extended_time()
