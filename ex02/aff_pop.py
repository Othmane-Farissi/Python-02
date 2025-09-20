import matplotlib.pyplot as plt
from load_csv import load
import numpy as np


def parse_population(value: str) -> float:
    """
    Convert population string to float.
    Examples:
        '2.5M' -> 2_500_000
        '300K' -> 300_000
        '1000' -> 1000
    """
    value = value.strip()
    if value.endswith("M"):
        return float(value[:-1]) * 1_000_000
    elif value.endswith("K"):
        return float(value[:-1]) * 1_000
    else:
        return float(value)


def main():
    try:
        data = load("population_total.csv")
        if data is None:
            raise AssertionError("dataset is empty")

        country_one = "Morocco"
        country_two = "Spain"

        country_one_row = data[data["country"] == country_one]
        country_two_row = data[data["country"] == country_two]

        if country_one_row.empty or country_two_row.empty:
            raise AssertionError(f"country {country_one} or {country_two} not found")

        years = np.array(data.columns[1:]).astype(int)
        pop_one = np.array([parse_population(x) for x in country_one_row.iloc[0, 1:]])
        pop_two = np.array([parse_population(x) for x in country_two_row.iloc[0, 1:]])

        plt.plot(years, pop_one / 1_000_000, label=country_one)
        plt.plot(years, pop_two / 1_000_000, label=country_two)

        plt.title("Population projections")
        plt.xlabel("Year")
        plt.ylabel("Population")
        plt.legend()
        plt.grid(True)
        plt.show()

    except AssertionError as e:
        print(f"ERROR: {e}")


if __name__ == "__main__":
    main()
