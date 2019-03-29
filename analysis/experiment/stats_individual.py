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
import scipy.stats
import statsmodels

from analysis.experiment.individual import individual_data, CONS, ROOM, \
    D_IND_0, D_IND_1, D_IND_2, D_IND_3, D_DIRECT, FIG_FOLDER


def get_groups(static_data, dynamic_data, span, const, rooms_id, g):

    data = []
    for r_id in rooms_id:

        cons_g_bool = static_data[:, CONS] == g
        belong_r_bool = static_data[:, ROOM] == r_id

        cons_belong_r_bool = cons_g_bool * belong_r_bool

        raw = dynamic_data[cons_belong_r_bool, :, const]
        bnd = round(len(dynamic_data[0, :]) * span)

        data.append(raw[:, -bnd:])

    return data


def _mw(to_compare, print_latex=False, **kwargs):

    ns = []

    print(to_compare)
    ps = []
    us = []

    for dic in to_compare:
        u, p = scipy.stats.mannwhitneyu(dic["data"][0], dic["data"][1])
        n = len(dic["data"][0]) + len(dic["data"][1])
        ps.append(p)
        us.append(u)
        ns.append(n)

    valid, p_corr, alpha_c_sidak, alpha_c_bonf = \
        statsmodels.stats.multitest.multipletests(pvals=ps, alpha=0.05, method="b")

    for p, u, n, p_c, v, dic in zip(ps, us, ns, p_corr, valid, to_compare):
        cond_name = dic['name']
        f_name = cond_name.replace("good", "").replace("_", "").replace("vs", ", ")

        if print_latex:
            xp_session = kwargs["xp_session"]
            measure = kwargs["measure"]
            p_c = f"{p_c:.3f}" if p_c >= 0.001 else '<0.001'
            p = f"{p:.3f}" if p >= 0.001 else '<0.001'
            print(f"{xp_session} & {measure} & ${f_name}$ & ${u}$ & ${p}$ & ${p_c}{'^*' if v else ''}$ & ${n}$" + r"\\")

        else:
            print(f"[{cond_name}] Mann-Whitney rank test: $u={u}$, $p={p_c:.3f}$, p raw {p:.3f}, $n={n}$, sign.: {v}")

    return p_corr


def main():

    static_data, dynamic_data = individual_data()

    # for name, const in zip(('D_IND_0', 'D_IND_1', 'D_IND_2', 'D_IND_3', 'D_DIRECT'),
    #                        (D_IND_0, D_IND_1, D_IND_2, D_IND_3, D_DIRECT)):
    #     data_evo = evolution_direct_split(static_data, dynamic_data, n_split=3, const=const)
    #     fig_evo_scatter(data_evo, title=name, f_name=f'individual_tracking_{name}.pdf')
    room_ids = [416, 414]
    grouped_data = get_groups(static_data, dynamic_data, span=.33, const=D_IND_0, rooms_id=[416, 414], g=2)
    print(grouped_data)

    to_compare = [
            {
                "data": np.array(grouped_data),
                "name": f"rm_{room_ids[0]}_vs_rm_{room_ids[1]}"
            }
        ]

    p = _mw(to_compare, print_latex=True,)
    print(p)


if __name__ == "__main__":

    main()