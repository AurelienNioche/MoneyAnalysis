def agent_labeling(n_good):
    return {i: f'$({(i - 1) % n_good + 1}, {i + 1})$' for i in range(n_good)}