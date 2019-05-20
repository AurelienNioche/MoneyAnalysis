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

import metric.metric as metric

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MoneyAnalysis.settings")

# Ensure settings are read
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

import numpy as np

from backup import backup

import simulation.economy
import simulation.run
import simulation.run_xp_like

import graph.boxplot
import graph.phase_diagram
import graph.supplementary.s1_and_s2

from xp import xp

from metric import metric

from graph.boxplot import _boxplot

import matplotlib.pyplot as plt

SCRIPT_FOLDER = os.path.dirname(os.path.abspath(__file__))
DATA_FOLDER = f'{SCRIPT_FOLDER}/data'


def phase_diagram(f_name='phase.pdf'):

    """
    plot phase diagrams
    with 3 and 4 goods
    """

    # Number of column
    # (Plot for each good considered as money if max_col == None)
    max_col = 1

    data_file = f'{DATA_FOLDER}/formatted_phase_diagram.p'

    if os.path.exists(data_file):
        data, labels = backup.load(data_file)

    else:

        data = []

        for n_good in 3, 4:
            d = simulation.run.get_data(n_good=n_good)

            formatted_data, labels = metric.phase_diagram(
                in_hand=d.in_hand,
                desired=d.desired,
                prod=d.prod,
                cons=d.cons,
                distribution=d.distribution,
                n_good=len(d.distribution[0])
            )
            data.append(formatted_data)

        backup.save((data, labels), data_file)

    graph.phase_diagram.plot(
        data=data,
        labels=labels,
        f_name=f_name,
        max_col=max_col
    )


def sim_and_xp():

    data = {}

    data['HUMAN'], room_n_good, room_uniform = xp.get_data()

    data['SIM'] = simulation.run_xp_like.get_data(xp_data=data['HUMAN'])

    category = data.keys()
    n_good_cond = np.unique(room_n_good)
    cond_labels = "NON-UNIF", "UNIF"

    fig_data = {n_good: {
        cat: {

        } for cat in category
    } for n_good in n_good_cond}

    for n_good in n_good_cond:

        for uniform in True, False:

            # Find the good indexes
            cond_n_good = room_n_good == n_good
            cond_uniform = room_uniform == uniform

            xp_cond = cond_n_good * cond_uniform
            assert(np.sum(xp_cond) == 1)
            d_idx = np.where(xp_cond == 1)[0][0]

            for cat in category:

                # Get formatted data
                d = data[cat][d_idx]
                d_formatted = metric.dynamic_data(data_xp_session=d)

                for agent_type in d_formatted.keys():
                    if agent_type not in fig_data[n_good][cat].keys():
                        fig_data[n_good][cat][agent_type] = {}

                    fig_data[n_good][cat][agent_type][cond_labels[int(uniform)]] = d_formatted[agent_type]

    graph.boxplot.plot(fig_data)


def supplementary_sim_and_xp():

    data = {}

    data['HUMAN'], room_n_good, room_uniform = xp.get_data()

    data['SIM'] = simulation.run_xp_like.get_data(xp_data=data['HUMAN'])

    category = data.keys()
    n_good_cond = np.unique(room_n_good)
    cond_labels = "NON-UNIF", "UNIF"

    fig_data = {n_good: {
        cat: {

        } for cat in category
    } for n_good in n_good_cond}

    for n_good in n_good_cond:

        for uniform in True, False:

            # Find the good indexes
            cond_n_good = room_n_good == n_good
            cond_uniform = room_uniform == uniform

            xp_cond = cond_n_good * cond_uniform
            assert(np.sum(xp_cond) == 1)
            d_idx = np.where(xp_cond == 1)[0][0]

            for cat in category:

                # Get formatted data
                d = data[cat][d_idx]
                d_formatted = metric.dynamic_data(data_xp_session=d, slice_idx='all')

                for agent_type in d_formatted.keys():
                    if agent_type not in fig_data[n_good][cat].keys():
                        fig_data[n_good][cat][agent_type] = {}

                    fig_data[n_good][cat][agent_type][cond_labels[int(uniform)]] = d_formatted[agent_type]

    graph.supplementary.s1_and_s2.plot(fig_data)


if __name__ == '__main__':

    # # Uncomment for running simulations used for phase diagram
    # phase_diagram()

    # # Uncomment for experiment analysis and experiment-like simulations
    # sim_and_xp()

    # # Uncomment for supplementary analysis
    supplementary_sim_and_xp()
