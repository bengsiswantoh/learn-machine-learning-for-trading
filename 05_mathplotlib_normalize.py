import pandas as pd
import matplotlib.pyplot as plt

from helper import get_data


def normalize_data(df):
    return df / df.loc[0, :]


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

    df = filter_data(df, ["BBCA.JK", "BBRI.JK"], "2019-02-01", "2019-04-01")
    plot_data(df)
    # plot_data(normalize_data(df))


if __name__ == "__main__":
    run()
