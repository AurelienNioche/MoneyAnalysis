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

import graph.boxplot
import graph.phase_diagram
import graph.supplementary.individual_behavior
import graph.supplementary.age
import graph.supplementary.gender
import graph.supplementary.sensitivity_analysis
import graph.parameter_recovery
import graph.learning_curves
import graph.exploratory.cross_validation

from simulation.model.RL.rl_agent import RLAgent


def sup_sensitivity_analysis():

    data = analysis.supplementary.sensitivity_analysis()
    graph.supplementary.sensitivity_analysis.plot(data)
    stats.sensitivity_analysis(data)


def sup_gender(obs_type='ind0'):

    data = analysis.supplementary.gender(obs_type=obs_type)
    graph.supplementary.gender.plot(data, obs_type=obs_type)
    analysis.stats.stats.supplementary_gender(data, obs_type=obs_type)


def sup_age(obs_type='ind0'):

    data = analysis.supplementary.age(obs_type=obs_type)
    graph.supplementary.age.plot(data, obs_type=obs_type)
    analysis.stats.stats.supplementary_age(data, obs_type=obs_type)


def sup_parameter_recovery():

    fig_data = analysis.supplementary.parameter_recovery(model=RLAgent)
    graph.parameter_recovery.plot(fig_data)
    analysis.stats.stats.parameter_recovery(fig_data)


def sup_effect_of_heterogeneous():

    name_extension = '_fit_non_heterogeneous'
    fig_data = analysis.supplementary.fit(
        model=RLAgent,
        heterogeneous=False)
    graph.boxplot.plot(fig_data, name_extension=name_extension)
    analysis.stats.stats.sim_and_xp(fig_data, name_extension=name_extension)


def sup_effect_of_extended_time(t_max=1000):

    name_extension = '_fit_extended'
    fig_data = analysis.supplementary.fit(
        model=RLAgent,
        heterogeneous=True, t_max=t_max)
    graph.boxplot.plot(fig_data, name_extension=name_extension)
    analysis.stats.stats.sim_and_xp(fig_data, name_extension=name_extension)


if __name__ == '__main__':

    sup_parameter_recovery()
    sup_effect_of_heterogeneous()
    sup_effect_of_extended_time()
