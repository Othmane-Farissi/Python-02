import matplotlib.pyplot as plt
from load_csv import load
import numpy as np
import matplotlib.ticker as mtick


def parse_number(value: str) -> float:
    """
    Convert values like '2.5M', '300K', or plain numbers into float.
    """
    value = str(value).strip()
    if value.endswith("M"):
        return float(value[:-1]) * 1_000_000
    elif value.endswith("K"):
        return float(value[:-1]) * 1_000
    try:
        return float(value)
    except ValueError:
        return np.nan


def main():
    try:
        gdp_data = load(
            "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
            )
        life_data = load("life_expectancy_years.csv")

        if gdp_data is None or life_data is None:
            raise AssertionError("dataset is empty")

        gdp_1900 = gdp_data["1900"].apply(parse_number).to_numpy()
        life_1900 = life_data["1900"].apply(parse_number).to_numpy()

        if len(gdp_1900) == 0 or len(life_1900) == 0:
            raise AssertionError("no country for the year provided")

        plt.scatter(gdp_1900, life_1900, alpha=0.7, label="Countries")

        plt.title("1900")
        plt.xlabel("GDP per person (PPP, inflation adjusted)")
        plt.xscale("log")
        plt.gca().xaxis.set_major_formatter(
            mtick.StrMethodFormatter('{x:.0f}'))
        plt.gca().xaxis.set_major_formatter(
            mtick.FuncFormatter(lambda x, _: f"{int(x/1000)}k"))
        plt.ylabel("Life expectancy (years)")
        plt.legend()
        plt.show()

    except AssertionError as e:
        print(f"ERROR: {e}")


if __name__ == "__main__":
    main()
