import pandas as pd
import matplotlib.pyplot as plt

def test_run():
  start_date = "2018-01-01"
  end_date = "2018-01-30"
  dates = pd.date_range(start_date, end_date)
  df1 = pd.DataFrame(index = dates)

if __name__ == "__main__":
  test_run()
