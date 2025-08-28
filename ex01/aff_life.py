import matplotlib.pyplot as plt
from load_csv import load
import numpy as np

def main():
    # Load dataset
    data = load("life_expectancy_years.csv")
    if data is None:
        print("Error: could not load dataset")
        return

    # Select country
    country_name = "Morocco"
    country_row = data[data["country"] == country_name]

    if country_row.empty:
        print(f"Error: country {country_name} not found in dataset")
        return

    # Extract years and values as 1D arrays
    years = np.array(data.columns[1:]).astype(int)
    values = np.array(country_row.iloc[0, 1:]).astype(float)

    # Plot
    plt.plot(years, values, label=country_name)
    plt.title(f"Life Expectancy in {country_name}")
    plt.xlabel("Year")
    plt.ylabel("Life Expectancy (years)")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
