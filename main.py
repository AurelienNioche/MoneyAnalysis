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

import analysis.compute.monetary_behavior
import analysis.compute.strategy_count_pool

import analysis.stats.mean_comparison


def stats_exp():

    # --------------- Monetary bhv ------------------------ #

    data = analysis.compute.monetary_behavior.run()

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

    data = analysis.compute.monetary_behavior.run()

    xlabel = 'Good'
    ylabel = 'Monetary behavior'

    for k, v in data.items():

        sig = analysis.stats.mean_comparison.monetary_behavior(v['monetary_bhv'])
        title = k
        means, err = analysis.tools.format.for_monetary_behavior_bar_plot(v['monetary_bhv'])
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
        means, err = analysis.tools.format.for_medium_bar_plot(v['medium'])
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


def run_simulation():

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
        f_name=f_name
    )


def exp_overall():

    monetary = analysis.compute.monetary_behavior.run()
    medium = analysis.compute.strategy_count_pool.run()

    # monetary_over_t = analysis.compute.monetary_behavior.run()

    keys = monetary.keys()

    for k in keys:

        med_t = monetary[k]['medium']
        med_bar = medium[k]['medium']
        m_bhv = monetary[k]['monetary_bhv']
        repartition = monetary[k]['repartition']

        monetary_means, monetary_err = analysis.tools.format.for_monetary_behavior_bar_plot(m_bhv)
        monetary_over_t = analysis.tools.format.for_monetary_behavior_over_t(m_bhv, repartition)

        medium_means, medium_err = analysis.tools.format.for_medium_bar_plot(med_bar)
        medium_over_t = analysis.tools.format.for_medium_over_t(med_t, repartition)

        data = {
            'monetary_bar': (monetary_means, monetary_err),
            'monetary_over_t': monetary_over_t,
            'medium_bar': (medium_means, medium_err),
            'medium_over_t': medium_over_t,
            'repartition': repartition
        }

        analysis.graph.monetary_and_medium.overall_one_condition(data=data, title=k, f_name=f'fig/overall_exp_{k}.pdf')


def sim_overall():

    data = backup.load('data/exp_like.p')


def run_simulations():

    """
    runs simulations with
    command line arguments
    """

    simulation.runner.run()


def main():
    run_simulations()


if __name__ == '__main__':

    # main()

    # bar_plots()
    # phase_diagram()
    # sim_overall()

    exp_overall()
    # run_experiment()
    # run_simulations()
    # bar_plots()
    # phase_diagram()
