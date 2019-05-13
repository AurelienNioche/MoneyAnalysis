import numpy as np
from tqdm import tqdm


def get_windowed_observation(dir_ex, ind_ex, n, n_split, n_good):

    tmax = len(n)
    step = tmax // n_split
    bounds = np.arange(tmax+1, step=step)
    # averaged_dir_ex = np.zeros(n_good, dtype=float)
    averaged_ind_ex = np.zeros(n_good, dtype=float)

    for good in range(n_good):

        #for i_bound in range(len(bounds) - 1):

        # set inferior and superior bound
        inf = bounds[-2]
        sup = bounds[-1]

        # get windowed data
        windowed_ind = ind_ex[inf:sup, good]
        windowed_dir = dir_ex[inf:sup]
        n_possibility = n[inf:sup]

        # If it is not the first window normalize, otherwise no (minus 0)
        # normalized by the number of attempts
        last_data_ind = ind_ex[inf - 1, good]
        last_data_dir = dir_ex[inf - 1]
        last_n = n[inf - 1]

        norm_windowed_ind = windowed_ind - last_data_ind
        # norm_windowed_dir = windowed_dir - last_data_dir

        norm_n_possibility = n_possibility - last_n

        ind_to_compute = []
        # dir_to_compute = []
        # idx = 0
        # for ex_type, norm in zip(
        #         [ind_to_compute, dir_to_compute], [norm_windowed_ind, norm_windowed_dir]):
        for x, y in zip(norm_windowed_ind,  norm_n_possibility):

            if y > 0:
                ind_to_compute.append(x/y)
            else:
                ind_to_compute.append(-1)
                # idx += 1

        # averaged_dir_ex = np.mean(dir_to_compute)
        assert len(ind_to_compute)
        averaged_ind_ex[good] = np.mean(ind_to_compute)

    return averaged_ind_ex  # averaged_dir_ex, averaged_ind_ex


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

            c = int(desired[t])

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


def get_observation(in_hand, desired, prod, cons, n_split=3):

    """
    :param: prod: nested list n_eco:n_agent
    :param: cons: nested list n_eco:n_agent
    :param in_hand: nested list n_eco:n_agent:t_max
    :param desired: nested list n_eco:n_agent:t_max
    :return: nested list economy index:good index
    """

    obs = []

    n_eco = len(in_hand)

    for i_eco in tqdm(range(n_eco)):
        n_good = int(max(in_hand[i_eco][:, 0])) + 1  # All individuals, time step=0
        n_agent = len(in_hand[i_eco])

        obs_eco = np.zeros((n_agent, n_good))
        for i_agent in range(n_agent):

            # dir_ex, ind_ex, n = exchange(n_good=n_good,
            #                              in_hand=in_hand[i_eco][i_agent],
            #                              desired=desired[i_eco][i_agent],
            #                              prod=prod[i_eco][i_agent],
            #                              cons=cons[i_eco][i_agent])
            # obs_eco[i_agent] = get_windowed_observation(dir_ex=dir_ex, ind_ex=ind_ex, n=n,
            #                                             n_good=n_good, n_split=n_split)  # np.random.random(n_good)

            obs_eco[i_agent, :] = [0.5 for _ in range(n_good)]

        to_add = []
        for i_good in range(n_good):
            non_prod_i = prod[i_eco] != i_good
            non_cons_i = cons[i_eco] != i_good
            can_use_as_m = non_prod_i * non_cons_i
            assert sum(can_use_as_m) > 0
            np.seterr(all='raise')
            to_add.append(
                np.mean(obs_eco[can_use_as_m, i_good])
            )
        obs.append(to_add)

    print(len(obs))
    return obs
