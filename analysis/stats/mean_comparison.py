import numpy as np
import scipy.stats
import statsmodels.stats.multitest


def get_comparisons(data):

    if len(data) == 3:

        comparisons = [
            (0, 1),
            (0, 2),
        ]

    else:

        comparisons = [
            (0, 1),
            (0, 2),
            (0, 3)
        ]

    return comparisons


# i = 0


def monetary_behavior(m_bhv):

    comparisons = get_comparisons(m_bhv)

    to_compare = []

    for g1, g2 in comparisons:

        # print(len(m_bhv[g1]))
        # print(len(m_bhv[g2]))
        to_compare.append(
            {
                "data": np.array([m_bhv[g1, :], m_bhv[g2, :]]),
                "name": f"good_{g1 + 1}_vs_good_{g2 +1}"
            }
        )

        # global i
        # print(i, np.array([m_bhv[g1, :], m_bhv[g2, :]]))
        # i += 1

    valid = mw(to_compare)

    return [c + (v, ) for c, v in zip(comparisons, valid)]


def medium(m):

    comparisons = get_comparisons(m)

    to_compare = []

    for g1, g2 in comparisons:

        to_compare.append(
            {
                "data": np.array([m[g1], m[g2]]),
                "name": f"good_{g1 + 1}_vs_good_{g2 + 1}"
            }
        )

    p = mw(to_compare)

    return [c + (v, ) for c, v in zip(comparisons, p)]


def mw(to_compare):

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








