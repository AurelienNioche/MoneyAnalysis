import numpy as np


def exchange(n_good, in_hand, desired, prod, cons):

    """
    Compute for a single subject for each timestep the cumulative number of
        * direct exchange with production good in hand
        * indirect exchange with good x
    :param n_good:
    :param in_hand:
    :param desired:
    :param prod:
    :param cons:
    :return:
    """

    t_max = len(in_hand)

    ind_ex = np.zeros((t_max, n_good))
    dir_ex = np.zeros(t_max)
    n = np.zeros(t_max, dtype=int)

    _n = 0
    _dir_ex = 0
    _ind_ex = np.zeros(n_good)

    for t in range(t_max):

        ih = in_hand[t]
        # --- old way ---
        # Check for direct
        # if (ih, c) == (prod, cons):
        #     dir_ex += 1
        # Check for indirect
        # else:
        #     for g in goods:
        #         if (ih, c) in [(prod, g), (g, cons)]:
        #             ind_ex[g] += 1
        if ih == prod:
            _n += 1

            c = desired[t]

            if int(c == cons):
                _dir_ex += 1
            else:
                _ind_ex[c] += 1

        ind_ex[t, :] = _ind_ex
        dir_ex[t] = _dir_ex
        n[t] = _n

    return dir_ex, ind_ex, n


def monetary(n_good, in_hand, desired, prod, cons):

    t_max = len(in_hand)

    monetary_behavior = np.zeros((t_max, n_good))
    n = np.zeros(t_max, dtype=int)

    _n = 0  #
    _m_bh = np.zeros(n_good)  # Monetary behavior

    for t in range(t_max):

        ih = in_hand[t]

        if ih == prod:
            _n += 1

            c = desired[t]

            for monetary_good in range(n_good):

                prod_or_cons_money = monetary_good in [prod, cons]

                if int(c == cons):
                    _m_bh[monetary_good] += int(prod_or_cons_money)

                else:
                    _m_bh[monetary_good] += int(c == monetary_good)

        monetary_behavior[t, :] = _m_bh
        n[t] = _n

    return monetary_behavior, n
