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


import pickle
import backup.backup as backup

import simulation.economy
import simulation.runner

import analysis.fit.RL.optimize

import analysis.tools
import analysis.tools.format
import analysis.tools.economy

import analysis.graph
import analysis.graph.monetary_and_medium
import analysis.graph.monetary_and_medium_bar
import analysis.graph.phase_diagram

import analysis.compute.monetary_and_medium
import analysis.compute.strategy_count_pool
import analysis.compute.demographics

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
        analysis.stats.mean_comparison.medium(monetary_over_user_mean)

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


def bar_plots():

    """
    plots bar for each condition from experimental data
    all plots are computed from two dimensions: n_good, n_agents
    """

    # --------------- Monetary bhv ------------------------ #

    data = analysis.compute.monetary_and_medium.run()

    xlabel = 'Good'
    ylabel = 'Monetary behavior'

    for k, v in data.items():

        sig = analysis.stats.mean_comparison.monetary_behavior(v['monetary_bhv'])
        title = k
        means, err = analysis.tools.format.for_monetary_behavior_bar_plot_from_experiment(v['monetary_bhv'])
        f_name = f'fig/monetary_bar_{title}'

        analysis.graph.monetary_and_medium_bar.one_condition_bar(
            means=means,
            err=err,
            title=title,
            ylabel=ylabel,
            xlabel=xlabel,
            sig=sig,
            f_name=f_name
        )

    # --------------- Medium  ------------------------ #

    data = analysis.compute.strategy_count_pool.run()

    xlabel = 'Good'
    ylabel = 'Used as medium'

    for k, v in data.items():

        title = k.replace('_strategy_count_pool', '')

        sig = analysis.stats.mean_comparison.medium(v['medium'])
        means, err = analysis.tools.format.for_medium_bar_plot_from_experiment(v['medium'])
        f_name = f'fig/medium_bar_{title}'

        analysis.graph.monetary_and_medium_bar.one_condition_bar(
            means=means,
            err=err,
            title=title,
            ylabel=ylabel,
            xlabel=xlabel,
            sig=sig,
            f_name=f_name
        )


def run_fit_simulation():

    """
    fit model on experimental data
    TODO: Does it still work?

    """

    data = pickle.load(open('data/fit.p', 'rb'))

    for r_id in analysis.tools.economy.labels.keys():

        # after reformatting
        data_fit = analysis.tools.format.for_fit(data)

        label = analysis.tools.economy.labels.get(r_id)

        cognitive_parameters = data_fit[label]

        repartition = analysis.tools.economy.repartitions.get(r_id)

        simulation.economy.launch(
            agent_model='RLAgent',
            repartition=repartition,
            t_max=50,
            economy_model='prod: i-1',
            cognitive_parameters=cognitive_parameters,
            seed=123
        )

        # SOMETHING TO DO HERE
        # res['repartition'] = repartition
        #
        # analysis.graph.monetary_and_medium.one_condition(res, f_name=f"sim_{label}.pdf")


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
    medium = analysis.compute.strategy_count_pool.run()

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

        analysis.graph.monetary_and_medium.overall_one_good(data, titles, f_name=f'fig/xp_{good}.pdf', exp=True)


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

        analysis.graph.monetary_and_medium.overall_one_good(
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

    # exp_overall()
    # analysis.graph.monetary_and_medium.overall_one_condition_example()
    # sim_overall()
    # bar_plots()
    # phase_diagram()
    # sim_overall()
    # exp_overall()
    # phase_diagram()
    # sim_overall()
    stats_sim()
    # analysis.compute.demographics.run()
    # analysis.graph.monetary_and_medium.overall_one_condition_example()
    # sim_overall()
    # exp_overall()
    # run_simulations()
    # run_experiment()
    # bar_plots()
    # run_simulations()
    # bar_plots()
    # phase_diagram()
