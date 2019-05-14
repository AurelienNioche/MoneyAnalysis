import numpy as np
import scipy.stats


# ---------- XP & SIM ---------------- #


def medium_over_user(medium):
    """
    returns an array with format compatible with
    for_medium_bar_plot_from_simulation function
    """

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
    Computes the average used as medium value for
    each time step and for each good over one simulation.
    Also excludes agents that cant use the
    concerned medium.
    """

    n_t = len(medium[0, 0, :])
    n_good = len(medium[:])

    new = np.zeros((n_good, n_t))

    for t in range(n_t):

        for good in range(n_good):
            cond = medium[good, :, t] != -1
            a = medium[good, cond, t]
            new[good, t] = np.mean(a)

    return new


def monetary_bhv_over_user(monetary_bhv):

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


def monetary_bhv_over_t(monetary_bhv, repartition):

    n_good = len(repartition)
    t_max = len(monetary_bhv[0, 0, :])

    agent_type = np.repeat(np.arange(n_good), repartition)

    y = np.zeros((n_good, n_good, t_max))

    for i in range(n_good):
        for j in range(n_good):
            for t in range(t_max):
                y[i, j, t] = np.mean(monetary_bhv[i, agent_type == j, t])

    return y


# ------------ XP ------------------- #


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

    n_good = len(medium)

    y = np.zeros(n_good)
    err = np.zeros(n_good)

    for good in range(n_good):
        y[good] = np.mean(medium[good])
        err[good] = scipy.stats.sem(medium[good])

    return y, err


def sim_medium_mean_over_user(list_medium):

    n_good = len(list_medium[0])

    y = [[] for _ in range(n_good)]

    for i in range(n_good):

        for j in range(len(list_medium[0][i])):

            a = []

            for l in list_medium:

                a.append(l[i][j])

            y[i].append(np.mean(a))

    return np.asarray(y)


def sim_medium_mean_over_t(list_medium):
    """
    Takes a list of outputs from 'medium_over_t' function
    and computes the average of all the simulations (each simulation
    already being averaged over all time steps)
    :param list_medium:
    :return:
    """

    t_max = len(list_medium[0][0, :])
    n_good = len(list_medium[0][:, 0])

    y = np.zeros((n_good, t_max))

    for i in range(n_good):

        for t in range(t_max):

            y[i, t] = np.mean([l[i, t] for l in list_medium])

    return y


def sim_monetary_bhv_bar_plot(monetary_bhv):

    n_good = len(monetary_bhv[:, 0])

    y = np.zeros(n_good)
    err = np.zeros(n_good)

    for good in range(n_good):

        y[good] = np.mean(monetary_bhv[good, :])
        err[good] = scipy.stats.sem(monetary_bhv[good, :])

    return y, err


def sim_monetary_mean_over_user(list_monetary):

    n_user = len(list_monetary[0][0, :])
    n_good = len(list_monetary[0][:, 0])

    y = np.zeros((n_good, n_user))

    for i in range(n_good):

        for n in range(n_user):

            y[i, n] = np.mean([l[i, n] for l in list_monetary])

    return y


def sim_monetary_behavior_mean_over_t(economies):

    t_max = len(economies[0][0, 0, :])
    n_good = len(economies[0][0, :, 0])

    y = np.zeros((n_good, n_good, t_max))

    for i in range(n_good):

        for j in range(n_good):

            for t in range(t_max):

                y[i, j, t] = np.mean([e[i, j, t] for e in economies])

    return y


