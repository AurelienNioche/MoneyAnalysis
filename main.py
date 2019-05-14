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

import analysis.tools
import analysis.tools.format
import analysis.tools.economy

import analysis.graph
import analysis.graph.phase_diagram

import analysis.experiment.monetary_and_medium
import analysis.experiment.demographics

import analysis.stats.mean_comparison
import simulation.supplementary_exploration
import simulation.supplementary_exploitation
import simulation.supplementary_main

from xp.xp import load_individual_data_from_db

SCRIPT_FOLDER = os.path.dirname(os.path.abspath(__file__))
DATA_FOLDER = f'{SCRIPT_FOLDER}/data'


def phase_diagram():

    """
    plot phase diagrams
    with 3 and 4 goods
    """

    f_name = 'fig/phase.pdf'

    # Number of column
    # (Plot for each good considered as money if max_col == None)
    max_col = 1

    data_file = f'{DATA_FOLDER}/formatted_phase_diagram.p'

    if os.path.exists(data_file):
        data, labels = backup.load(data_file)

    else:

        data = []

        for n_good in 3, 4:
            d = simulation.run.get_data(phase=True, n_good=n_good)

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

    analysis.graph.phase_diagram.plot(
        data=data,
        labels=labels,
        f_name=f_name,
        max_col=max_col
    )


def sim_and_xp(n_split=3):

    data, room_n_good, room_uniform = load_individual_data_from_db()

    for n_good in 3, 4:

        for uniform in True, False:

            cond_n_good = room_n_good == n_good
            cond_uniform = room_uniform == uniform

            cond = cond_n_good * cond_uniform
            assert(np.sum(cond) == 1)
            d_idx = np.where(cond == 1)[0][0]
            print(type(d_idx))
            d = data[d_idx]

            n_agent = len(d.prod)
            for i in range(n_agent):
                dir_ex, ind_ex, n = metric.exchange(n_good=n_good,in_hand=d.in_hand[i],
                                                    desired=d.in_hand[i], cons=d.cons[i],
                                                    prod=d.prod[i])
                metric.get_windowed_observation(dir_ex=dir_ex, ind_ex=ind_ex, n=n, n_split=n_split, n_good=n_good)

    # bkp = simulation.run.get_data(phase=False)
    #
    # room_id = {
    #     3: (414, 416),
    #     4: (417, 415)
    # }
    #
    # for n_good in (3, 4):
    #
    #     data = []
    #
    #     titles = [analysis.tools.economy.labels.get(r_id) for r_id in room_id[n_good]]
    #
    #     for r_id in room_id[n_good]:
    #
    #         label = analysis.tools.economy.labels.get(r_id)
    #         xp_session = f"{n_good}-{'NUPM' if 'non_uniform' in label else 'U'}"
    #         print(f"Stats for simulation '{label}':")

            # ------------------------- Get data --------------------- #

            # monetary_bhv = [
            #     d for i, d in enumerate(bkp.monetary_bhv)
            #     if bkp.room_id[i] == r_id
            # ]
            #
            # medium = [
            #     d for i, d in enumerate(bkp.medium)
            #     if bkp.room_id[i] == r_id
            # ]
            #
            # # distribution is common
            # distribution = [
            #     d for i, d in enumerate(bkp.distribution)
            #     if bkp.room_id[i] == r_id
            # ][0]

            # # Now we can do stats
            # money_sig = analysis.stats.mean_comparison.run(monetary_over_user_mean,
            #                                                print_latex=True,
            #                                                xp_session=xp_session, measure="MB"
            #                                                )


if __name__ == '__main__':

    # Create fig folder
    os.makedirs("fig", exist_ok=True)

    # # Uncomment for running simulations used for phase diagram
    # phase_diagram()

    # # Uncomment for experiment analysis and experiment-like simulations
    sim_and_xp()

    #   PROBABLY TO REMOVE !!!!!!
    # simulation.supplementary_exploitation.main()
