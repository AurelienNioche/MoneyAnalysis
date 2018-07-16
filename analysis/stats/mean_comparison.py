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


def monetary_bhv_format(monetary_bhv):

    n_user = len(monetary_bhv[0, :, 0])
    n_good = len(monetary_bhv[:, 0, 0])

    new = np.zeros((n_good, n_user))

    for i in range(n_user):

        for good in range(n_good):
            new[good, i] = np.mean(monetary_bhv[good, i, :])

    return new


def pool_monetary_bhv(monetary_bhv):

    economies = [monetary_bhv_format(d) for d in monetary_bhv]

    n_user = len(economies[0][0, :])
    n_good = len(economies[0][:, 0])

    new = np.zeros((n_good, n_user))

    for i in range(n_user):

        for good in range(n_good):

            new[good, i] = np.mean([e[good, i] for e in economies])

    return new


def medium_exclude_non_users(medium):

    n_user = len(medium[0, :])
    n_good = len(medium[:, 0])

    without_non_users = []

    for good in range(n_good):

        new = medium[good, medium[good, :] != -1]

        without_non_users.append(new)

    return without_non_users


def monetary_behavior(data):

    # If there is only one economy
    # we have one array
    # else if we have many economies
    # we have a list of arrays
    if isinstance(data, list):

        m_bhv = pool_monetary_bhv(data)

    else:

        m_bhv = monetary_bhv_format(data)

    comparisons = get_comparisons(m_bhv)

    to_compare = []

    for g1, g2 in comparisons:

        to_compare.append(
            {
                "data": np.array([m_bhv[g1, :], m_bhv[g2, :]]),
                "name": f"good_{g1}_vs_good_{g2}"
            }
        )

    mw(to_compare)

    if len(m_bhv) == 3:

        print('*' * 5, 'POST HOC', '*' * 5)

        comparisons = [(1, 2)]

        to_compare = []

        for g1, g2 in comparisons:

            to_compare.append(
                {
                    "data": np.array([m_bhv[g1, :], m_bhv[g2, :]]),
                    "name": f"good_{g1}_vs_good_{g2}"
                }
            )

        mw(to_compare)


def medium(data):

    m = medium_exclude_non_users(data)

    comparisons = get_comparisons(m)

    to_compare = []

    for g1, g2 in comparisons:

        to_compare.append(
            {
                "data": np.array([m[g1], m[g2]]),
                "name": f"good_{g1}_vs_good_{g2}"
            }
        )

    mw(to_compare)

    if len(m) == 3:

        print('*' * 5, 'POST HOC', '*' * 5)

        comparisons = [(1, 2)]

        to_compare = []

        for g1, g2 in comparisons:

            to_compare.append(
                {"data": np.array([m[g1], m[g2]]), "name": f"good_{g1}_vs_good_{g2}"}
            )

        mw(to_compare)


def mw(to_compare):

    ps = []
    us = []

    for dic in to_compare:
        u, p = scipy.stats.mannwhitneyu(dic["data"][0], dic["data"][1])
        ps.append(p)
        us.append(u)

    valid, p_corr, alpha_c_sidak, alpha_c_bonf = \
        statsmodels.stats.multitest.multipletests(pvals=ps, alpha=0.01, method="b")

    for p, u, p_c, v, dic in zip(ps, us, p_corr, valid, to_compare):
        print("[Test diff {}] "
              "Mann-Whitney rank test: u {}, p {:.3f}, p corr {:.3f}, significant: {}"
              .format(dic["name"], u, p, p_c, v))
        print()










