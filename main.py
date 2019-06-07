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

import analysis.exploratory
import analysis.main
import analysis.supplementary

from analysis.stats import stats

import graph.sim_and_xp
import graph.phase_diagram
import graph.supplementary.s1_and_s2
import graph.supplementary.age
import graph.supplementary.gender
import graph.supplementary.effect_of_unique_parameter
import graph.supplementary.parameter_recovery
import graph.supplementary.learning_curves
import graph.supplementary.cross_validation


def phase_diagram(f_name='phase.pdf'):

    """
    plot phase diagrams
    with 3 and 4 goods
    """

    data, labels = analysis.main.phase_diagram()
    graph.phase_diagram.plot(data=data, labels=labels, f_name=f_name)


def sim_and_xp():

    data = analysis.main.sim_and_xp()
    graph.sim_and_xp.plot(data)
    analysis.stats.stats.sim_and_xp(data)


def sim_and_xp_exploration():

    # With gamma = 0.225 simulations fail statistically with 4 goods but graph are not clear
    data = analysis.exploratory.sim_and_xp_exploration(beta=1e+20)
    graph.sim_and_xp.plot(data)
    analysis.stats.stats.sim_and_xp(data, name_extension="exploration")


def supplementary_sim_and_xp():

    data = analysis.supplementary.supplementary_sim_and_xp()
    graph.supplementary.s1_and_s2.plot(data)


def old_supplementary_gender():

    data = analysis.supplementary.old_supplementary_gender()
    graph.supplementary.gender.plot(data)
    analysis.stats.stats.supplementary_gender(data)


def supplementary_age():

    data = analysis.supplementary.supplementary_age()
    graph.supplementary.age.plot(data)
    analysis.stats.stats.supplementary_age(data)


def parameter_recovery():

    fig_data = analysis.supplementary.supplementary_parameter_recovery()
    graph.supplementary.parameter_recovery.plot(fig_data)
    analysis.stats.stats.parameter_recovery(fig_data)


def fit():

    fig_data = analysis.supplementary.supplementary_fit()
    graph.sim_and_xp.plot(fig_data, name_extension='FIT')
    stats.sim_and_xp(fig_data, name_extension='FIT')


def learning_curves():

    fig_data = analysis.exploratory.learning_curves()
    graph.supplementary.learning_curves.plot(fig_data)


def ind0_freq_over_time():

    data = analysis.exploratory.ind0_freq_over_time()
    graph.supplementary.learning_curves.plot(data, f_name='fig/ind0_freq_over_time_{}.pdf')


def supplementary_gender():
    obs_type = 'ind_0'
    data = analysis.supplementary.supplementary_gender(obs_type=obs_type)
    graph.supplementary.gender.plot(data)
    analysis.stats.stats.supplementary_gender(data, obs_type=obs_type)


def cross_validation():

    data = analysis.exploratory.cross_validation()
    graph.supplementary.cross_validation.plot(data)
    analysis.stats.stats.cross_validation(data)


def check_effect_of_heterogeneous():

    name_extension = 'FIT_non_heterogeneous'
    fig_data = analysis.supplementary.supplementary_fit(heterogeneous=False)
    graph.sim_and_xp.plot(fig_data, name_extension=name_extension)
    analysis.stats.stats.sim_and_xp(fig_data, name_extension=name_extension)


def check_effect_of_extended_time():

    name_extension = 'FIT_extended'
    fig_data = analysis.supplementary.supplementary_fit(heterogeneous=False, t_max=1000)
    graph.sim_and_xp.plot(fig_data, name_extension=name_extension)
    analysis.stats.stats.sim_and_xp(fig_data, name_extension=name_extension)


def effect_of_unique_parameter():

    data = analysis.supplementary.effect_of_unique_parameter()
    graph.supplementary.effect_of_unique_parameter.plot(data)


if __name__ == '__main__':

    # # Uncomment for running simulations used for phase diagram
    phase_diagram()

    # # Uncomment for experiment analysis and experiment-like simulations
    sim_and_xp()

    # # Uncomment for supplementary analysis
    supplementary_sim_and_xp()

    # # Uncomment for supplementary analysis concerning gender
    supplementary_gender()
    supplementary_age()

    # # Uncomment for supplementary analysis concerning parameter exploration
    sim_and_xp_exploration()

    # # Uncomment for supplementary analysis related to fit
    fit()
    learning_curves()
    parameter_recovery()
