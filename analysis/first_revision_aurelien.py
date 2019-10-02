import os

from backup import backup

import simulation.run_first_revision

from . main import format_for_phase_diagram


DATA_FOLDER = "data"


def phase_diagram(agent_model, m=0):

    data_file = os.path.join(
        DATA_FOLDER,
        f'formatted_phase_diagram_{agent_model.__name__}.p')

    if os.path.exists(data_file):

        data, labels = backup.load(data_file)
        return data, labels
    data = {}

    for n_good in (4, 3):

        d = simulation.run_first_revision.get_data(
            agent_model=agent_model,
            n_good=n_good)

        formatted_d, labels = format_for_phase_diagram(d, m)

        data[n_good] = formatted_d

    backup.save((data, labels), data_file)

    return data, labels
