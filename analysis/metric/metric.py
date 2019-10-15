import numpy as np
from tqdm import tqdm

np.seterr(all='raise')


def statistic(ex, n, t, window):

    sup = t
    inf = max(-1, sup - window)

    # Number of attempts
    begin_n = n[inf] if inf != -1 else 0
    last_n = n[sup]

    diff_n = last_n - begin_n

    begin_ex = ex[inf] if inf != -1 else 0
    last_ex = ex[sup]

    diff_ex = last_ex - begin_ex

    if diff_n > 0:
        st = diff_ex / diff_n
    else:
        st = np.nan

    return st


def exchange(n_good, in_hand, desired, prod, cons, m=None):

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

    n = np.zeros(t_max, dtype=int)
    dir_ex = np.zeros(t_max)

    _n = 0
    _dir_ex = 0

    if m is None:
        ind_ex = np.zeros((t_max, n_good), dtype=int)
        _ind_ex = np.zeros(n_good, dtype=int)

    else:
        ind_ex = np.zeros(t_max, dtype=int)
        _ind_ex = 0

    for t in range(t_max):

        ih = in_hand[t]
        # --- ....old way ---
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

            if c == cons:
                _dir_ex += 1
            else:
                if m is None:
                    _ind_ex[c] += 1
                else:
                    _ind_ex += int(c == m)

        if m is None:
            ind_ex[t, :] = _ind_ex
        else:
            ind_ex[t] = _ind_ex
        dir_ex[t] = _dir_ex
        n[t] = _n

    return dir_ex, ind_ex, n


# def _windowed_computation(ex, inf, sup, norm_n_possibility, split_idx):
#
#     # get windowed data
#     raw_windowed = ex[inf:sup]
#     # If it is not the first window normalize, otherwise no (minus 0)
#     # normalized by the number of attempts
#
#     last_data = ex[inf - 1] if split_idx != 0 else 0
#
#     norm_windowed = raw_windowed - last_data
#
#     r = []
#     for x, y in zip(norm_windowed, norm_n_possibility):
#
#         if y > 0:
#             r.append(x / y)
#
#     try:
#         assert len(r)
#         r_mean = np.mean(r)
#     except AssertionError:
#         r_mean = np.nan
#
#     return r_mean
#
#
# def get_windowed_observation(dir_ex, ind_ex, n, n_split, n_good, slice_idx=-1):
#
#     m_defined = len(ind_ex.shape) == 1
#
#     t_max = len(n)
#     step = t_max // n_split
#     bounds = np.arange(t_max+1, step=step)
#     m_dir_ex = np.zeros(n_split, dtype=float)
#
#     if m_defined:
#         m_ind_ex = np.zeros(n_split, dtype=float)
#     else:
#         m_ind_ex = np.zeros((n_split, n_good), dtype=float)
#
#     if slice_idx == 'all':
#         slice_to_compute = range(n_split)
#     else:
#         if slice_idx != -1:
#             slice_to_compute = slice_idx,
#         else:
#             slice_to_compute = n_split - 1,
#
#     for i in slice_to_compute:
#
#         # set inferior and superior bound
#         inf = bounds[i]
#         sup = bounds[i+1]
#
#         # Number of attempts
#         n_possibility = n[inf:sup]
#
#         last_n = n[inf - 1] if i != 0 else 0
#         norm_n_possibility = n_possibility - last_n
#
#         m_dir_ex[i] = _windowed_computation(
#             ex=dir_ex, inf=inf, sup=sup,
#             norm_n_possibility=norm_n_possibility,
#             split_idx=i)
#
#         if m_defined:
#             m_ind_ex[i] = _windowed_computation(
#                 ex=ind_ex[:], inf=inf, sup=sup,
#                 norm_n_possibility=norm_n_possibility,
#                 split_idx=i)
#
#         else:
#             for good in range(n_good):
#
#                 m_ind_ex[i, good] = _windowed_computation(
#                     ex=ind_ex[:, good], inf=inf, sup=sup,
#                     norm_n_possibility=norm_n_possibility,
#                     split_idx=i)
#
#     if slice_idx != 'all':
#         if m_defined:
#             return m_dir_ex[slice_idx], m_ind_ex[slice_idx]
#         else:
#             return m_dir_ex[slice_idx], m_ind_ex[slice_idx, :]
#
#     else:
#         return m_dir_ex, m_ind_ex


