import graph.learning_curves
import analysis.basile


def main():

    data = analysis.basile.learning_curves_xp()
    graph.learning_curves.plot(data, f_name='fig/ind0_freq_over_time_{}.pdf')


if __name__ == "__main__":

    main()