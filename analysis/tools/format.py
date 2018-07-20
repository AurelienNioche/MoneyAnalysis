import numpy as np
import scipy.stats
import simulation.economy


# ------------ XP ------------------- #


def exp_monetary_bhv_over_user(monetary_bhv):

    n_user = len(monetary_bhv[0, :, 0])
    n_good = len(monetary_bhv[:, 0, 0])

    new = np.zeros((n_good, n_user))

    for i in range(n_user):

        for good in range(n_good):
            new[good, i] = np.mean(monetary_bhv[good, i, :])

    return new


def exp_monetary_bhv_over_t(monetary_bhv, repartition):

    n_good = len(repartition)
    t_max = len(monetary_bhv[0, 0, :])

    agent_type = np.repeat(np.arange(n_good), repartition)

    y = np.zeros((n_good, n_good, t_max))

    for i in range(n_good):
        for j in range(n_good):
            for t in range(t_max):
                y[i, j, t] = np.mean(monetary_bhv[i, agent_type == j, t])

    return y


# def exp_medium_over_t(medium, repartition, model='prod: i-1'):
#
#     n_good = len(repartition)
#     t_max = len(medium[0, :])
#
#     roles = simulation.economy.Economy.get_roles(n_goods=len(repartition), model=model)
#
#     y = np.zeros((n_good, t_max))
#
#     for i in range(n_good):
#
#         n = 0
#
#         for idx, (j, k) in enumerate(roles):
#             if j != i and k != i:
#                 n += repartition[idx]
#
#         y[i] = medium[i] / n
#
#     return y


def exp_medium_bar_plot(medium):

    n_good = len(medium)

    y = np.zeros(n_good)
    err = np.zeros(n_good)

    for good in range(n_good):
        y[good] = np.mean(medium[good])
        err[good] = scipy.stats.sem(medium[good])

    return y, err


def exp_monetary_bhv_bar_plot(monetary_bhv):

    n_user = len(monetary_bhv[0, :, 0])
    n_good = len(monetary_bhv[:, 0, 0])

    new = np.zeros((n_good, n_user))
    y = np.zeros(n_good)
    err = np.zeros(n_good)

    for i in range(n_user):

        for good in range(n_good):
            new[good, i] = np.mean(monetary_bhv[good, i, :])

    for good in range(n_good):

        y[good] = np.mean(new[good, :])
        err[good] = scipy.stats.sem(new[good, :])

    return y, err


# ----------- SIM --------------------------------- #


def sim_medium_bar_plot(medium):

    n_good = len(medium[:, 0])

    y = np.zeros(n_good)
    err = np.zeros(n_good)

    for good in range(n_good):
        y[good] = np.mean(medium[good, :])
        err[good] = scipy.stats.sem(medium[good, :])

    return y, err


def medium_over_user(medium):
    """
    returns an array with format compatible with
    for_medium_bar_plot_from_simulation function
    """

    # print(len(medium.flatten() == -1))

    n_user = len(medium[0, :, 0])
    n_good = len(medium[:, 0, 0])

    new = np.zeros((n_good, n_user))

    for i in range(n_user):

        for good in range(n_good):
            if -1 in medium[good, i, :]:
                v = np.nan
            else:
                a = medium[good, i, :]
                v = np.mean(a)

            new[good, i] = v

    without_nan = [
        [i for i in new[good, :] if not np.isnan(i)]
        for good in range(n_good)
    ]

    return without_nan


def medium_over_t(medium):
    """
    returns an array with format compatible with
    for_medium_bar_plot_from_simulation function
    """

    n_t = len(medium[0, 0, :])
    n_good = len(medium[:, 0, 0])

    new = np.zeros((n_good, n_t))

    for t in range(n_t):

        for good in range(n_good):
            cond = medium[good, :, t] != -1
            new[good, t] = np.mean(medium[good, cond, t])

    return new


def sim_medium_over_t_mean(list_medium):

    n_eco = len(list_medium)
    n_good = len(list_medium[0])

    y = np.zeros((n_good, n_eco))

    for g in range(n_good):

        for i in range(n_eco):

            y[g, i] = np.mean(list_medium[i][g])

    return y


def sim_monetary_bhv_bar_plot(monetary_bhv):

    n_good = len(monetary_bhv[:, 0])

    y = np.zeros(n_good)
    err = np.zeros(n_good)

    for good in range(n_good):

        y[good] = np.mean(monetary_bhv[good, :])
        err[good] = scipy.stats.sem(monetary_bhv[good, :])

    return y, err


def monetary_over_user(monetary_bhv):

    """
    returns an array with format compatible with
    for_monetary_behavior_bar_plot_from_simulation function
    """

    n_user = len(monetary_bhv[0, :, 0])
    n_good = len(monetary_bhv[:, 0, 0])

    new = np.zeros((n_good, n_user))

    for i in range(n_user):

        for good in range(n_good):
            new[good, i] = np.mean(monetary_bhv[good, i, :])

    return new


# def sim_monetary_mean_over_user(list_monetary_bhv):
#
#     n_eco = len(list_monetary_bhv)
#     n_good = len(list_monetary_bhv[0][:, ])
#
#     y = np.zeros((n_good, n_eco))
#
#     for g in range(n_good):
#
#         for i in range(n_eco):
#
#             y[g, i] = np.mean(list_monetary_bhv[i][g])
#
#     return y

def sim_monetary_mean_over_user(list_monetary_bhv):

    n_good = len(list_monetary_bhv[0][:, ])

    n_total_user = 0

    for l in list_monetary_bhv:
        n_total_user += len(l[0])

    # print(n_total_user)

    # y = np.zeros((n_good, n_total_user))

    one_good_all_agents = [[] for _ in range(n_good)]

    for eco in list_monetary_bhv:

        for good in range(n_good):
            one_good_all_agents[good] += list(eco[good])

    # print(len(one_good_all_agents[0]))

    return np.asarray(one_good_all_agents)


def sim_monetary_behavior_mean_over_t(economies):

    t_max = len(economies[0][0, 0, :])
    n_good = len(economies[0][0, :, 0])

    y = np.zeros((n_good, n_good, t_max))

    for i in range(n_good):

        for j in range(n_good):

            for t in range(t_max):

                y[i, j, t] = np.mean([e[i, j, t] for e in economies])

    return y


def sim_medium_mean_over_user(list_medium_over_user):

    n_eco = len(list_medium_over_user)
    n_good = len(list_medium_over_user[0])

    y = np.zeros((n_good, n_eco))

    for g in range(n_good):

        for i in range(n_eco):

            y[g, i] = np.mean(list_medium_over_user[i][g])

    return y


def phase_diagram(monetary_behavior, distribution, n_good):

    n = len(distribution)  # Number of economies in this batch

    money = _get_money_array(monetary_behavior, distribution, n_good)

    unq_repartition = np.unique(distribution, axis=0)
    labels = np.unique([i[-1] for i in unq_repartition])

    n_side = len(labels)

    phases = []

    for good in range(n_good):

        scores = np.array([
            np.mean([money[i][good] for i in range(n) if np.all(distribution[i] == r)])
            for r in unq_repartition
        ])

        phases.append(scores.reshape(n_side, n_side).T)

    return phases, labels


def _get_money_array(monetary_behavior, repartition, n_good):

    n = len(repartition)  # Number of economies in this batch

    return np.array([
        [np.mean(monetary_behavior[i][good, :, :]) for good in range(n_good)] for i in range(n)
    ])
