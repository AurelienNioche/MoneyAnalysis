import numpy as np
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
    t_max = len(monetary_bhv[0, ])

    agent_type = np.repeat(np.arange(n_good), repartition)

    y = np.zeros((n_good, t_max))

    for i in range(n_good):
        for t in range(t_max):
            y[i, t] = np.mean(monetary_bhv[agent_type == i, t])

    return y


def for_medium_over_t(medium, repartition, model='prod: i-1'):

    n_good = len(repartition)
    t_max = len(medium[0, ])

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

    unq_repartition = np.unique(repartition, axis=0)
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






