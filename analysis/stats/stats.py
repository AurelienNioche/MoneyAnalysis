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


def format_p_value(p, threshold=0.05):

    f = '$'

    if p >= 0.001:
        f += f"{p:.3f}"
    else:
        f += '<0.001'

    if p < threshold:
        f += '^*$'
    else:
        f += '$'
    return f


def mann_whitney(to_compare, print_latex=False, **kwargs):

    ns = []
    ps = []
    us = []

    for dic in to_compare:
        u, p = scipy.stats.mannwhitneyu(dic["data"][0], dic["data"][1])
        n = len(dic["data"][0]) + len(dic["data"][1])
        ps.append(p)
        us.append(u)
        ns.append(n)

    if not len(ns):
        return

    valid, p_corr, alpha_c_sidak, alpha_c_bonf = \
        statsmodels.stats.multitest.multipletests(pvals=ps, alpha=0.05,
                                                  method="b")

    for p, u, n, p_c, v, dic in zip(ps, us, ns, p_corr, valid, to_compare):

        if print_latex:

            comparison = dic["comparison"]

            xp_label = kwargs["xp_label"]
            measure = kwargs["measure"]

            corr = p_c != p

            p_c = f"{p_c:.3f}" if p_c >= 0.001 else '<0.001'
            p = f"{p:.3f}" if p >= 0.001 else '<0.001'

            part0 = f"{xp_label} & {comparison} & {measure} & $U$ & ${u}$ & ${p}"
            if corr:
                part0 += f"$ & ${p_c}"
            part1 = f"{'^*' if v else ''}$ & ${n}$" + r"\\"
            print(part0 + part1)

        else:
            cond_name = dic['name']
            print(
                f"[{cond_name}] Mann-Whitney rank test: $u={u}$, "
                f"$p corr={p_c:.3f}$, p raw {p:.3f}, $n={n}$, sign.: {v}")

    return p_corr


def sim_and_xp(data, data_type=('Human', 'Simulation'),
               conditions=('Uniform', 'Non-uniform'),
               name_extension='', print_latex=True,
               comparison='Agent type dist.',
               measure='Ind. good 1'):

    # keys: ngood, HUMAN/SIM, agent_type, UNIF/NON-UNIF (1, 0)
    # Main tests
    print(SEP)
    print(f'MAIN SIM AND XP TESTS {name_extension}')
    print(SEP)

    human, sim = data_type
    unif, non_unif = conditions

    to_compare = [
        {
            'data': np.array([
                data[3][sim][2][unif],
                data[3][sim][2][non_unif],
            ]),
            'name': 'SIM, 3 GOODS, UNIF vs. NON-UNIF, '
                    'agent_type=2, obs=ind_0',
            'comparison':
                'Agent type dist. in artificial agents of type (2, 3)'
        }, ]
    mann_whitney(to_compare=to_compare, print_latex=print_latex,
                 xp_label='3 goods', measure=measure,
                 comparison=comparison)

    to_compare = [
        {
            'data': np.array([
                data[3][human][2][unif],
                data[3][human][2][non_unif],
            ]),
            'name': 'HUMAN, 3 GOODS, UNIF vs. NON-UNIF, '
                    'agent_type=2, obs=ind_0',
            'comparison':
                'Agent type dist. in human agents of type (2, 3)'
        },
    ]

    mann_whitney(to_compare=to_compare, print_latex=print_latex,
                 xp_label='3 goods', measure=measure,
                 comparison=comparison)

    to_compare = [
        {
            'data': np.array([
                data[4][sim][2][unif],
                data[4][sim][2][non_unif],
            ]),
            'name': 'SIM, 4 GOODS, UNIF vs. NON-UNIF, '
                    'agent_type=2, obs=ind_0',
            'comparison':
                'Agent type dist. in artificial agents of type (2, 3)'
        },
        {
            'data': np.array([
                data[4][sim][3][unif],
                data[4][sim][3][non_unif],
            ]),
            'name': 'SIM, 4 GOODS, UNIF vs. NON-UNIF, '
                    'agent_type=3, obs=ind_0',
            'comparison':
                'Agent type dist. in artificial agents of type (3, 4)'
        },
    ]

    mann_whitney(to_compare=to_compare, print_latex=print_latex,
                 xp_label='4 goods', measure=measure,
                 comparison=comparison)

    to_compare = [
        {
            'data': np.array([
                data[4][human][2][unif],
                data[4][human][2][non_unif],
            ]),
            'name': 'HUMAN, 4 GOODS, UNIF vs. NON-UNIF, '
                    'agent_type=2, obs=ind_0',
            'comparison':
                'Agent type dist. in human agents of type (2, 3)'
        },
        {
            'data': np.array([
                data[4][human][3][unif],
                data[4][human][3][non_unif],
            ]),
            'name': 'HUMAN, 4 GOODS, UNIF vs. NON-UNIF, '
                    'agent_type=3, obs=ind_0',
            'comparison':
                'Agent type dist. in human agents of type (3, 4)'
        }
    ]

    mann_whitney(to_compare=to_compare, print_latex=print_latex,
                 xp_label='4 goods', measure=measure,
                 comparison=comparison)


