# https://numpy.org/doc/stable/reference/random/index.html

import numpy as np


def create_1D_array():
    print(np.array([2, 3, 4]))


def create_2D_array():
    print(np.array([(2, 3, 4), (5, 6, 7)]))


def create_1D_empty_array():
    print(np.empty(5))


def create_2D_empty_array():
    print(np.empty((5, 4)))


def create_3D_empty_array():
    print(np.empty((5, 4, 3)))


def create_array_specific_datatype():
    print(np.ones((5, 4), dtype=np.int_))


def create_array_random_values():
    print(np.random.random((5, 4)))


def create_array_random_values_alt():
    print(np.random.rand(5, 4))


def create_array_random_gaussian():
    print(np.random.normal(size=(2, 3)))


def create_array_random_gaussian_specific():
    # change mean to 50 and s.d. to 10
    print(np.random.normal(50, 10, size=(2, 3)))


def random_integers():
    # a single integer in [0, 10]
    print(np.random.randint(10))

    # same as above, specifying [low, high] explicit
    print(np.random.randint(0, 10))

    # 5 random integer as a 1D array
    print(np.random.randint(0, 10, size=5))

    # 2x3 array of random integers
    print(np.random.randint(0, 10, size=(2, 3)))


def run():
    create_1D_array()
    create_2D_array()
    create_1D_empty_array()
    create_2D_empty_array()
    create_3D_empty_array()
    create_array_specific_datatype()
    create_array_random_values()
    create_array_random_values_alt()
    create_array_random_gaussian()
    create_array_random_gaussian_specific()
    random_integers()


if __name__ == "__main__":
    run()
