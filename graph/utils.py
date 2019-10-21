import os

import matplotlib.pyplot as plt

DEFAULT_FIG_FOLDER = "fig"


def save_fig(fig_name, fig_folder=None):

    if fig_name is not None:

        if fig_folder is None:
            fig_folder = DEFAULT_FIG_FOLDER

        os.makedirs(fig_folder, exist_ok=True)
        fig_path = os.path.join(fig_folder, fig_name)
        plt.savefig(fig_path)
        plt.close()
        print(f"Figure '{fig_path}' created.\n")


def get_ax(axes, row, col):

    if len(axes.shape) == 1:
        if col > row:
            return axes[col]
        elif row > col:
            return axes[row]
        else:
            assert row == col == 0
            return axes[0]
    else:
        try:
            return axes[row, col]
        except IndexError as e:
            print(row, col, axes.shape)
            raise e
