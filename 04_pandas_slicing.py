import os
import pandas as pd

def symbol_to_path(symbol, base_dir="data"):
  # Return CSV path given ticker symbol
  return os.path.join(base_dir, "{}.csv".format(str(symbol)))

def get_data(symbols, dates):
  # Read stock data (adjusted close) for given symbols from CSV files
  df = pd.DataFrame(index = dates)

  for symbol in symbols:
    df_temp = pd.read_csv(symbol_to_path(symbol),
      index_col = "Date",
      parse_dates = True,
      usecols=["Date", "Adj Close"],
      na_values=["nan"])

    # Rename columns to symbol
    df_temp = df_temp.rename(columns={"Adj Close": symbol})

    # Join the two dataframes using DataFrame.join()
    df = df.join(df_temp, how = "inner")

  return df

def combine_several_data(show = False):
  symbols = ["BBRI.JK", "INDF.JK"]

  start_date = "2018-01-01"
  end_date = "2018-02-01"

  dates = pd.date_range(start_date, end_date)

  df = get_data(symbols, dates)

  if show:
    print(df)

  return df

def run():
  # combine_several_data(True)

  df = combine_several_data()
  # Slice by row range (dates) using DataFrame.ix[] selector
  print(df.ix["2018-01-01":"2018-01-10"])

  # Slice by column (symbols)
  print(df["INDF.JK"])
  print(df[["BBRI.JK", "INDF.JK"]])

  # Slice by row and column
  print(df.ix["2018-01-01":"2018-01-10", ["BBRI.JK", "INDF.JK"]])

if __name__ == "__main__":
  run()
