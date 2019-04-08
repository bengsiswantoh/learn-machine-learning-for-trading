import pandas as pd

def get_max_close(symbol):
  df = pd.read_csv("data/{}.csv".format(symbol))
  return df["Close"].max()

def get_mean_volume(symbol):
  df = pd.read_csv("data/{}.csv".format(symbol))
  return df["Volume"].mean()

def test_run():
  for symbol in ["BBRI.JK" ,"INDF.JK"]:
    print("Mean Volume")
    print(symbol, get_mean_volume(symbol))

if __name__ == "__main__":
  test_run()
