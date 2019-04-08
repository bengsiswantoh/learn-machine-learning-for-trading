import pandas as pd

def test_run():
  df = pd.read_csv("data/INDF.JK.csv")
  # print(df)
  # print(df.head())
  # print(df.tail())
  print(df[10:21])

if __name__ == "__main__":
  test_run()
