import pandas as pd

def print_all(df):
  print(df)

def print_first_five(df):
  print(df.head())

def print_last_five(df):
  print(df.tail())

def print_spesific_index(df):
  print(df[10:21])

def get_max_close(symbol):
  df = pd.read_csv("data/{}.csv".format(symbol))
  return df["Close"].max()

def get_mean_volume(symbol):
  df = pd.read_csv("data/{}.csv".format(symbol))
  return df["Volume"].mean()

def run():
  df = pd.read_csv("data/INDF.JK.csv")
  print_all(df)
  print_first_five(df)
  print_last_five(df)
  print_spesific_index(df)

  for symbol in ["BBRI.JK" ,"INDF.JK"]:
    print("Max Close")
    print(symbol, get_max_close(symbol))
    print("Mean Volume")
    print(symbol, get_mean_volume(symbol))

if __name__ == "__main__":
  run()
