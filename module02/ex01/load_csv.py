import sys
import pandas as pd


def load(path: str) -> pd.DataFrame:
    """
        return a dataset from csv file path
    """

    try:
        df = pd.read_csv(path)

    except (FileNotFoundError, pd.errors.EmptyDataError,
            pd.errors.ParserError, IsADirectoryError):
        print("Et non gaston!")
        exit()

    print(f"loading dataset of dimensions ({df.shape[0]}, {df.shape[1]})")
    print(df)

    return df


def main():
    if len(sys.argv) != 2 or sys.argv[1].split(".")[-1] != "csv":
        print("bad arguments")
        exit()

    load(sys.argv[1])


if __name__ == "__main__":
    main()
