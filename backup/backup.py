import pickle
import os


def save(obj, file_name):

    dir_path = os.path.dirname(file_name)
    if dir_path:
        os.makedirs(dir_path, exist_ok=True)
    print(f"Saving file '{file_name}'...")
    with open(file_name, 'wb') as f:
        pickle.dump(obj=obj, file=f)
    print("Done")


def load(file_name):

    print(f"Loading file '{file_name}'...")
    data = pickle.load(file=open(file_name, 'rb'))
    print("Done")
    return data
