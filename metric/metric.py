import numpy as np
from tqdm import tqdm


def get_windowed_observation(dir_ex, ind_ex, n, n_split, n_good, slice_idx=-1):

    tmax = len(n)
    step = tmax // n_split
    bounds = np.arange(tmax+1, step=step)
    m_ind_ex = np.zeros((n_split, n_good), dtype=float)
    m_dir_ex = np.zeros(n_split, dtype=float)

    for i in range(n_split):
        # set inferior and superior bound
        inf = bounds[i]
        sup = bounds[i+1]

        # Number of attempts
        n_possibility = n[inf:sup]

        last_n = n[inf - 1] if i != 0 else 0
        last_data_dir = dir_ex[inf - 1] if i != 0 else 0

        # compute average direct exchanges
        windowed_dir = dir_ex[inf:sup]

        norm_n_possibility = n_possibility - last_n
        norm_windowed_dir = windowed_dir - last_data_dir

        dir_to_compute = []
        for x, y in zip(norm_windowed_dir,  norm_n_possibility):

            if y > 0:
                dir_to_compute.append(x/y)
            # else:
            #     dir_to_compute.append(-1)

        m_dir_ex[i] = np.mean(dir_to_compute)

        # Average indirect exchanges for each good
        for good in range(n_good):

            # get windowed data
            windowed_ind = ind_ex[inf:sup, good]
            # If it is not the first window normalize, otherwise no (minus 0)
            # normalized by the number of attempts

            last_data_ind = ind_ex[inf - 1, good] if i != 0 else 0

            norm_windowed_ind = windowed_ind - last_data_ind

            ind_to_compute = []
            for x, y in zip(norm_windowed_ind,  norm_n_possibility):

                if y > 0:
                    ind_to_compute.append(x/y)
                # else:
                #     ind_to_compute.append(-1)
                    # idx += 1

            m_ind_ex[i, good] = np.mean(ind_to_compute)

    return (m_dir_ex[slice_idx], m_ind_ex[slice_idx, :]) if slice_idx != 'all' else (m_dir_ex, m_ind_ex)


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
        # --- ...old way ---
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
                _ind_ex[c] += 1

        ind_ex[t, :] = _ind_ex
        dir_ex[t] = _dir_ex
        n[t] = _n

    return dir_ex, ind_ex, n


def get_economy_measure(in_hand, desired, prod, cons, n_split=3):

    """
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

        n_good = int(max(in_hand[i_eco][:, 0])) + 1  # All individuals, time step=0
        n_agent = len(in_hand[i_eco])

        obs_eco = np.zeros((n_agent, n_good))
        for i_agent in range(n_agent):

            dir_ex, ind_ex, n = exchange(n_good=n_good,
                                         in_hand=in_hand[i_eco][i_agent],
                                         desired=desired[i_eco][i_agent],
                                         prod=prod[i_eco][i_agent],
                                         cons=cons[i_eco][i_agent])
            _dir, _ind = get_windowed_observation(dir_ex=dir_ex, ind_ex=ind_ex, n=n,
                                                  n_good=n_good, n_split=n_split, slice_idx=-1)
            obs_eco[i_agent] = _ind

        to_add = []
        for i_good in range(n_good):

            non_prod_i = prod[i_eco] != i_good
            non_cons_i = cons[i_eco] != i_good
            can_use_as_m = non_prod_i * non_cons_i

            np.seterr(all='raise')
            to_add.append(
                np.mean(obs_eco[can_use_as_m, i_good])
            )

        obs.append(to_add)

    return obs


def phase_diagram(in_hand, desired, prod, cons, distribution, n_good):

    n = len(distribution)  # Number of economies in this batch

    observation = get_economy_measure(in_hand=in_hand, desired=desired, prod=prod, cons=cons)

    money = np.array([
        [observation[i][good] for good in range(n_good)] for i in range(n)
    ])

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


def get_individual_measure(data_xp_session, i, n_split, slice_idx, obs_type):

    dir_ex, ind_ex, n = exchange(
        n_good=data_xp_session.n_good,
        in_hand=data_xp_session.in_hand[i],
        desired=data_xp_session.desired[i],
        cons=data_xp_session.cons[i],
        prod=data_xp_session.prod[i])

    _dir, _ind = get_windowed_observation(
        dir_ex=dir_ex, ind_ex=ind_ex, n=n, n_split=n_split,
        n_good=data_xp_session.n_good, slice_idx=slice_idx)

    if slice_idx != 'all':

        if obs_type in ('ind_0', 'ind_1', 'ind_2', 'ind_3'):
            good = int(obs_type[-1])
            d = _ind[good]

        else:
            d = _dir

    else:
        if obs_type in ('ind_0', 'ind_1', 'ind_2', 'ind_3'):
            good = int(obs_type[-1])
            d = _ind[:, good]

        else:
            d = _dir[:]

    return d


def dynamic_data(data_xp_session, n_split=3, obs_type='ind_0', slice_idx=-1):

    """
    :param slice_idx: integer or 'all'
    :param obs_type: 'ind_0', 'ind_1', 'ind_2', 'ind_3', 'dir'
    :param data_xp_session: DataXPSession object
    :param n_split: integer
    :return: dictionary:
    key: agent_type
    value: average for each subject able to use the
    """

    assert obs_type in ('ind_0', 'ind_1', 'ind_2', 'ind_3', 'dir'), 'Observation type not recognized'

    if obs_type not in ('ind_0', 'dir'):
        raise NotImplementedError('Other obs than ind_0 or dir are not available yet.')

    n_good = data_xp_session.n_good

    n_agent = len(data_xp_session.prod)

    n_possible_type = 2 if obs_type == 'ind_0' else 0
    agent_types = tuple(range(n_possible_type, n_good))

    formatted_data = {k: [] for k in agent_types}

    for i in range(n_agent):

        agent_type = data_xp_session.cons[i]

        if agent_type in agent_types:

            d = get_individual_measure(data_xp_session, i, n_split, slice_idx, obs_type)
            formatted_data[agent_type].append(d)

    return formatted_data
