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

import numpy as np
from analysis import demographics, medium, monetary_behavior, strategy, life_expectancy, \
    strategy_count, strategy_count_pool
import graph.strategy
import graph.life_expectancy


def main():

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
    # data.update(monetary_behavior.run())
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

    strategy_count_pool.run()

if __name__ == '__main__':

    main()
