import graph.supplementary.gender
import graph.learning_curves

import analysis.basile
import analysis.stats.stats


def ind0_freq_over_time():

    data = analysis.basile.learning_curves_xp()
    graph.learning_curves.plot(data, f_name='fig/ind0_freq_over_time_{}.pdf')


def supplementary_gender():
    obs_type = 'ind_0'
    data = analysis.basile.supplementary_gender(obs_type=obs_type)
    graph.supplementary.gender.plot(data)
    analysis.stats.stats.supplementary_gender(data, obs_type=obs_type)


if __name__ == "__main__":

    # ind0_freq_over_time()
    supplementary_gender()

