import pandas as pd
from matplotlib import pyplot as plt
import matplotlib.ticker as mticker
from load_csv import load


def aff_life(df: pd.DataFrame):
    """
        return a dataset from csv file path
    """

    # SET PLOT
    fig, ax = plt.subplots()
    myLocator = mticker.MultipleLocator(40)
    ax.xaxis.set_major_locator(myLocator)

    try:
        df.set_index('country', inplace=True)
        country_data = df.loc['France']

    except (FileNotFoundError, pd.errors.EmptyDataError,
            pd.errors.ParserError, IsADirectoryError):
        print("Et non gaston!")
        exit()
    except KeyError as e:
        print("KeyError", e)
        exit()
    except KeyboardInterrupt:
        print("\rquit")
        exit()

    # TITLES GRAPH X AND Y
    plt.title("France Life expectancy Projections")
    plt.xlabel("Year")
    plt.ylabel("Life Expectancy")

    # CREATE AND SHOW
    plt.plot(country_data.index, country_data.values)
    plt.show()


if __name__ == "__main__":

    aff_life(load("life_expectancy_years.csv"))
