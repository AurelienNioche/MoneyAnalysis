import analysis.exploratory

import graph.sim_and_xp
import analysis.stats.stats


def main():

    ext = 'MEDIAN_SPLIT'
    fig_data = analysis.exploratory.agent_selection()
    graph.sim_and_xp.plot(fig_data, name_extension=ext)
    analysis.stats.stats.sim_and_xp(fig_data, data_type=('SIM', 'SIM_SELECT'), name_extension=ext)


if __name__ == '__main__':

    main()
