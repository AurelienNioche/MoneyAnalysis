import numpy as np

mapping = {
    414: np.array([9, 9, 18]),
    415: np.array([10, 10, 10, 10]),
    416: np.array([10, 10, 10]),
    417: np.array([10, 10, 20, 20])
}


def get(room_id):

    return mapping[room_id]