import numpy as np
import simulation.economy

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
