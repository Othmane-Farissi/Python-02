import pandas as pd


def load(path: str):
    """
    Load a CSV file into a pandas DataFrame.

    Args:
        path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: The loaded dataset.
    """
    try:
        dt = pd.read_csv(path)
        if dt is None:
            raise ValueError("Failed to load dataset")
        return dt

    except ValueError as e:
        print(f"ERROR:{e}")