def supplementary_age(data, print_latex=True):

    measure_label = 'Ind. good 1'

    print(SEP)
    print(f'SUPPLEMENTARY AGE TEST')
    print(SEP)

    for n_good in data.keys():

        n = len(data[n_good]['obs'])

        cor, p = scipy.stats.pearsonr(
            data[n_good]['age'],
            data[n_good]['obs']
        )

        if print_latex:
            print(f'{n_good} goods & Age & {measure_label} & '
                  f'$r_pearson$ & {cor:.2f}$ & ${p:.3f} & ${n}$\\\\')
        else:
            print(f'[{n_good} goods] Pearson corr age - measure: '
                  f'$r_pearson={cor:.2f}$, $p={p:.3f}$')

    print(SEP)


def supplementary_gender(data, print_latex=True):

    measure_label = 'Ind. good 1'

    print(SEP)
    print('SUPPLEMENTARY GENDER TEST')
    print(SEP)

    for n_good in data.keys():

        mann_whitney(to_compare=[{
            'data': np.array([data[n_good]['Male'], data[n_good]['Female']]),
            'name': f'MALE VS FEMALE, & {measure_label}',
            'comparison': 'Gender'
        }],
            print_latex=print_latex,
            xp_label=f'{n_good} goods',
            measure=measure_label,
            )
    print()


def parameter_recovery(data, print_latex=True):

    print(SEP)
    print(f'SUPPLEMENTARY PARAM RECOVERY TEST')
    print(SEP)

    for param, (value, r_value) in sorted(data.items()):

        n = len(value)

        cor, p = scipy.stats.pearsonr(
            value,
            r_value
        )

        if print_latex:
            print(f'$\{param}$ & ' +
                  '$r_{pearson}$ & ' +
                  f'${cor:.2f}$ & {format_p_value(p)} & ${n}$')

        else:
            print(f'Pearson corr: $r_pearson={cor:.2f}$, $p={p:.3f}$')


def cross_validation(data):

    mann_whitney(to_compare=[{
            'data': np.array([data['UNIF'], data['NON-UNIF']]),
            'name': 'CROSS-VALIDATION obs_type=ind_0'
        }])


def sensitivity_analysis(data):

    print(SEP)
    print('Sensitivity analysis')
    print(SEP)

    for n_good in data.keys():

        xp_label = f'{n_good} goods'

        parameters = sorted([i for i in data[n_good].keys() if i[0] == '$'])

        h = []
        p = []
        n = []

        for param in parameters:

            x_ticks = np.unique(data[n_good][param])

            values_box_plot = [[] for _ in range(len(x_ticks))]

            for idx, x in enumerate(x_ticks):
                not_nan = np.invert(np.isnan(data[n_good]['ind0']))
                relevant = data[n_good][param] == x
                values = data[n_good]['ind0'][relevant * not_nan]
                values_box_plot[idx] += list(values)

            # Kruskal-Wallis H-test
            _h, _p = scipy.stats.kruskal(*values_box_plot)
            h.append(_h)
            p.append(_p)
            n.append(np.sum([len(i) for i in values_box_plot]))

        valid, p_corr, alpha_c_sidak, alpha_c_bonf = \
            statsmodels.stats.multitest.multipletests(pvals=p, alpha=0.05,
                                                      method="b")

        for i in range(len(p)):

            comparison = f'{parameters[i]}-value'
            measure = 'Ind. good 1'

            corr = p_corr[i] != p[i]

            p_c = f"{p_corr[i]:.3f}" if p_corr[i] >= 0.001 else '<0.001'
            p_raw = f"{p[i]:.3f}" if p[i] >= 0.001 else '<0.001'

            part0 = f"{xp_label} & {comparison} & {measure} & $H$ & " \
                f"${h[i]:.2f}$ & ${p_raw}"
            if corr:
                part0 += f"$ & ${p_c}"
            part1 = f"{'^*' if valid[i] else ''}$ & ${n[i]}$" + r"\\"

            print(part0 + part1)


if __name__ == "__main__":
    exit('Run the additional_info.py.old script.')
