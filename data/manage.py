import os
import pickle


def save(obj, file_name="data/data.p"):

    os.makedirs(os.path.dirname(file_name), exist_ok=True)

    # Save data in pickle
    with open(file_name, "wb") as f:
        pickle.dump(obj, f)


def load(file_name="data/data.p"):

    with open(file_name, "rb") as f:
        return pickle.load(f)
