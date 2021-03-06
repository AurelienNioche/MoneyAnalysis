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


def evolution_direct_split(static_data, dynamic_data, n_split, const):

    """
    :param static_data:
    :param dynamic_data:
    :param n_split:
    :param const:
    :return:
    dictionary.
     * Key: number of room.
     * Value: nested list with dimenions: type of agent, time window, individual
    """
    data = {}
    rooms = Room.objects.all().order_by('id')
    rooms_id = [r.id for r in rooms]

    for r_id in rooms_id:

        r = Room.objects.get(id=r_id)
        n_good = r.n_type

        data_room = []

        for agent_type in range(n_good):

            cons_g_bool = static_data[:, Stc.CONS] == agent_type
            belong_r_bool = static_data[:, Stc.ROOM] == r_id

            cons_belong_r_bool = cons_g_bool * belong_r_bool
            n = int(np.sum(cons_belong_r_bool))

            raw = dynamic_data[cons_belong_r_bool, :, const]
            raw_n = dynamic_data[cons_belong_r_bool, :, Dyn.NP]
            tmax = len(dynamic_data[0, :, 0])
            spl = tmax // n_split
            bnds = np.arange(tmax+1, step=spl)

            points = [[] for _ in range(n_split)]

            # for each subject
            for i in range(n):
                # for each bound (window, nsplit)
                for j in range(len(bnds) - 1):

                    inf = bnds[j]
                    sup = bnds[j+1]

                    data_window = raw[i, inf:sup]

                    if j != 0:
                        last_data = raw[i, inf - 1]
                        last_n = raw_n[i, inf - 1]
                    else:
                        last_data = 0
                        last_n = 0

                    norm_data_window = data_window - last_data

                    n_possibility = raw_n[i, inf:sup]
                    norm_n_possibility = n_possibility - last_n

                    to_compute = []
                    idx = 0
                    for x, y in zip(norm_data_window, norm_n_possibility):

                        if y > 0:
                            to_compute.append(x/y)
                        idx += 1

                    # assert((min(to_compute), max(to_compute))

                    data_ind = np.mean(to_compute)

                    points[j].append(data_ind)

            data_room.append(points)

        data[r_id] = data_room
    return data


def evolution_direct(static_data, dynamic_data, window_size=5):

    data = {}
    rooms = Room.objects.all().order_by('id')
    rooms_id = [r.id for r in rooms]

    for r_id in rooms_id:

        r = Room.objects.get(id=r_id)
        n_good = r.n_type
        data_room = []

        for g in range(n_good):

            cons_g_bool = static_data[:, Stc.CONS] == g
            belong_r_bool = static_data[:, Stc.ROOM] == r_id

            cons_belong_r_bool = cons_g_bool * belong_r_bool
            n = int(np.sum(cons_belong_r_bool))

            raw = dynamic_data[cons_belong_r_bool, :, Dyn.DIRECT]
            data_good = []
            for i in range(n):
                r_mean = running_mean(raw[i], n=window_size)
                data_ind = r_mean
                data_good.append(data_ind)

            data_room.append(data_good)

        data[r_id] = data_room

    return data


def main():
    static_data, dynamic_data = individual_data()

    consts = [k for k in vars(Dyn) if not k.startswith('_') and k not in ["NP", "N_VAR"]]
    for const in consts:
        print(const)
        data_evo = evolution_direct_split(static_data, dynamic_data, n_split=3, const=getattr(Dyn, const))
        fig_evo_scatter(data_evo, title=const, f_name=f'individual_tracking_{const}.pdf')


if __name__ == "__main__":
    main()
