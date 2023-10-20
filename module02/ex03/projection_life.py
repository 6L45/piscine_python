#! /bin/python3

import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.ticker import ScalarFormatter, FuncFormatter
from load_csv import load


def format_x_ticks(value, pos):
    if value == 1000:
        return "1k"
    elif value == 10000:
        return "10k"
    else:
        return str(int(value))


def aff_pop(df: pd.DataFrame, df2: pd.DataFrame):
    """
        return a dataset from csv file path
    """

    try:
        df.set_index("country", inplace=True)
        df2.set_index("country", inplace=True)

        newdf = pd.concat([df.loc[:, "1900"], df2.loc[:, "1900"]], axis=1)
        newdf.columns = ["expectancy", "product"]

        newdf.plot(kind="scatter", x="product", y="expectancy")

        plt.xscale("log")

        formatter = ScalarFormatter()
        formatter.set_scientific(False)  # Désactive la notation scientifique
        plt.gca().xaxis.set_major_formatter(formatter)

        custom_x_ticks = [300, 1000, 10000]
        plt.gca().xaxis.set_major_formatter(FuncFormatter(format_x_ticks))
        plt.xticks(custom_x_ticks)

    except (FileNotFoundError, pd.errors.EmptyDataError,
            pd.errors.ParserError, IsADirectoryError):
        print("Et non gaston!")
        exit()
    except KeyError as e:
        print("KeyError", e)
        exit()

    # TITLES GRAPH X AND Y
    plt.title("1900")
    plt.xlabel("Gross domestic product")
    plt.ylabel("Life Expectancy")

    try:
        # CREATE AND SHOW
        plt.show()
    except KeyboardInterrupt:
        print("\rquit")
        exit()


def main():
    aff_pop(load("life_expectancy_years.csv"),
            load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv"))


if __name__ == "__main__":
    main()
