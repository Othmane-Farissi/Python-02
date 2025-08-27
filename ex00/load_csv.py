import pandas as pd 

def load_csv(path : str) :
    try:
        dt = pd.read_csv(path)
        print(f"Loading dataset of dimensions {data.shape}")

        return dt
    except Exception:
        return None
