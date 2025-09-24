import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from load_csv import load
import numpy as np


def parse_population(value: str) -> float:
    """
    Convert population string to float.
    """
    value = value.strip()
    if value.endswith("M"):
        return float(value[:-1]) * 1_000_000
    elif value.endswith("K"):
        return float(value[:-1]) * 1_000
    else:
        return float(value)


def millions_formatter(x, pos):
    """Format large numbers into 'XM' style."""

    return f"{int(x/1_000_000)}M"


def main():
    """
    Plot the historical and projected population of two countries.

    - Loads population data from a CSV file using `load()`.
    - Extracts population data for two specific countries.
    - Filters the years to the range 1800–2050.
    - Converts population values to numbers using `parse_population()`.
    - Plots both countries' population over time using matplotlib.
    - Formats the Y-axis to display population in millions.
    - Adds title, labels, grid, and legend for clarity.
    """
    try:
        data = load("population_total.csv")
        if data is None:
            raise AssertionError("dataset is empty")

        country_one = "Morocco"
        country_two = "Spain"

        country_one_row = data[data["country"] == country_one]
        country_two_row = data[data["country"] == country_two]

        if country_one_row.empty or country_two_row.empty:
            raise AssertionError(
                f"country {country_one} or {country_two} not found"
            )

        years = np.array(data.columns[1:]).astype(int)
        mask = (years >= 1800) & (years <= 2050)
        years = years[mask]

        pop_one = np.array(
            [parse_population(v) for v in country_one_row.iloc[0, 1:]]
        )[mask]

        pop_two = np.array(
            [parse_population(v) for v in country_two_row.iloc[0, 1:]]
        )[mask]

        # Plot the populations
        plt.plot(years, pop_one, label=country_one)
        plt.plot(years, pop_two, label=country_two)

        plt.title("Population projections")
        plt.xlabel("Year")
        plt.ylabel("Population")

        plt.gca().yaxis.set_major_formatter(FuncFormatter(millions_formatter))

        plt.legend()
        plt.grid(True)
        plt.show()

    except AssertionError as e:
        print(f"ERROR: {e}")


if __name__ == "__main__":
    main()
