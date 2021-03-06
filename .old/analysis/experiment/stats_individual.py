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
import scipy.stats
import statsmodels.stats.multitest

from analysis.experiment.individual import individual_data, Dyn
from analysis.experiment.evolution import evolution_direct_split


def get_groups(static_data, dynamic_data, n_split, const, rooms_id, agent_type):

    data = evolution_direct_split(static_data, dynamic_data, n_split, const)
    to_return = []
    for r_id in rooms_id:

        d = data[r_id][agent_type][-1]
        to_return.append(d)

        # cons_g_bool = static_data[:, Stc.CONS] == g
        # belong_r_bool = static_data[:, Stc.ROOM] == r_id
        #
        # cons_belong_r_bool = cons_g_bool * belong_r_bool
        #
        # raw = dynamic_data[cons_belong_r_bool, :, const]
        # bnd = round(len(dynamic_data[0, :]) * span)
        #
        # selected = raw[:, -bnd:]
        # d = np.mean(selected, axis=1)
        # print("n", d.shape[0])
        # data.append(d)

    return to_return


def _mw(to_compare, print_latex=False, **kwargs):

    ns = []

    ps = []
    us = []

    for dic in to_compare:
        try:
            u, p = scipy.stats.mannwhitneyu(dic["data"][0], dic["data"][1])  # , alternative="two-sided")
            n = len(dic["data"][0]) + len(dic["data"][1])
            ps.append(p)
            us.append(u)
            ns.append(n)
        except ValueError as e:
            print(e)

    if not len(ns):
        return

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

    consts = [k for k in vars(Dyn) if not k.startswith('_') and k not in ("NP", "N_VAR")]

    for (room1, name1), (room2, name2) in zip(
            [(416, '3G U'), (415, '4G U')], [(414, '3G NU'), (417, '4G NU')]):

        print(f'{name1} vs. {name2}')

        for const in consts:

            print("*" * 10)
            print(const)

            for g in range(int(name1[0])):
                print('-' * 10)
                print("CONS", g)

                print(f'{name1} vs. {name2}')

                grouped_data = get_groups(
                    static_data, dynamic_data, n_split=3, const=getattr(Dyn, const), rooms_id=[room1, room2],
                    agent_type=g
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
