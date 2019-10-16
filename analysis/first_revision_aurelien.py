import os

from backup import backup

import simulation.run_first_revision

from . main import format_for_phase_diagram


DATA_FOLDER = "data"


def phase_diagram(agent_model, n_good_condition, m=0):

    data_file = os.path.join(
        DATA_FOLDER,
        f'formatted_phase_diagram_'
        f'{agent_model.__name__}_'
        f'{"_".join(str(i) for i in n_good_condition)}.p')

    if os.path.exists(data_file):

        data, labels = backup.load(data_file)
        return data, labels
    data = {}

    labels = None
    for n_good in n_good_condition:

        d = simulation.run_first_revision.get_data(
            agent_model=agent_model,
            n_good=n_good)

        formatted_d, labels = format_for_phase_diagram(d, m)

        data[n_good] = formatted_d

    backup.save((data, labels), data_file)

    return data, labels
