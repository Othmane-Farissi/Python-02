import pandas as pd

def load(path: str):
    try:
        dt = pd.read_csv(path)
        if dt is None:
            raise ValueError("Failed to load dataset")
        return dt

    except ValueError as e:
        print("ERROR:{e}")
