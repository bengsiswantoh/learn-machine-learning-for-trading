import numpy as np


def run():
    # Random Integers
    a = np.random.random((5, 4))
    print(a.shape)
    print(a.shape[0])  # number of rows
    print(a.shape[1])  # number of columns
    print(len(a.shape))  # dimension in an array
    print(a.size)  # total number of elements in an array
    print(a)
    print(a.dtype)

    a = np.random.seed(693)  # seed the random number generator
    a = np.random.randint(0, 10, size=(5, 4))
    print("Array:\n", a)

    # Sum of all elements
    print("Sum of all elements:", a.sum())

    # Iterate over rows, to compute sum of each column
    print("Sum of each column:\n", a.sum(axis=0))

    # Iterate over columns, to compute sum of each row
    print("Sum of each row:\n", a.sum(axis=1))

    # Statistics: min, max, mean (across rows, cols, and overall)
    print("Minimum of each column:\n", a.min(axis=0))
    print("Maximum of each row:\n", a.max(axis=1))
    print("Mean of all elements:\n", a.mean())

    a = np.array([9, 6, 2, 3, 12, 14, 7, 10],
                 dtype=np.int32)  # 32-bit integer array
    print("Array:", a)

    # Find the maximum and its index in array
    print("Maximum value:", a.max())
    print("Index of max.:", a.argmax())


if __name__ == "__main__":
    run()
