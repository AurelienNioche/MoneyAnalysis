import matplotlib.pyplot as plt

from fit import fit
from xp import xp

import fit.data
import simulation.run_based_on_fit


def main():

    data = {}
    data["HUMAN"], room_n_good, room_uniform = xp.get_data()
    alpha, beta, gamma, mean_p, lls, bic, eco = fit.data.get(data["HUMAN"], room_n_good, room_uniform)

    data["SIM"] = simulation.run_based_on_fit.get_data(xp_data_list=data["HUMAN"],
                                                       alpha=alpha, beta=beta, gamma=gamma, eco=eco)

    r_alpha, r_beta, r_gamma, r_mean_p, r_lls, r_bic, r_eco = fit.data.get(data["SIM"], room_n_good, room_uniform,
                                                                           extension="sim")
    parameter_names = "alpha", "beta", "gamma"

    fig, axes = plt.subplots(nrows=3)

    i = 0
    for values, r_values in ((alpha, r_alpha), (beta, r_beta), (gamma, r_gamma)):
        ax = axes[i]
        ax.scatter(values, r_values, alpha=0.5)
        title = parameter_names[i]
        ax.set_title(title)
        i += 1

    plt.tight_layout()
    plt.savefig("fig/parameter_recovery.pdf")


if __name__ == "__main__":

    main()
