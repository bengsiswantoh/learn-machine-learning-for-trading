import numpy as np

def test_run():
  # sample numbers from Gaussian (normal) distribution
  print(np.random.normal(50, 10, size = (2, 3))) # change mean to 50 and s.d. to 10

if __name__ == "__main__":
  test_run()