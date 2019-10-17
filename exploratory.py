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
import analysis.supplementary

from analysis.stats import stats

import graph.boxplot
import graph.phase_diagram
import graph.learning_curves
import graph.exploratory.cross_validation


def exploratory_parameters():

    # With gamma = 0.225 simulations fail statistically with 4 goods
    data = analysis.exploratory.sim_and_xp_exploration(beta=1e+20)
    graph.boxplot.plot(data)
    analysis.stats.stats.sim_and_xp(data, name_extension="_exploration")


def exploratory_cross_validation():

    data = analysis.exploratory.cross_validation()
    graph.exploratory.cross_validation.plot(data)
    analysis.stats.stats.cross_validation(data)


def exploratory_median_split():

    ext = '_median_split'
    fig_data = analysis.exploratory.agent_selection()
    graph.boxplot.plot(fig_data,
                       name_extension=ext)
    analysis.stats.stats.sim_and_xp(fig_data,
                                    data_type=('SIM', 'SIM_SELECT'),
                                    name_extension=ext)
