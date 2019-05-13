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
import sys

from analysis.experiment.graph import fig_evo_scatter
from analysis.experiment.tools import running_mean

SCRIPT_FOLDER = os.path.dirname(os.path.abspath(__file__))
sys.path.append(f"{SCRIPT_FOLDER}/../../")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MoneyAnalysis.settings")

# Ensure settings are read
from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()

import numpy as np

from game.models import Room
# from analysis.experiment.individual import individual_data, CONS, ROOM, \
# D_IND_0, D_IND_1, D_IND_2, D_IND_3, D_DIRECT

from analysis.experiment.individual import Stc, Dyn, individual_data
from analysis.experiment import metric


def get_windowed_observation(dir_ex, ind_ex, n, n_split, n_good):

    tmax = len(n)
    step = tmax // n_split
    bounds = np.arange(tmax+1, step=step)
    averaged_dir_ex = np.zeros(n_good, dtype=float)
    averaged_ind_ex = np.zeros(n_good, dtype=float)

    for good in range(n_good):

        for i_bound in range(len(bounds) - 1):

            # set inferior and superior bound
            inf = bounds[i_bound]
            sup = bounds[i_bound+1]

            # get windowed data
            windowed_ind = ind_ex[inf:sup, good]
            windowed_dir = dir_ex[inf:sup]
            n_possibility = n[inf:sup]

            # If it is not the first window normalize, otherwise no (minus 0)
            # normalized by the number of attempts
            last_data_ind = ind_ex[inf - 1, good] if i_bound != 0 else 0
            last_data_dir = dir_ex[inf - 1] if i_bound != 0 else 0
            last_n = n[inf - 1] if i_bound != 0 else 0

            norm_windowed_ind = windowed_ind - last_data_ind
            norm_windowed_dir = windowed_dir - last_data_dir

            norm_n_possibility = n_possibility - last_n

            ind_to_compute = []
            dir_to_compute = []
            # idx = 0
            for ex_type, norm in zip(
                    [ind_to_compute, dir_to_compute], [norm_windowed_ind, norm_windowed_dir]):
                for x, y in zip(norm,  norm_n_possibility):

                    if y > 0:
                        ex_type.append(x/y)
                    # idx += 1

            averaged_dir_ex = np.mean(dir_to_compute)
            averaged_ind_ex[good] = np.mean(ind_to_compute)

    return averaged_dir_ex, averaged_ind_ex


def main():

    dir_ex, ind_ex, n = metric.exchange(n_good=3, )




if __name__ == '__main__':
    main()
