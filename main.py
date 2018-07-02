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
from analysis import demographics, medium, monetary_behavior
from graph import graph


def main():

    demographics.run()

    data = {
        "3_good_non_uniform_monetary_behavior": np.random.random((3, 50)),
        "3_good_non_uniform_medium": np.random.random((3, 50)),
        "3_good_uniform_monetary_behavior": np.random.random((3, 50)),
        "3_good_uniform_medium": np.random.random((3, 50)),
        "4_good_non_uniform_monetary_behavior": np.random.random((4, 50)),
        "4_good_non_uniform_medium": np.random.random((4, 50)),
        "4_good_uniform_monetary_behavior": np.random.random((4, 50)),
        "4_good_uniform_medium": np.random.random((4, 50)),
        "money_bar_mean": np.random.random(4),
        "money_bar_std": np.random.random(4) / 100,
    }

    data.update(medium.run())
    data.update(monetary_behavior.run())

    graph.make_figs(data)


if __name__ == '__main__':

    main()
