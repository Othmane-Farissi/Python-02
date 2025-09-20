import matplotlib.pyplot as plt
from load_csv import load
import numpy as np

def main():
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
