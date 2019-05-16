import numpy as np


def main():

    prod = 1
    cons = 2
    t_max = 10000
    n_goods = 4

    ih = prod

    goods = list(range(n_goods))

    ind_ex = {i: 0 for i in range(n_goods)}
    dir_ex = 0

    n = 0

    for t in range(t_max):
        _goods = goods.copy()
        _goods.remove(ih)

        c = np.random.choice(_goods)

        # Check if direct
        # if (ih, c) == (prod, cons):
        #     dir_ex += 1
        # else:
        #     for g in goods:
        #         if (ih, c) in [(prod, g), (g, cons)]:
        #             ind_ex[g] += 1
        if ih == prod:
            n += 1

            if int(c == cons):
                dir_ex += 1
            else:
                ind_ex[c] += 1

        ih = c

    dir_ex /= n
    ind_ex = {k: v/n for k, v in ind_ex.items()}

    print(f'dir: {dir_ex}')
    for g in range(n_goods):
        print(f'ind with {g}: {ind_ex[g]}')


if __name__ == "__main__":
    main()
