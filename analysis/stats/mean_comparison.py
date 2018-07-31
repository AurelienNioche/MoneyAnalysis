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


def _mw(to_compare):

    ps = []
    us = []

    for dic in to_compare:
        u, p = scipy.stats.mannwhitneyu(dic["data"][0], dic["data"][1])
        ps.append(p)
        us.append(u)

    valid, p_corr, alpha_c_sidak, alpha_c_bonf = \
        statsmodels.stats.multitest.multipletests(pvals=ps, alpha=0.05, method="b")

    for p, u, p_c, v, dic in zip(ps, us, p_corr, valid, to_compare):
        print("[{}] "
              "Mann-Whitney rank test: $u={}$, $p={:.3f}$, p raw {:.3f}, significant: {}"
              .format(dic["name"], u, p_c, p, v))
        print()

    return p_corr


def run(data):

    cp = comparisons[len(data)]

    to_compare = []

    for g1, g2 in cp:

        to_compare.append(
            {
                "data": np.array([data[g1], data[g2]]),
                "name": f"good_{g1 + 1}_vs_good_{g2 + 1}"
            }
        )

    p = _mw(to_compare)

    return [c + (v, ) for c, v in zip(cp, p)]
