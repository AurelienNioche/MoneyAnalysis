import numpy as np
import scipy.stats
import simulation.economy


def for_fit(data):

    # Input data structure
    #  data = {
    #  '<economy_label>': {'<parameter>': np.array with size n_user},
    #                       ...
    #  }

    # output data structure
    #  data = {
    #  '<economy_label>': np.array([<param1>, <param2>, <param3>]) * n_user
    # }
    #

    formatted_data = {}

    for k, v in data.items():

        n = len(v['alpha'])
        room_data = np.zeros((n, len(v)))

        for i in range(n):
            # for param_label, param_value in v.items():

            room_data[i] = v["alpha"][i], v["beta"][i], v["gamma"][i]

        formatted_data[k] = room_data

    return formatted_data


def for_monetary_behavior_over_t(monetary_bhv, repartition):

    n_good = len(repartition)
    t_max = len(monetary_bhv[0, 0, :])

    agent_type = np.repeat(np.arange(n_good), repartition)

    y = np.zeros((n_good, n_good, t_max))

    for i in range(n_good):
        for j in range(n_good):
            for t in range(t_max):
                y[i, j, t] = np.mean(monetary_bhv[i, agent_type == j, t])

    return y


def for_medium_bar_plot_from_experiment(medium):

    n_good = len(medium[:, 0])

    y = np.zeros(n_good)
    err = np.zeros(n_good)

    for good in range(n_good):
        y[good] = np.mean(medium[good, medium[good, :] != -1])
        err[good] = scipy.stats.sem(medium[good, medium[good, :] != -1])

    return y, err


def for_medium_bar_plot_from_simulation(medium):

    n_good = len(medium[:, 0])

    y = np.zeros(n_good)
    err = np.zeros(n_good)

    for good in range(n_good):
        y[good] = np.mean(medium[good, :])
        err[good] = scipy.stats.sem(medium[good, :])

    return y, err


def for_medium_bar_plot_from_simulation_pool(medium):
    """
    returns an array with format compatible with
    for_medium_bar_plot_from_simulation function
    """

    n_user = len(medium[0, :, 0])
    n_good = len(medium[:, 0, 0])

    new = np.zeros((n_good, n_user))

    for i in range(n_user):

        for good in range(n_good):
            new[good, i] = np.mean(medium[good, i, medium[good, i, :] != -1])

    return new


def for_monetary_behavior_bar_plot_from_experiment(monetary_bhv):

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


def for_monetary_bar_plot_from_simulation(monetary_bhv):

    n_good = len(monetary_bhv[:, 0])

    y = np.zeros(n_good)
    err = np.zeros(n_good)

    for good in range(n_good):

        y[good] = np.mean(monetary_bhv[good, :])
        err[good] = scipy.stats.sem(monetary_bhv[good, :])

    return y, err


def for_monetary_behavior_bar_plot_from_simulation_pool(monetary_bhv):

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


def for_monetary_behavior_over_time_mean(economies):

    t_max = len(economies[0][0, 0, :])
    n_good = len(economies[0][0, :, 0])

    y = np.zeros((n_good, n_good, t_max))

    for i in range(n_good):

        for j in range(n_good):

            for t in range(t_max):

                y[i, j, t] = np.mean([e[i, j, t] for e in economies])

    return y


def for_variable_over_user_mean(economies):

    n_user = len(economies[0][0, :])
    n_good = len(economies[0][:, 0])

    y = np.zeros((n_good, n_user))

    for i in range(n_good):

        for t in range(n_user):

            y[i, t] = np.mean([eco[i, t] for eco in economies])

    return y


def for_medium_over_time_mean(economies):

    n_user = len(economies[0][0, :])
    n_good = len(economies[0][:, 0])

    y = np.zeros((n_good, n_user))

    for i in range(n_good):

        for t in range(n_user):

            y[i, t] = np.mean([eco[i, t] for eco in economies])

    return y


def for_medium_over_t(medium, repartition, model='prod: i-1'):

    n_good = len(repartition)
    t_max = len(medium[0, :])

    roles = simulation.economy.Economy.get_roles(n_goods=len(repartition), model=model)

    y = np.zeros((n_good, t_max))

    for i in range(n_good):

        n = 0

        for idx, (j, k) in enumerate(roles):
            if j != i and k != i:
                n += repartition[idx]

        y[i] = medium[i] / n

    return y


def for_phase_diagram(monetary_behavior, repartition, n_good):

    n = len(repartition)  # Number of economies in this batch

    money = _get_money_array(monetary_behavior, repartition, n_good)

    unq_repartition = np.unique(repartition)
    labels = np.unique([i[-1] for i in unq_repartition])

    n_side = len(labels)

    phases = []

    for good in range(n_good):

        scores = np.array([
            np.mean([money[i][good] for i in range(n) if np.all(repartition[i] == r)])
            for r in unq_repartition
        ])

        phases.append(scores.reshape(n_side, n_side).T)

    return phases, labels


def _get_money_array(monetary_behavior, repartition, n_good):

    n = len(repartition)  # Number of economies in this batch

    return np.array([
        [np.mean(monetary_behavior[i][good, :, :]) for good in range(n_good)] for i in range(n)
    ])






