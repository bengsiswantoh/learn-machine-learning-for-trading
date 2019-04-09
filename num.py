import numpy as np

def test_run():
  # Random Integers
  a = np.random.random((5, 4))
  print(a.shape)
  print(a.shape[0]) # number of rows
  print(a.shape[1]) # number of columns
  print(len(a.shape))
  print(a.size)
  print(a)
  print(a.dtype)

if __name__ == "__main__":
  test_run()
