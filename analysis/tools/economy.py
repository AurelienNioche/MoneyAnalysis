import numpy as np


labels = {
    414: "3_good_non_uniform",
    415: "4_good_uniform",
    416: "3_good_uniform",
    417: "4_good_non_uniform"
}

repartitions = {
    414: np.array([9, 9, 18]),
    415: np.array([10, 10, 10, 10]),
    416: np.array([10, 10, 10]),
    417: np.array([10, 10, 20, 20])
}

