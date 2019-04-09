import numpy as np

def test_run():
  # Random Integers
  print(np.random.randint(10)) # a single integer in [0, 10]
  print(np.random.randint(0, 10)) # same as above, specifying [low, high] explicit
  print(np.random.randint(0, 10, size = 5)) # 5 random integer as a 1D array
  print(np.random.randint(0, 10, size = (2, 3))) # 2x3 array of random integers

if __name__ == "__main__":
  test_run()
