import pandas as pd

def load(path: str):
    try:
        dt = pd.read_csv(path)
        print(f"Loading dataset of dimensions: {dt.shape}")
        return dt

    except Exception:
        return None
