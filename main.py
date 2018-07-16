# DuopolyAnalysis
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


import matplotlib.pyplot as plt
import matplotlib.gridspec as grd
import itertools as it
import numpy as np
import pickle
# from analysis import demographics, medium, monetary_behavior, strategy, life_expectancy, \
#     strategy_count, strategy_count_pool, monetary_behavior_pool
# import graph.strategy
# import graph.life_expectancy
# import graph.strategy_count_pool
import backup.backup as backup

import simulation.economy
import simulation.runner

import analysis.fit.RL.optimize

import analysis.tools
import analysis.tools.format
import analysis.tools.economy

import analysis.graph
import analysis.graph.monetary_and_medium
import analysis.graph.phase_diagram

import analysis.compute.monetary_and_medium
import analysis.compute.strategy_count_pool

import analysis.stats.mean_comparison


def stats_exp():

    # --------------- Monetary bhv ------------------------ #

    data = analysis.compute.monetary_and_medium.run()

    print('*' * 5, 'TESTING MONETARY BHV', '*' * 5)

    for k, v in data.items():

        print('Room: ', k)

        analysis.stats.mean_comparison.monetary_behavior(v['monetary_bhv'])

    # --------------- Medium  ------------------------ #

    print('*' * 5, 'TESTING USED AS MEDIUM', '*' * 5)

    data = analysis.compute.strategy_count_pool.run()

    for k, v in data.items():

        print('Room: ', k.replace('_strategy_count_pool', ''))

        analysis.stats.mean_comparison.medium(v['medium'])


def bar_plots():

    # --------------- Monetary bhv ------------------------ #

    data = analysis.compute.monetary_and_medium.run()

    for k, v in data.items():

        analysis.graph.monetary_and_medium.one_condition_money_bar(v['monetary_bhv'], k)
    #
    # --------------- Medium  ------------------------ #

    data = analysis.compute.strategy_count_pool.run()

    for k, v in data.items():

        k = k.replace('_strategy_count_pool', '')

        analysis.graph.monetary_and_medium.one_condition_medium_bar(v['medium'], k)


def stats_sim_exp_like():

    data = simulation.runner.run(exp_like=True)

    cond = analysis.tools.economy.labels.copy().items()

    print('*' * 5, 'TESTING MONETARY BHV', '*' * 5)

    for i, (room_id, label) in enumerate(sorted(cond)):

        monetary_bhv = [b for i, b in enumerate(data.monetary_bhv) if data.room_id[i] == room_id]

        print('Room: ', label)

        analysis.stats.mean_comparison.monetary_behavior(monetary_bhv)

    # print('*' * 5, 'TESTING USED AS MEDIUM', '*' * 5)
    #
    # for i, (room_id, label) in enumerate(sorted(cond)):
    #
    #     medium = [b for i, b in enumerate(data.medium) if data.room_id[i] == room_id]
    #
    #     print('Room: ', label)
    #
    #     analysis.stats.mean_comparison.medium(medium)


def run_experiment():
    data = analysis.compute.monetary_and_medium.run()

    for label, room_data in data.items():
        analysis.graph.monetary_and_medium.one_condition(room_data, f_name=f'xp_{label}.pdf')


def run_simulation():

    data = pickle.load(open('data/fit.p', 'rb'))

    for r_id in analysis.tools.economy.labels.keys():

        # after reformatting
        data_fit = analysis.tools.format.for_fit(data)

        label = analysis.tools.economy.labels.get(r_id)

        cognitive_parameters = data_fit[label]

        repartition = analysis.tools.economy.repartitions.get(r_id)

        res = simulation.economy.launch(
            agent_model='RLAgent',
            repartition=repartition,
            t_max=50,
            economy_model='prod: i-1',
            cognitive_parameters=cognitive_parameters,
            seed=123
        )
        res['repartition'] = repartition

        analysis.graph.monetary_and_medium.one_condition(res, f_name=f"sim_{label}.pdf")


def phase_diagram():

    three_good_file = 'data/phase_3_goods.p'
    four_good_file = 'data/phase_4_goods.p'

    four_good_data = backup.load(four_good_file)
    three_good_data = backup.load(three_good_file)

    analysis.graph.phase_diagram.plot(
        three_good=three_good_data,
        four_good=four_good_data
    )


def run_simulations():
    simulation.runner.run(exp_like=False)


def main():
    run_simulations()


if __name__ == '__main__':

    # main()

    # bar_plots()
    phase_diagram()
    # run_simulations()
    # bar_plots()
    # phase_diagram()
