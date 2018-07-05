from scipy.optimize import minimize


def f(param):
    x, y = param
    return x**2 + y


def main():

    res = minimize(f, x0=(100, 100))
    print(res)


if __name__ == "__main__":
    main()