def get_economy_measure(in_hand, desired, prod, cons, m=0, n_split=2):

    """
    :param m: None or integer
    :param n_split: integer
    :param cons: nested list n_eco:n_agent
    :param prod: nested list n_eco:n_agent
    :param in_hand: nested list n_eco:n_agent:t_max
    :param desired: nested list n_eco:n_agent:t_max
    :return: nested list economy index:good index
    """

    obs = []

    n_eco = len(in_hand)

    for i_eco in tqdm(range(n_eco)):

        # All individuals, time step=0
        n_good = int(max(in_hand[i_eco][:, 0])) + 1
        n_agent = len(in_hand[i_eco])

        if m is None:
            obs_eco = np.zeros((n_agent, n_good))

        else:
            obs_eco = np.zeros(n_agent)

        for i_agent in range(n_agent):

            _, ex, n = exchange(
                n_good=n_good,
                in_hand=in_hand[i_eco][i_agent],
                desired=desired[i_eco][i_agent],
                prod=prod[i_eco][i_agent],
                cons=cons[i_eco][i_agent],
                m=m)

            # _dir, _ind = get_windowed_observation(
            #     dir_ex=dir_ex, ind_ex=ind_ex, n=n,
            #     n_good=n_good, n_split=n_split, slice_idx=-1)
            t_max = len(ex)
            window = int(t_max/n_split)
            _ind = \
                statistic(
                    ex=ex, n=n, t=t_max - 1, window=window
                )

            obs_eco[i_agent] = _ind

        if m is None:
            to_add = []
            for i_good in range(n_good):

                non_prod_i = prod[i_eco] != i_good
                non_cons_i = cons[i_eco] != i_good
                can_use_as_m = non_prod_i * non_cons_i

                to_add.append(
                    np.mean(obs_eco[can_use_as_m, i_good])
                )
            obs.append(to_add)
        else:
            non_prod_i = prod[i_eco] != m
            non_cons_i = cons[i_eco] != m
            can_use_as_m = non_prod_i * non_cons_i

            mean_obs = np.nanmean(obs_eco[can_use_as_m])

            assert not np.isnan(mean_obs)
            obs.append(mean_obs)

    return np.asarray(obs)

#
# def get_individual_measure(data_xp_session, i, n_split, slice_idx, obs_type):
#
#     dir_ex, ind_ex, n = exchange(
#         n_good=data_xp_session.n_good,
#         in_hand=data_xp_session.in_hand[i],
#         desired=data_xp_session.desired[i],
#         cons=data_xp_session.cons[i],
#         prod=data_xp_session.prod[i])
#
#     _dir, _ind = get_windowed_observation(
#         dir_ex=dir_ex, ind_ex=ind_ex, n=n, n_split=n_split,
#         n_good=data_xp_session.n_good, slice_idx=slice_idx)
#
#     if slice_idx != 'all':
#
#         if obs_type in ('ind_0', 'ind_1', 'ind_2', 'ind_3'):
#             good = int(obs_type[-1])
#             d = _ind[good]
#
#         else:
#             d = _dir
#
#     else:
#         if obs_type in ('ind_0', 'ind_1', 'ind_2', 'ind_3'):
#             good = int(obs_type[-1])
#             d = _ind[:, good]
#
#         else:
#             d = _dir[:]
#
#     return d
#
#
# def dynamic_data(data_xp_session, n_split=3, obs_type='ind_0', slice_idx=-1):
#
#     """
#     :param slice_idx: integer or 'all'
#     :param obs_type: 'ind_0', 'ind_1', 'ind_2', 'ind_3', 'dir'
#     :param data_xp_session: DataXPSession object
#     :param n_split: integer
#     :return: dictionary:
#     key: agent_type
#     value: average for each subject able to use the
#     """
#
#     assert obs_type in ('ind_0', 'ind_1', 'ind_2', 'ind_3', 'dir'), \
#         'Observation type not recognized'
#
#     if obs_type not in ('ind_0', 'dir'):
#         raise NotImplementedError(
#             'Other obs than ind_0 or dir are not available yet.')
#
#     n_good = data_xp_session.n_good
#
#     n_agent = len(data_xp_session.prod)
#
#     n_possible_type = 2 if obs_type == 'ind_0' else 0
#     agent_types = tuple(range(n_possible_type, n_good))
#
#     formatted_data = {k: [] for k in agent_types}
#
#     for i in range(n_agent):
#
#         agent_type = data_xp_session.cons[i]
#
#         if agent_type in agent_types:
#
#             d = get_individual_measure(data_xp_session, i,
#                                        n_split, slice_idx,
#                                        obs_type)
#             formatted_data[agent_type].append(d)
#
#     return formatted_data
