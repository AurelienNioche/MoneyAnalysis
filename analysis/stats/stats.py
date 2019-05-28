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

SEP = '-' * 30


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


def sim_and_xp(data, name_extension=''):
    # keys: ngood, HUMAN/SIM, agent_type, UNIF/NON-UNIF (1, 0)
    # Main tests
    print(SEP)
    print(f'MAIN SIM AND XP TESTS {name_extension}')
    print(SEP)

    to_compare = [
        {
            'data': np.array([
                data[3]['HUMAN'][2]['UNIF'],
                data[3]['HUMAN'][2]['NON-UNIF'],
            ]),
            'name': 'HUMAN, 3 GOODS, UNIF vs. NON-UNIF, agent_type=2, obs=ind_0'
        },

        {
            'data': np.array([
                data[3]['SIM'][2]['UNIF'],
                data[3]['SIM'][2]['NON-UNIF'],
            ]),
            'name': 'SIM, 3 GOODS, UNIF vs. NON-UNIF, agent_type=2, obs=ind_0'
        }
    ]

    _mw(to_compare=to_compare)

    to_compare = [
        {
            'data': np.array([
                data[4]['HUMAN'][2]['UNIF'],
                data[4]['HUMAN'][2]['NON-UNIF'],
            ]),
            'name': 'HUMAN, 4 GOODS, UNIF vs. NON-UNIF, agent_type=2, obs=ind_0'
        },
        {
            'data': np.array([
                data[4]['SIM'][2]['UNIF'],
                data[4]['SIM'][2]['NON-UNIF'],
            ]),
            'name': 'SIM, 4 GOODS, UNIF vs. NON-UNIF, agent_type=2, obs=ind_0'
        },
        {
            'data': np.array([
                data[4]['HUMAN'][3]['UNIF'],
                data[4]['HUMAN'][3]['NON-UNIF'],
            ]),
            'name': 'HUMAN, 4 GOODS, UNIF vs. NON-UNIF, agent_type=3, obs=ind_0'
        },
        {
            'data': np.array([
                data[4]['SIM'][3]['UNIF'],
                data[4]['SIM'][3]['NON-UNIF'],
            ]),
            'name': 'SIM, 4 GOODS, UNIF vs. NON-UNIF, agent_type=3, obs=ind_0'
        }
    ]

    _mw(to_compare=to_compare)


def supplementary_age(data):

    for n_good in data.keys():
        print(SEP)
        print(f'SUPPLEMENTARY AGE TEST FOR N_GOOD = {n_good}')
        print(SEP)

        cor, p = scipy.stats.pearsonr(
            data[n_good]['age'],
            data[n_good]['obs']
        )

        print(f'Pearson corr age - measure : $r_pearson={cor:.2f}$, $p={p:.3f}$')


def supplementary_gender(data):

    for n_good in data.keys():
        print(SEP)
        print(f'SUPPLEMENTARY GENDER TEST FOR N_GOOD = {n_good}')
        print(SEP)

        _mw(to_compare=[{
            'data': np.array([data[n_good]['MALE'], data[n_good]['FEMALE']]),
            'name': 'MALE VS FEMALE, obs=dir'
        }])

        print(SEP)


def parameter_recovery(data):

    for param, (value, r_value) in sorted(data.items()):
        print(SEP)
        print(f'SUPPLEMENTARY PARAM RECOVERY TEST FOR PARAM = {param}')
        print(SEP)

        cor, p = scipy.stats.pearsonr(
            value,
            r_value
        )

        print(f'Pearson corr: $r_pearson={cor:.2f}$, $p={p:.3f}$')


if __name__ == "__main__":
    exit('Run the main.py script.')
