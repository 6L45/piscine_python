#! /bin/python3

import sys
import pandas as pd
from matplotlib import pyplot as plt
import matplotlib.ticker as mticker
from load_csv import load


def convert_K_M_B_values(x):
    if x.endswith('M'):
        return float(x[:-1])
    elif x.endswith('k'):
        return float(x[:-1]) * 1e-3
    elif x.endswith('B'):
        return float(x[:-1]) * 1e3
    else:
        return float(x)


def format_y_ticks(x, pos):
    if x % 20 == 0:
        return f"{int(x)}M"
    return ""


def aff_pop(df: pd.DataFrame, countries: list):
    """
        return a dataset from csv file path
    """

    # SET PLOT
    fig, ax = plt.subplots()
    myLocator = mticker.MultipleLocator(40)
    ax.xaxis.set_major_locator(myLocator)

    try:
        df = df.loc[:, 'country':'2050']
        df.set_index("country", inplace=True)
        country_data = df.loc["France"]

        country_data = pd.DataFrame(country_data)
        country_data = country_data.map(lambda x:
                                        convert_K_M_B_values(x))
        plt.plot(country_data.index, country_data.values, label="France")

        if countries:
            for country in countries:
                country_data = df.loc[country]
                country_data = pd.DataFrame(country_data)
                country_data = country_data.map(lambda x:
                                                convert_K_M_B_values(x))
                plt.plot(country_data.index, country_data.values,
                         label=country)

    except (FileNotFoundError, pd.errors.EmptyDataError,
            pd.errors.ParserError, IsADirectoryError):
        print("Et non gaston!")
        exit()
    except KeyError as e:
        print("KeyError", e)
        exit()

    ax.yaxis.set_major_formatter(mticker.FuncFormatter(format_y_ticks))

    # TITLES GRAPH X AND Y
    plt.title("populations Projections")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.legend()

    try:
        # CREATE AND SHOW
        plt.show()
    except KeyboardInterrupt:
        print("\rquit")
        exit()


def main():
    if len(sys.argv) > 1:
        aff_pop(load("population_total.csv"), sys.argv[1:])


if __name__ == "__main__":
    main()
