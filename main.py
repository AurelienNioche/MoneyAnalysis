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


import backup.backup as backup

import simulation.economy
import simulation.runner

import analysis.tools
import analysis.tools.format
import analysis.tools.economy

import analysis.graph
import analysis.graph.monetary_and_medium_over_time
import analysis.graph.monetary_and_medium_bar
import analysis.graph.phase_diagram

import analysis.compute.monetary_and_medium
import analysis.compute.medium_over_individuals
import analysis.compute.demographics

import analysis.stats.mean_comparison


def stats_exp():

    # --------------- Monetary bhv ------------------------ #

    monetary_bhv = analysis.compute.monetary_and_medium.run()
    medium = analysis.compute.medium_over_individuals.run()

    room_ids = (414, 415, 416, 417)

    for r_id in room_ids:

        print('*' * 5, 'Room', r_id, '*' * 5)

        label = analysis.tools.economy.labels.get(r_id)

        print(label)

        # --------------- Monetary bhv  ------------------------ #

        print('Testing monetary behavior')

        data = analysis.tools.format.for_monetary_behavior_over_user_from_experiment(
            monetary_bhv[label]['monetary_bhv']
        )

        analysis.stats.mean_comparison.monetary_behavior(data)

        # --------------- Medium  ------------------------ #

        print('Testing medium')

        data = medium[label]['medium']

        analysis.stats.mean_comparison.medium(data)


def stats_sim():

    bkp = simulation.runner.run(phase=False)

    room_ids = (414, 415, 416, 417)

    for r_id in room_ids:

        print('*' * 5, 'Room', r_id, '*' * 5)
        print(analysis.tools.economy.labels.get(r_id))

        # ------------------------- Get data --------------------- #

        monetary_bhv = [
            d for i, d in enumerate(bkp.monetary_bhv)
            if bkp.room_id[i] == r_id
        ]

        medium_over_agents = [
            d for i, d in enumerate(bkp.medium_over_agents)
            if bkp.room_id[i] == r_id
        ]

        # ---------------------- format for monetary -------------- #

        print('Testing monetary behavior')

        # reformat each economies to compress on agents
        monetary_over_user = [
            analysis.tools.format.for_monetary_behavior_bar_plot_from_simulation_pool(m)
            for m in monetary_bhv
        ]

        # average all that
        monetary_over_user_mean = \
            analysis.tools.format.for_variable_over_user_mean(monetary_over_user)

        # Now we can do stats
        analysis.stats.mean_comparison.monetary_behavior(monetary_over_user_mean)

        # ---------------------- format for medium -------------- #

        print('Testing medium')

        # reformat each economies to compress on agents
        medium_over_user = [
            analysis.tools.format.for_medium_bar_plot_from_simulation_pool(m) for m in medium_over_agents
        ]

        # average all that
        medium_over_user_mean = \
            analysis.tools.format.for_variable_over_user_mean(medium_over_user)

        # Now we can do stats
        analysis.stats.mean_comparison.medium(medium_over_user_mean)


def phase_diagram():

    """
    plot phase diagrams
    with 3 and 4 goods
    """

    three_good_file = 'data/phase_3_goods.p'
    four_good_file = 'data/phase_4_goods.p'
    f_name = 'fig/phase.pdf'

    # Number of column
    # (Plot for each good considered as money if max_col == None)
    max_col = 1

    if not os.path.exists(three_good_file):
        three_good_data = simulation.runner.run(phase=True, n_good=3)
    else:
        three_good_data = backup.load(three_good_file)

    if not os.path.exists(four_good_file):
        four_good_data = simulation.runner.run(phase=True, n_good=4)
    else:
        four_good_data = backup.load(four_good_file)

    data = []

    for d in (three_good_data, four_good_data):

        formatted_data, labels = analysis.tools.format.for_phase_diagram(
            monetary_behavior=d.monetary_bhv,
            repartition=d.repartition,
            n_good=len(d.repartition[0])
        )

        data.append(formatted_data)

    analysis.graph.phase_diagram.plot(
        data=data,
        labels=labels,
        f_name=f_name,
        max_col=max_col
    )


