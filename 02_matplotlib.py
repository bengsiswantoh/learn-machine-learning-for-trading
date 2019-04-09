import pandas as pd
import matplotlib.pyplot as plt

def plot_column(df):
  df["Adj Close"].plot()
  plt.show()

def plot_2_columns(df):
  df[["Close", "Adj Close"]].plot()
  plt.show()

def run():
  df = pd.read_csv("data/INDF.JK.csv")
  plot_column(df)
  plot_2_columns(df)

if __name__ == "__main__":
  run()
