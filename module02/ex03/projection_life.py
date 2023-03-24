import pandas as pd
from matplotlib import pyplot as plt
from load_csv import load


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


if __name__ == "__main__":

    aff_pop(load("life_expectancy_years.csv"),
            load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv"))
