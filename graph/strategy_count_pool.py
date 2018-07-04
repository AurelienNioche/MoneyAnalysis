import matplotlib.pyplot as plt
import matplotlib.gridspec as grd
import itertools as it
import os

from graph.tools import bar

script_name = '_strategy_count_pool'


def plot(data, f_name=None):

    data_keys = \
        "3_good_non_uniform" + script_name, \
        "3_good_uniform" + script_name, \
        "4_good_non_uniform" + script_name, \
        "4_good_uniform" + script_name

    fig = plt.figure(figsize=(15, 15))
    gs = grd.GridSpec(nrows=2, ncols=2, width_ratios=[1, 1], height_ratios=[3, 4])

    coord = it.product(range(2), repeat=2)

    for i, k in enumerate(data_keys):
        c = next(coord)

        bar.bar(
            means=data[k]['mean'], errors=data[k]['std'], subplot_spec=gs[c[0], c[1]], fig=fig,
            labels=[str(i) for i in range(len(data[k]['mean']))], title=k.replace(script_name, ''),
            color="C7"
        )

    plt.tight_layout()

    if f_name is not None:
        os.makedirs(os.path.dirname(f_name), exist_ok=True)
        plt.savefig(f_name)

    plt.show()
