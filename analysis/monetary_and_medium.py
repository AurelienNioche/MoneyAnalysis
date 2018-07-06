import matplotlib.pyplot as plt
import matplotlib.gridspec as grd
import numpy as np
import itertools as it

from game.models import Room
from analysis import monetary_behavior
from analysis.tools import economy_repartitions, economy_labels
import simulation.data_format

import graph.graph



def run():

    coord = it.product(range(4), range(6))
    gs = grd.GridSpec(nrows=4, ncols=6)

    fig = plt.figure()
    rooms = Room.objects.all().order_by('id')

    data = {}

    for r in rooms:

        n_good = r.n_type
        print(r.id)
        label = economy_labels.get(r.id)

        data[label] = {}

        for m in range(n_good):

            monetary_data = monetary_behavior.run(
                m=m, room_id=r.id
            )[label + '_monetary_behavior']

            data[label].update({
                f'monetary_behavior_{m}': monetary_data
            })

            repartition = economy_repartitions.get(r.id)

            for i in range(n_good):
                print(len(data[label][f'monetary_behavior_{m}'][i]))

                data = simulation.data_format.for_monetary_behavior_over_t(data[label][f'monetary_behavior_{m}'][i], repartition)

                graph.graph._monetary_behavior_over_t(data=data, fig=fig, subplot_spec=gs[next(coord)], title=f'm={m}')

     # data = simulation.data_format.for_medium_over_t(res['medium'], repartition)
     # graph.graph._medium_over_t(data=data, fig=fig, subplot_spec=gs[next(coord)])

    plt.show()
