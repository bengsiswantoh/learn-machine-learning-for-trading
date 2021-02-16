import time
import numpy as np


def simple_test():
    t1 = time.time()
    print("ML4T")
    t2 = time.time()
    print("The time taken by print statement is ", t2 - t1, " seconds")


def how_long(func, *args):
    t0 = time.time()
    result = func(*args)
    t1 = time.time()
    return result, t1 - t0


def manual_mean(arr):
    sum = 0
    for i in range(0, arr.shape[0]):
        for j in range(0, arr.shape[1]):
            sum = sum + arr[i, j]
    return sum / arr.size


def numpy_mean(arr):
    return arr.mean()


def compare_numpy():
    nd1 = np.random.random((1000, 10000))

    res_manual, t_manual = how_long(manual_mean, nd1)
    res_numpy, t_numpy = how_long(numpy_mean, nd1)
    print("Manual: {:.6f} ({:.3f} secs) vs. Numpy: {:.6f} ({:.3f} secs)".format(
        res_manual, t_manual, res_numpy, t_numpy))

    # Make sure both give us the same number (upto some precision)
    assert abs(res_manual - res_numpy) <= 10e-6, "Results aren't equal!"

    # Compute speedup
    speedup = t_manual / t_numpy
    print("Numpy mean is", speedup, "times faster than manual for loops")


def run():
    # simple_test()
    compare_numpy()


if __name__ == "__main__":
    run()
