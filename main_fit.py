import numpy as np

from fit import fit
from xp import xp

from metric import metric

import graph.sim_and_xp
from stats import stats

import fit.data
import simulation.run_based_on_fit


def main():

    alpha, beta, gamma, mean_p, lls, bic, eco = fit.data.get()

    data = {}
    data["HUMAN"], room_n_good, room_uniform = xp.get_data()
    data["SIM"] = simulation.run_based_on_fit.get_data(xp_data_list=data["HUMAN"], alpha=alpha, beta=beta, gamma=gamma, eco=eco)

    category = data.keys()
    n_good_cond = np.unique(room_n_good)
    cond_labels = "NON-UNIF", "UNIF"

    fig_data = {n_good: {
        cat: {

        } for cat in category
    } for n_good in n_good_cond}

    for n_good in room_n_good:

        for uniform in True, False:

            # Find the good indexes
            cond_n_good = room_n_good == n_good
            cond_uniform = room_uniform == uniform

            xp_cond = cond_n_good * cond_uniform
            assert (np.sum(xp_cond) == 1)
            d_idx = np.where(xp_cond == 1)[0][0]

            for cat in category:

                # Get formatted data
                d = data[cat][d_idx]
                d_formatted = metric.dynamic_data(data_xp_session=d)

                for agent_type in sorted(d_formatted.keys()):
                    if agent_type not in fig_data[n_good][cat].keys():
                        fig_data[n_good][cat][agent_type] = {}

                    fig_data[n_good][cat][agent_type][cond_labels[int(uniform)]] = d_formatted[agent_type]

    graph.sim_and_xp.plot(fig_data, name_extension='FIT')
    stats.sim_and_xp(fig_data)


if __name__ == "__main__":

    main()
