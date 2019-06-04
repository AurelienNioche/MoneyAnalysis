import analysis.supplementary
import graph.sim_and_xp
import analysis.stats.stats


def main():

    name_extension = 'FIT_non_heterogeneous'
    fig_data = analysis.supplementary.supplementary_fit(heterogeneous=False)
    graph.sim_and_xp.plot(fig_data, name_extension=name_extension)
    analysis.stats.stats.sim_and_xp(fig_data, name_extension=name_extension)

    name_extension = 'FIT_extended'
    fig_data = analysis.supplementary.supplementary_fit(heterogeneous=False, t_max=1000)
    graph.sim_and_xp.plot(fig_data, name_extension=name_extension)
    analysis.stats.stats.sim_and_xp(fig_data, name_extension=name_extension)


if __name__ == "__main__":

    main()
