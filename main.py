import pandas as pd
import matplotlib.pyplot as plt

def test_run():
  # Define date range
  start_date = "2019-01-01"
  end_date = "2019-04-01"
  dates = pd.date_range(start_date, end_date)

  # Create an empty dataframe
  df1 = pd.DataFrame(index = dates)

  # Read INDF data into temporary dataframe
  dfINDF = pd.read_csv("data/INDF.JK.csv",
    index_col = "Date",
    parse_dates = True,
    usecols=["Date", "Adj Close"],
    na_values=["nan"])

  # Join the two dataframes using DataFrame.join()
  df1 = df1.join(dfINDF, how = "inner")

  # Drop NaN Values
  print(df1)

if __name__ == "__main__":
  test_run()
