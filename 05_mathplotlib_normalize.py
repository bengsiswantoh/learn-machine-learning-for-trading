import pandas as pd
import matplotlib.pyplot as plt

from helper import get_data


def normalize_data(df, symbols, start_date):
    start_values = {}
    for s in symbols:
        start_values[s] = df.loc[start_date, s]
        print(start_values[s])

    for date in df.index:
        print(date)
        for s in symbols:
            df.loc[date, s] = df.loc[date, s] / start_values[s]

    return df


def plot_data(df, title="Stock prices"):
    ax = df.plot(title=title, fontsize=2)
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    plt.show()


def filter_data(df, columns, start_index, end_index):
    return df.loc[start_index:end_index, columns]


def run():
    # Define date range
    start_date = "2019-01-01"
    end_date = "2020-04-01"
    dates = pd.date_range(start_date, end_date)

    symbols = ["BBCA.JK", "BBRI.JK"]

    df = get_data(symbols, dates)

    start_date_filter = "2019-02-01"
    df = filter_data(df, ["BBCA.JK", "BBRI.JK"],
                     start_date_filter, "2019-04-01")
    plot_data(df)
    df = normalize_data(df, symbols, start_date_filter)
    plot_data(df)


if __name__ == "__main__":
    run()
