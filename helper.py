import os
import pandas as pd


def symbol_to_path(symbol, base_dir="data"):
    # Return CSV path given ticker symbol
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))


def get_data(symbols, dates):
    # Read stock data (adjusted close) for given symbols from CSV files
    df = pd.DataFrame(index=dates)

    for symbol in symbols:
        df_temp = pd.read_csv(symbol_to_path(symbol),
                              index_col="Date",
                              parse_dates=True,
                              usecols=["Date", "Adj Close"],
                              na_values=["nan"])

        # Rename columns to symbol
        df_temp = df_temp.rename(columns={"Adj Close": symbol})

        # Join the two dataframes using DataFrame.join()
        df = df.join(df_temp, how="inner")

    return df
