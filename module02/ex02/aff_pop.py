import sys
import pandas as pd
from matplotlib import pyplot as plt
import matplotlib.ticker as mticker
from load_csv import load


def aff_pop(df: pd.DataFrame, countries: list):
    """
        return a dataset from csv file path
    """

    # SET PLOT
    fig, ax = plt.subplots()
    myLocator = mticker.MultipleLocator(40)
    ax.xaxis.set_major_locator(myLocator)

    try:
        df.set_index("country", inplace=True)
        country_data = df.loc["France"]
        plt.plot(country_data.index, country_data.values, label="France")

        if countries:
            for country in countries:
                country_data = df.loc[country]
                plt.plot(country_data.index, country_data.values,
                         label=country)

    except (FileNotFoundError, pd.errors.EmptyDataError,
            pd.errors.ParserError, IsADirectoryError):
        print("Et non gaston!")
        exit()
    except KeyError as e:
        print("KeyError", e)
        exit()

    # TITLES GRAPH X AND Y
    plt.title("populations Projections")
    plt.xlabel("Year")
    plt.ylabel("Life Expectancy")
    plt.legend()

    try:
        # CREATE AND SHOW
        plt.show()
    except KeyboardInterrupt:
        print("\rquit")
        exit()


if __name__ == "__main__":

    aff_pop(load("life_expectancy_years.csv"), sys.argv[1:])
