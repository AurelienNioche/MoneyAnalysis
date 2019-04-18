import numpy as np


# def running_mean(l, N):
#     sum = 0
#     result = list(0 for x in l)
#
#     for i in range(0, N):
#         sum = sum + l[i]
#         result[i] = sum / (i + 1)
#
#     for i in range(N, len(l)):
#         sum = sum - l[i - N] + l[i]
#         result[i] = sum / N
#
#     return result


def running_mean(x, n):
    """
    :param x: data
    :param n: window size
    :return:
    """
    return np.convolve(x, np.ones(n) / n, mode='valid')
