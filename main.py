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

import graph.sim_and_xp
import graph.phase_diagram
import graph.supplementary.s1_and_s2
import graph.supplementary.age
import graph.supplementary.gender

import stats.stats

import format.data


def phase_diagram(f_name='phase.pdf'):

    """
    plot phase diagrams
    with 3 and 4 goods
    """

    data, labels = format.data.phase_diagram()
    graph.phase_diagram.plot(data=data, labels=labels, f_name=f_name)


def sim_and_xp():

    data = format.data.sim_and_xp()
    graph.sim_and_xp.plot(data)
    stats.stats.sim_and_xp(data)


def sim_and_xp_exploration():

    # With gamma = 0.225 simulations fail statistically with 4 goods but graph are not clear
    data = format.data.sim_and_xp_exploration(beta=1e+20)
    graph.sim_and_xp.plot(data)
    stats.stats.sim_and_xp(data, extension="exploration")


def supplementary_sim_and_xp():

    data = format.data.supplementary_sim_and_xp()
    graph.supplementary.s1_and_s2.plot(data)


def supplementary_gender():

    data = format.data.supplementary_gender()
    graph.supplementary.gender.plot(data)
    stats.stats.supplementary_gender(data)


def supplementary_age():

    age, data = format.data.supplementary_age()
    graph.supplementary.age.plot(age=age, y=data)
    stats.stats.supplementary_age(age=age, y=data)


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
