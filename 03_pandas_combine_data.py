import pandas as pd


def create_data_frame_with_dates_as_index(show=False):
    start_date = "2021-01-01"
    end_date = "2021-02-01"

    dates = pd.date_range(start_date, end_date)

    df = pd.DataFrame(index=dates)
    if show:
        print(df)

    return df


def join_and_drop(df, df_temp):
    df = df.join(df_temp)
    df = df.dropna()
    return df


def inner_join(df, df_temp):
    df = df.join(df_temp, how="inner")
    return df


def create_BBCA_with_dates_as_index():
    df = create_data_frame_with_dates_as_index()

    dfBBCA = pd.read_csv("data/BBCA.JK.csv",
                         index_col="Date",
                         parse_dates=True,
                         usecols=["Date", "Adj Close"],
                         na_values=["nan"])

    # df = join_and_drop(df, dfBBCA)

    df = inner_join(df, dfBBCA)

    print(df)


def combine_several_data():
    symbols = ["BBCA.JK", "BBRI.JK"]

    df = create_data_frame_with_dates_as_index()

    for symbol in symbols:
        df_temp = pd.read_csv("data/{}.csv".format(symbol),
                              index_col="Date",
                              parse_dates=True,
                              usecols=["Date", "Adj Close"],
                              na_values=["nan"])

        # Rename columns to symbol
        df_temp = df_temp.rename(columns={"Adj Close": symbol})

        # Join the two dataframes using DataFrame.join()
        df = df.join(df_temp, how="inner")

    print(df)


def run():
    create_data_frame_with_dates_as_index(True)
    create_BBCA_with_dates_as_index()
    combine_several_data()


if __name__ == "__main__":
    run()
