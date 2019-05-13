# MoneyAnalysis
# Copyright (C) 2018  Aurélien Nioche, Basile Garcia & Nicolas Rougier
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
# Django specific settings
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MoneyAnalysis.settings")

# Ensure settings are read
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()


import simulation.economy
import simulation.run

import analysis.tools
import analysis.tools.format
import analysis.tools.economy

import analysis.graph
import analysis.graph.overall
import analysis.graph.phase_diagram

import analysis.experiment.monetary_and_medium
import analysis.experiment.demographics

import analysis.stats.mean_comparison
import simulation.supplementary_exploration
import simulation.supplementary_exploitation
import simulation.supplementary_main


def exp_overall():

    """
    plots each experimental condition
    from experimental data

    """

    results = analysis.experiment.monetary_and_medium.run()

    for good in (3, 4):

        data = []
        titles = (f'{good}_good_non_uniform', f'{good}_good_uniform')
        stat_title = (f'{good}-NUPM', f'{good}-U')

        for k, xp_session in zip(titles, stat_title):

            # Get data
            medium = results[k]['medium']
            m_bhv = results[k]['monetary_bhv']
            distribution = results[k]['distribution']

            # Do stats
            print(f"Stats for experiment '{k}':")

            # Monetary bhv
            monetary_over_user = analysis.tools.format.monetary_bhv_over_user(m_bhv)
            money_sig = analysis.stats.mean_comparison.run(monetary_over_user, print_latex=True,
                                                           xp_session=xp_session, measure="MB")

            # Use as a medium
            medium_over_user = analysis.tools.format.medium_over_user(medium)
            med_sig = analysis.stats.mean_comparison.run(medium_over_user, print_latex=True,
                                                         xp_session=xp_session, measure="MoE")

            # Format data for Monetary bhv graph
            monetary_means, monetary_err = analysis.tools.format.exp_monetary_bhv_bar_plot(m_bhv)
            monetary_over_t = analysis.tools.format.monetary_bhv_over_t(m_bhv, distribution)

            # Format data for Used as medium graph
            medium_means, medium_err = analysis.tools.format.exp_medium_bar_plot(medium_over_user)
            medium_over_t = analysis.tools.format.medium_over_t(medium)

            d = {
                'monetary_bar': (monetary_means, monetary_err, money_sig),
                'monetary_over_t': monetary_over_t,
                'medium_bar': (medium_means, medium_err, med_sig),
                'medium_over_t': medium_over_t,
                'distribution': distribution
            }

            data.append(d)
            print()

        analysis.graph.overall.experiment(data, titles, f_name=f'fig/xp_{good}.pdf', exp=True)


def phase_diagram():

    """
    plot phase diagrams
    with 3 and 4 goods
    """

    f_name = 'fig/phase.pdf'

    # Number of column
    # (Plot for each good considered as money if max_col == None)
    max_col = 1

    three_good_data = simulation.run.get_data(phase=True, n_good=3)
    four_good_data = simulation.run.get_data(phase=True, n_good=4)

    data = []

    for d in (three_good_data, four_good_data):

        formatted_data, labels = analysis.tools.format.phase_diagram(
            in_hand=d.in_hand,
            desired=d.desired,
            prod=d.prod,
            cons=d.cons,
            distribution=d.distribution,
            n_good=len(d.distribution[0])
        )

        data.append(formatted_data)

    analysis.graph.phase_diagram.plot(
        data=data,
        labels=labels,
        f_name=f_name,
        max_col=max_col
    )


def sim_overall():

    """
    plots each experimental condition
    from simulation data

    """

    bkp = simulation.run.get_data(phase=False)

    room_id = {
        3: (414, 416),
        4: (417, 415)
    }

    for n_good in (3, 4):

        data = []

        titles = [analysis.tools.economy.labels.get(r_id) for r_id in room_id[n_good]]

        for r_id in room_id[n_good]:

            label = analysis.tools.economy.labels.get(r_id)
            xp_session = f"{n_good}-{'NUPM' if 'non_uniform' in label else 'U'}"
            print(f"Stats for simulation '{label}':")

            # ------------------------- Get data --------------------- #

            monetary_bhv = [
                d for i, d in enumerate(bkp.monetary_bhv)
                if bkp.room_id[i] == r_id
            ]

            medium = [
                d for i, d in enumerate(bkp.medium)
                if bkp.room_id[i] == r_id
            ]

            # distribution is common
            distribution = [
                d for i, d in enumerate(bkp.distribution)
                if bkp.room_id[i] == r_id
            ][0]

            # ------------------------- Monetary bhv ------------------------------- #

            # BAR PLOTS
            # reformat each economies to compress on agents
            monetary_over_user = [
                analysis.tools.format.monetary_bhv_over_user(m)
                for m in monetary_bhv
            ]

            # average all that
            monetary_over_user_mean = \
                analysis.tools.format.sim_monetary_mean_over_user(monetary_over_user)

            # Now we can do stats
            money_sig = analysis.stats.mean_comparison.run(monetary_over_user_mean,
                                                           print_latex=True,
                                                           xp_session=xp_session, measure="MB"
                                                           )

            # reformat for bar plots
            monetary_means, monetary_err = \
                analysis.tools.format.sim_monetary_bhv_bar_plot(monetary_over_user_mean)

            # CURVE PLOTS
            monetary_over_t = [
                analysis.tools.format.monetary_bhv_over_t(m, distribution)
                for m in monetary_bhv
            ]

            # Average all that
            monetary_over_t_means = analysis.tools.format.sim_monetary_behavior_mean_over_t(monetary_over_t)

            # ------------------------- Medium ------------------------------- #

            # BAR PLOTS
            # reformat each economies to compress on agents
            medium_over_user = [
                analysis.tools.format.medium_over_user(m)
                for m in medium
            ]

            # average all that
            medium_over_user_mean = \
                analysis.tools.format.sim_medium_mean_over_user(medium_over_user)

            # Now we can do stats
            med_sig = analysis.stats.mean_comparison.run(medium_over_user_mean, print_latex=True,
                                                         xp_session=xp_session, measure="MoE")

            # reformat for bar plots
            medium_means, medium_err = \
                analysis.tools.format.sim_medium_bar_plot(medium_over_user_mean)

            # CURVE PLOTS
            # compress each economies on time
            medium_over_t = [
                analysis.tools.format.medium_over_t(m)
                for m in medium
            ]

            # average all that
            medium_over_t_means = analysis.tools.format.sim_medium_mean_over_t(medium_over_t)

            d = {
                'monetary_bar': (monetary_means, monetary_err, money_sig),
                'monetary_over_t': monetary_over_t,
                'monetary_over_t_means': monetary_over_t_means,
                'medium_bar': (medium_means, medium_err, med_sig),
                'medium_over_t': medium_over_t,
                'medium_over_t_means': medium_over_t_means,
                'distribution': distribution
            }

            data.append(d)
            print()

        analysis.graph.overall.experiment(
            data, titles, f_name=f'fig/sim_{n_good}.pdf', exp=False
        )


if __name__ == '__main__':

    # Create fig folder
    os.makedirs("fig", exist_ok=True)

    # # Uncomment for running simulations used for phase diagram
    phase_diagram()

    # # Uncomment for experiment analysis and experiment-like simulations
    sim_overall()
    exp_overall()

    #   PROBABLY TO REMOVE !!!!!!
    # simulation.supplementary_exploitation.main()
