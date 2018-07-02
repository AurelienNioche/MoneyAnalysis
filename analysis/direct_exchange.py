from analysis.conversion import Converter
from game.models import User, Choice, Room
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as grd


def run():

    rooms = Room.objects.all().order_by('id')

    room_id = [r.id for r in rooms]

    room_t_max = [r.t_max for r in rooms]

    room_n_good = [r.n_type for r in rooms]

    # -------------------------------- #
    # ------- Analyse by room -------- #
    # -------------------------------- #

    # ---- Pooled over time ------ #

    for i, r_id in enumerate(room_id):

        print("Room ", i)

        n_good = room_n_good[i]

        print("N good", n_good)
        print()

        good_list = [n_good - 1, ] + list(range(n_good - 1))

        for prod_good in good_list:

            users = User.objects.filter(room_id=r_id, production_good=Converter.reverse_value(prod_good, n_good=n_good))
            u_id = [u.id for u in users]

            cpt_good = Converter.convert_value(users[0].consumption_good, n_good=n_good)
            print("Prod", prod_good, "Cons", cpt_good, "N", len(u_id))

            u_score = [u.score for u in users]

            means = []

            for ui, us in zip(u_id, u_score):
                choices = Choice.objects.filter(room_id=r_id, user_id=ui, t__gt=29)

                in_hand = np.asarray(Converter.convert([c.good_in_hand for c in choices], n_good=n_good))
                desired = np.asarray(Converter.convert([c.desired_good for c in choices], n_good=n_good))

                prod_in_hand = in_hand == prod_good
                cpt_for_desired = desired == cpt_good

                dir_ex = prod_in_hand * cpt_for_desired
                means.append(np.mean(dir_ex))
                # #print(f"Prop dir exch {np.mean(dir_ex):.2f}; Score {us}")

            print(f"Dist of means = {means}")
            print(f"Mean = {np.mean(means):.2f} (+/- {np.std(means):.2f}); median = {np.median(means):.2f}")
            print("-" * 5)

    # -------------- By time step  ---------- #

    data_list = []

    for i, r_id in enumerate(room_id):

        print("Room ", i)

        t_max = room_t_max[i]
        n_good = room_n_good[i]

        print("N good", n_good)
        print()

        good_list = [n_good - 1, ] + list(range(n_good - 1))

        data = np.zeros((t_max, n_good))

        for agent_idx, prod_good in enumerate(good_list):

            users = User.objects.filter(room_id=r_id, production_good=Converter.reverse_value(prod_good, n_good=n_good))
            u_id = [u.id for u in users]

            cpt_good = Converter.convert_value(users[0].consumption_good, n_good=n_good)
            print("Prod", prod_good, "Cons", cpt_good, "N", len(u_id))

            for t in range(t_max):

                choices = Choice.objects.filter(room_id=r_id, user_id__in=u_id, t=t)

                in_hand = np.asarray(Converter.convert([c.good_in_hand for c in choices], n_good=n_good))
                desired = np.asarray(Converter.convert([c.desired_good for c in choices], n_good=n_good))

                prod_in_hand = in_hand == prod_good
                cpt_for_desired = desired == cpt_good

                dir_ex = prod_in_hand * cpt_for_desired

                print(f"Prop dir exch for {t}: {np.mean(dir_ex):.2f}")

                data[t, agent_idx] = np.mean(dir_ex)

        data_list.append(data)
        print("*" * 10)

    fig = plt.figure()
    gs = grd.GridSpec(nrows=2, ncols=2)

    ax = fig.add_subplot(gs[0, 0])
    ax.plot(data_list[0])
    ax.set_ylim(0, 1)

    ax = fig.add_subplot(gs[0, 1])
    ax.plot(data_list[1])
    ax.set_ylim(0, 1)

    ax = fig.add_subplot(gs[1, 0])
    ax.plot(data_list[2])
    ax.set_ylim(0, 1)

    ax = fig.add_subplot(gs[1, 1])
    ax.plot(data_list[3])
    ax.set_ylim(0, 1)

    plt.show()