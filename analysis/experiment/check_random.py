import numpy as np


def main():

    prod = 1
    cons = 2
    t_max = 1000000
    n_goods = 3

    ih = prod

    goods = list(range(n_goods))

    ind_ex = {i: 0 for i in range(n_goods)}
    dir_ex = 0

    for t in range(t_max):
        _goods = goods.copy()
        _goods.remove(ih)

        c = np.random.choice(_goods)

        if (ih, c) == (prod, cons):
            dir_ex += 1
        else:
            for g in goods:
                if (ih, c) in [(prod, g), (g, cons)]:
                    ind_ex[g] += 1

    print(dir_ex/t_max)
    for g in range(n_goods):
        print(f'ind with {g}:', ind_ex[g] / t_max)


if __name__ == "__main__":
    main()
