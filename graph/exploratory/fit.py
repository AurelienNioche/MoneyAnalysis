import matplotlib.pyplot as plt

import os


FIG_FOLDER = "fig"
os.makedirs(FIG_FOLDER, exist_ok=True)


def plot_hist(alpha, beta, gamma, mean_p, lls, bic, ):

    for v, param_name in zip(
            (alpha, beta, gamma, mean_p, lls, bic, ),
            ("alpha", "beta", "gamma", "mean_p", "lls", "bic", )
    ):

        plt.hist(v)
        plt.title(param_name)
        f_name = f"fig/{param_name}_distribution.pdf"
        plt.savefig()
        print(f'{f_name} has been produced')

