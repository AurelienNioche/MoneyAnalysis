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
# from analysis import demographics, medium, monetary_behavior, strategy, life_expectancy, \
#     strategy_count, strategy_count_pool, monetary_behavior_pool
# import graph.strategy
# import graph.life_expectancy
# import graph.strategy_count_pool

import RL.optimize
# import WSS.optimize
import simulation.economy
import simulation.data_format
import graph.graph

import RL.simulation.format_data
import analysis.tools.economy_labels
import analysis.tools.economy_repartitions
import analysis.monetary_and_medium
import RL.optimize


def plot_data(data, f_name=None):
    coord = it.product(range(2), range(3))
    gs = grd.GridSpec(nrows=2, ncols=3)

    fig = plt.figure()

    for i in range(len(data['repartition'])):
        data_mbh = simulation.data_format.for_monetary_behavior_over_t(data['monetary_bhv'][i], data['repartition'])

        graph.graph._monetary_behavior_over_t(data=data_mbh, fig=fig, subplot_spec=gs[next(coord)], title=f'm={i}')

    data_m = simulation.data_format.for_medium_over_t(data['medium'], data['repartition'])
    graph.graph._medium_over_t(data=data_m, fig=fig, subplot_spec=gs[next(coord)])

    plt.tight_layout()

    if f_name is not None:
        os.makedirs('fig', exist_ok=True)
        plt.savefig(f'fig/{f_name}')


def run_experiment():
    data = analysis.monetary_and_medium.run()

    for label, room_data in data.items():
        plot_data(room_data, f_name=f'xp_{label}.pdf')


def run_simulation():
    for r_id in analysis.tools.economy_labels.mapping.keys():
        data_fit = RL.simulation.format_data.run()

        label = analysis.tools.economy_labels.get(r_id)

        cognitive_parameters = data_fit[label]

        repartition = analysis.tools.economy_repartitions.get(r_id)

        res = simulation.economy.launch(
            agent_model='RLAgent',
            repartition=repartition,
            t_max=50,
            economy_model='prod: i-1',
            cognitive_parameters=cognitive_parameters,
            seed=123
        )
        res['repartition'] = repartition

        plot_data(res, f_name=f"sim_{label}.pdf")


def main():

    run_experiment()
    run_simulation()

    RL.optimize.main(f_name='hist.pdf')

    # demographics.run()

    # data = {
    #     "3_good_non_uniform_monetary_behavior": np.random.random((3, 50)),
    #     "3_good_non_uniform_medium": np.random.random((3, 50)),
    #     "3_good_uniform_monetary_behavior": np.random.random((3, 50)),
    #     "3_good_uniform_medium": np.random.random((3, 50)),
    #     "4_good_non_uniform_monetary_behavior": np.random.random((4, 50)),
    #     "4_good_non_uniform_medium": np.random.random((4, 50)),
    #     "4_good_uniform_monetary_behavior": np.random.random((4, 50)),
    #     "4_good_uniform_medium": np.random.random((4, 50)),
    #     "money_bar_mean": np.random.random(4),
    #     "money_bar_std": np.random.random(4) / 100,
    # }
    #
    # # data.update(monetary_behavior.run())
    # data.update(medium.run())
    # graph.make_figs(data)

    # data = life_expectancy.run()
    # graph.life_expectancy.plot(data, f_name="fig/life_expectancy.pdf")

    # for m in range(4):
    #     data = strategy.run(m=m)
    #     graph.strategy.plot(data, m_color=f'C{m}', f_name=f'fig/strategy_m{m}.pdf')
    #
    # m = 5
    # data = strategy.run(m=m, order_by_m=False)
    # graph.strategy.plot(data, m_color=f'C{m}', f_name=f'fig/strategy_m{m}.pdf')

    # strategy_count.run()

    # data = strategy_count_pool.run()
    # graph.strategy_count_pool.plot(data, f_name=f'fig/strategy_count_pool.pdf')

    # data = monetary_behavior_pool.run()
    # graph.strategy_count_pool.plot(data, suffix='_monetary_behavior_pool',
    #                                f_name=f'fig/monetary_behavior_pool.pdf')

    # RL.optimize.run()
    # WSS.optimize.run()


if __name__ == '__main__':

    # main()
    # run_simulation()

    main()
