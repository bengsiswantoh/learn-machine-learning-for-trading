import pandas as pd
import matplotlib.pyplot as plt

def test_run():
  # Define date range
  start_date = "2019-01-01"
  end_date = "2019-04-01"
  dates = pd.date_range(start_date, end_date)

  # Create an empty dataframe
  df1 = pd.DataFrame(index = dates)

  # Read symbols data into temporary dataframe
  symbols = ["BBRI.JK", "INDF.JK"]
  for symbol in symbols:
    df_temp = pd.read_csv("data/{}.csv".format(symbol),
      index_col = "Date",
      parse_dates = True,
      usecols=["Date", "Adj Close"],
      na_values=["nan"])

    # Rename columns to symbol
    df_temp = df_temp.rename(columns={"Adj Close": symbol})

    # Join the two dataframes using DataFrame.join()
    df1 = df1.join(df_temp, how = "inner")

  print(df1)

if __name__ == "__main__":
  test_run()
