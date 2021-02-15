import pandas as pd

from helper import get_data


def combine_several_data(show=False):
    symbols = ["BBCA.JK", "BBRI.JK"]

    start_date = "2020-01-01"
    end_date = "2020-02-01"

    dates = pd.date_range(start_date, end_date)

    df = get_data(symbols, dates)

    if show:
        print(df)

    return df


def run():
    # combine_several_data(True)

    df = combine_several_data()
    # Slice by row range (dates) using DataFrame.ix[] selector
    print(df.loc["2020-01-01":"2020-01-10"])

    # Slice by column (symbols)
    print(df["BBCA.JK"])
    print(df[["BBCA.JK", "BBRI.JK"]])

    # # Slice by row and column
    print(df.loc["2020-01-01":"2020-01-10", ["BBCA.JK", "BBRI.JK"]])


if __name__ == "__main__":
    run()
