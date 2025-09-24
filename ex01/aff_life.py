import matplotlib.pyplot as plt
from load_csv import load
import numpy as np


def main():
    """
    Plot the life expectancy over years for a specific country.

    - Loads a CSV dataset using the `load` function.
    - Extracts life expectancy data for a specific
      country (hardcoded as "Morocco").
    - Converts the years and life expectancy values
      to NumPy arrays.
    - Plots the data using matplotlib with labeled axes,
      title, legend, and grid.
    """
    try:
        data = load("life_expectancy_years.csv")
        if data is None:
            raise AssertionError("could not load Dataset")

        country_name = "Morocco"
        country_row = data[data["country"] == country_name]

        if country_row.empty:
            raise AssertionError("could not find {country_name} in dataset")

        years = np.array(data.columns[1:]).astype(int)
        age = np.array(country_row.iloc[0, 1:]).astype(int)

        plt.plot(years, age, label=country_name)
        plt.title(f"Life expectancy in {country_name}")
        plt.xlabel("Year")
        plt.ylabel("Life Expectancy (years)")
        plt.legend()
        plt.grid(True)
        plt.show()

    except AssertionError as e:
        print(f"ERROR: {e}")


if __name__ == "__main__":
    main()
