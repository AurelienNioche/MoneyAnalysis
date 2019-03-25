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
SCRIPT_FOLDER = os.path.dirname(os.path.abspath(__file__))
sys.path.append(f"{SCRIPT_FOLDER}/../../")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MoneyAnalysis.settings")

# Ensure settings are read
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

import numpy as np
import matplotlib.pyplot as plt

from game.models import Room
from analysis.experiment.individual import individual_data, CONS, ROOM, \
    D_IND_0, D_IND_1, D_IND_2, D_IND_3, D_DIRECT, FIG_FOLDER


def evolution_direct_split(static_data, dynamic_data, n_split, const):

    data = {}
    rooms = Room.objects.all().order_by('id')
    rooms_id = [r.id for r in rooms]

    for r_id in rooms_id:

        r = Room.objects.get(id=r_id)
        n_good = r.n_type

        data_room = []

        for g in range(n_good):

            cons_g_bool = static_data[:, CONS] == g
            belong_r_bool = static_data[:, ROOM] == r_id

            cons_belong_r_bool = cons_g_bool*belong_r_bool
            n = int(np.sum(cons_belong_r_bool))

            raw = dynamic_data[cons_belong_r_bool, :, const]
            tmax = len(dynamic_data[0, :])
            spl = tmax//n_split
            bnds = np.arange(tmax+1, step=spl)

            points = [[] for _ in range(n_split)]

            for i in range(n):
                for j, k in enumerate(bnds):
                    if k != bnds[-1]:
                        data_ind = np.mean(raw[i, k:bnds[j+1]])
                        points[j].append(data_ind)

            data_room.append(points)

        data[r_id] = data_room
    return data


def fig_evo_scatter(data_evo, title, f_name=None):

    rooms_id = list(data_evo.keys())
    rooms_id.sort()

    rooms_id = [416, 414, 415, 417]

    colors = [f"C{i}" for i in range(4)]

    fig, ax = plt.subplots(ncols=4, nrows=4, figsize=(20, 20))

    fig.suptitle(title)
    print(f'Doing {title}')

    for idx, r_id in enumerate(rooms_id):

        data_room = data_evo[r_id]

        n_good = len(data_room)
        n_split = len(data_room[0])

        for g in range(n_good):

            n_sub = len(data_room[g][0])
            print(f'Room={r_id}, ngood={n_good}, good={g}, nsub={n_sub}')

            for n in range(n_sub):

                sub = []

                for s in range(n_split):

                    data_sub = data_room[g][s][n]
                    sub.append(data_sub)

                    ax[idx, g].scatter([s], [data_sub], color=colors[g], alpha=0.5)

                assert len(sub) == n_split
                ax[idx, g].plot(range(n_split), sub, color=colors[g], alpha=0.5)
                ax[idx, g].set_xlim([-0.15, n_split-0.85])
                ax[idx, g].set_ylim([-.02, 1.02])
                ax[idx, g].set_xticks([])
                ax[idx, g].set_yticks([0, 0.25, 0.5, 0.75, 1.])

    if f_name:
        plt.savefig(f"{FIG_FOLDER}/{f_name}")
    else:
        plt.show()


def main():

    static_data, dynamic_data = individual_data()

    for name, const in zip(('D_IND_0', 'D_IND_1', 'D_IND_2', 'D_IND_3', 'D_DIRECT'),
                           (D_IND_0, D_IND_1, D_IND_2, D_IND_3, D_DIRECT)):
        data_evo = evolution_direct_split(static_data, dynamic_data, n_split=3, const=const)
        fig_evo_scatter(data_evo, title=name, f_name=f'individual_tracking_{name}.pdf')


if __name__ == "__main__":

    main()
