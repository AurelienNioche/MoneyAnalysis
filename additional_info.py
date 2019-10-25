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

from backup import backup

import simulation.run

import analysis.supplementary


def main_reward():

    analysis.supplementary.reward()


def n_eco():

    print('[3 goods]', end=' ')
    simulation.run.get_data(fake=True, n_good=3)
    print()
    print('[4 goods]', end=' ')
    simulation.run.get_data(fake=True, n_good=4)
    print()


def n_eco_asym():

    print('[3 goods - Asym]', end=' ')
    print(len(backup.load("data/phase_3_goods_asymmetric/seed.p")))
    print()
    print('[4 goods - Asym]', end=' ')
    print(len(backup.load("data/phase_3_goods_asymmetric/seed.p")))


if __name__ == '__main__':

    n_eco()
    n_eco_asym()
    main_reward()
