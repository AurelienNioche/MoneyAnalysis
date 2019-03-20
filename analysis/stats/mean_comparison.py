import numpy as np
import scipy.stats
import statsmodels.stats.multitest


comparisons = {
    3: [
            (0, 1),
            (0, 2),
    ],
    4: [
        (0, 1),
        (0, 2),
        (0, 3)
    ]
}


def _mw(to_compare, print_latex=False, **kwargs):

    ns = []

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


def run(data, print_latex=False, **kwargs):

    cp = comparisons[len(data)]

    to_compare = []

    for g1, g2 in cp:

        to_compare.append(
            {
                "data": np.array([data[g1], data[g2]]),
                "name": f"good_{g1 + 1}_vs_good_{g2 + 1}"
            }
        )

    p = _mw(to_compare, print_latex, **kwargs)

    return [c + (v, ) for c, v in zip(cp, p)]
