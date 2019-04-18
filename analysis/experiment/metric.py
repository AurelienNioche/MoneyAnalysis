import numpy as np


def monetary_behavior(n_good, in_hand, desired, prod, cons):

    t_max = len(in_hand)

    ind_ex = np.zeros((t_max, n_good), dtype=int)
    dir_ex = np.zeros(t_max, dtype=int)
    n = np.zeros(t_max, dtype=int)

    _n = 0
    _dir_ex = 0
    _ind_ex = np.zeros(n_good, dtype=int)

    for t in range(t_max):

        ih = in_hand[t]

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

        ind_ex[t, :] = _ind_ex.copy()
        dir_ex[t] = _dir_ex
        n[t] = _n

    _dir_ex /= _n
    _ind_ex /= _n

    return dir_ex, ind_ex, n
