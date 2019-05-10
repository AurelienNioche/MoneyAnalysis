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
import statsmodels.stats.multitest

from analysis.experiment.individual import individual_data, Dyn, Stc


def get_groups(static_data, dynamic_data, span, const, rooms_id, g):

    data = []
    for r_id in rooms_id:

        cons_g_bool = static_data[:, Stc.CONS] == g
        belong_r_bool = static_data[:, Stc.ROOM] == r_id

        cons_belong_r_bool = cons_g_bool * belong_r_bool

        raw = dynamic_data[cons_belong_r_bool, :, const]
        bnd = round(len(dynamic_data[0, :]) * span)

        data.append(np.mean(raw[:, -bnd:], axis=1))

    return data


def _mw(to_compare, print_latex=False, **kwargs):

    ns = []

    ps = []
    us = []

    for dic in to_compare:
        u, p = scipy.stats.mannwhitneyu(dic["data"][0], dic["data"][1], alternative="two-sided")
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
            print(
                f"[{cond_name}] Mann-Whitney rank test: $u={u}$, $p corr={p_c:.3f}$, p raw {p:.3f}, $n={n}$, sign.: {v}")

    return p_corr


def main():

    static_data, dynamic_data = individual_data()

    # 414 3G non-uniform
    # 415 4G  uniform
    # 416 3G uniform
    # 417 4G non-uniform

    consts = [k for k in vars(Dyn) if not k.startswith('_') and k != "NP"]

    for const in consts:
        print(const)
        for (room1, name1),  (room2, name2) in zip(
                [(415, '3G U'), (416, '4G U')], [(417, '3G NU'), (414, '4G NU')]):

            print(f'{name1} vs. {name2}')

            grouped_data = get_groups(
                static_data, dynamic_data, span=.5, const=const, rooms_id=[room1, room2], g=1
            )

            to_compare = [
                    {
                        "data": np.array(grouped_data),
                        "name": f"rm_{room1}_vs_rm_{room2}"
                    }
                ]

            p = _mw(to_compare)
            print(p)
            print()


if __name__ == "__main__":

    main()