def exp_overall():

    """
    plots each experimental condition
    from experimental data

    """

    monetary = analysis.compute.monetary_and_medium.run()
    medium = analysis.compute.medium_over_individuals.run()

    for good in (3, 4):

        data = []
        titles = (f'{good}_good_non_uniform', f'{good}_good_uniform')

        for k in titles:

            # Used as medium over t is computed in monetary_behavior script
            med_t = monetary[k]['medium']

            m_bhv = monetary[k]['monetary_bhv']

            # Used as medium pooled over agents is computed in strategy_count_pool script
            med_bar = medium[k]['medium']

            repartition = monetary[k]['repartition']

            # Format data for Monetary bhv graph
            monetary_means, monetary_err = analysis.tools.format.for_monetary_behavior_bar_plot_from_experiment(m_bhv)
            money_sig = analysis.stats.mean_comparison.monetary_behavior(m_bhv)

            monetary_over_t = analysis.tools.format.for_monetary_behavior_over_t(m_bhv, repartition)

            # Format data for Used as medium graph
            medium_means, medium_err = analysis.tools.format.for_medium_bar_plot_from_experiment(med_bar)
            med_sig = analysis.stats.mean_comparison.medium(med_bar)

            medium_over_t = analysis.tools.format.for_medium_over_t(med_t, repartition)

            d = {
                'monetary_bar': (monetary_means, monetary_err, money_sig),
                'monetary_over_t': monetary_over_t,
                'medium_bar': (medium_means, medium_err, med_sig),
                'medium_over_t': medium_over_t,
                'repartition': repartition
            }

            data.append(d)

        analysis.graph.monetary_and_medium_over_time.overall_one_good(data, titles, f_name=f'fig/xp_{good}.pdf', exp=True)


def sim_overall():

    """
    plots each experimental condition
    from simulation data

    """

    bkp = simulation.runner.run(phase=False)

    room_id = {
        3: (414, 416),
        4: (415, 417)
    }

    for n_good in (3, 4):

        data = []

        titles = [analysis.tools.economy.labels.get(r_id) for r_id in room_id[n_good]]

        for r_id in room_id[n_good]:

            # ------------------------- Get data --------------------- #

            monetary_bhv = [
                d for i, d in enumerate(bkp.monetary_bhv)
                if bkp.room_id[i] == r_id
            ]

            medium_over_time = [
                d for i, d in enumerate(bkp.medium_over_time)
                if bkp.room_id[i] == r_id
            ]

            medium_over_agents = [
                d for i, d in enumerate(bkp.medium_over_agents)
                if bkp.room_id[i] == r_id
            ]

            # repartition is common
            repartition = [
                d for i, d in enumerate(bkp.repartition)
                if bkp.room_id[i] == r_id
            ][0]

            # ------------------------- Monetary bhv ------------------------------- #

            # BAR PLOTS
            # reformat each economies to compress on agents
            monetary_over_user = [
                analysis.tools.format.for_monetary_behavior_bar_plot_from_simulation_pool(m)
                for m in monetary_bhv
            ]

            # average all that
            monetary_over_user_mean = \
                analysis.tools.format.for_variable_over_user_mean(monetary_over_user)

            # Now we can do stats
            money_sig = analysis.stats.mean_comparison.medium(monetary_over_user_mean)

            # reformat for bar plots
            monetary_means, monetary_err = \
                analysis.tools.format.for_monetary_bar_plot_from_simulation(monetary_over_user_mean)

            # CURVE PLOTS
            monetary_over_t = [
                analysis.tools.format.for_monetary_behavior_over_t(m, repartition)
                for m in monetary_bhv
            ]

            # Average all that
            monetary_over_t_means = analysis.tools.format.for_monetary_behavior_over_time_mean(monetary_over_t)

            # ------------------------- Medium ------------------------------- #

            # BAR PLOTS
            # reformat each economies to compress on agents
            medium_over_user = [
                analysis.tools.format.for_medium_bar_plot_from_simulation_pool(m) for m in medium_over_agents
            ]

            # average all that
            medium_over_user_mean = \
                analysis.tools.format.for_variable_over_user_mean(medium_over_user)

            # Now we can do stats
            med_sig = analysis.stats.mean_comparison.medium(medium_over_user_mean)

            # reformat for bar plots
            medium_means, medium_err = \
                analysis.tools.format.for_medium_bar_plot_from_simulation(medium_over_user_mean)

            # CURVE PLOTS
            # compress each economies on time
            medium_over_t = [
                analysis.tools.format.for_medium_over_t(m, repartition)
                for m in medium_over_time
            ]

            # average all that
            medium_over_t_means = analysis.tools.format.for_medium_over_time_mean(medium_over_t)

            d = {
                'monetary_bar': (monetary_means, monetary_err, money_sig),
                'monetary_over_t': monetary_over_t,
                'monetary_over_t_means': monetary_over_t_means,
                'medium_bar': (medium_means, medium_err, med_sig),
                'medium_over_t': medium_over_t,
                'medium_over_t_means': medium_over_t_means,
                'repartition': repartition
            }

            data.append(d)

        analysis.graph.monetary_and_medium_over_time.overall_one_good(
            data, titles, f_name=f'fig/sim_{n_good}.pdf', exp=False
        )


def run_simulations():

    """
    runs simulations with
    command line arguments
    """

    simulation.runner.run()


def main():
    pass


if __name__ == '__main__':

    # main()

    # # Uncomment for experiment analysis and experiment-like simulations
    # exp_overall()
    # sim_overall()

    # # Uncomment for producing stats
    # stats_sim()
    # stats_exp()

    # # Uncomment for running simulations used for phase diagram
    # phase_diagram()

    run_simulations()
    pass
