
import numpy as np

def reshape_array():
    range = np.arange(12)
    range_3_4 = np.reshape(range, (3, 4))
    print(range_3_4)


def change_sign():
    array = np.arange(21)
    array[((array > 7) & (array < 16))] = -1 * array[((array > 7) & (array < 16))]
    print(array)


def inner_product():
    a = np.array([10, 1, 5])
    b = np.array([9, 3, 6])
    product = a*b
    inner_product = np.sum(product)
    print(inner_product)


def frob_norm():
    x = np.random.uniform(0, 1, size=(20,))
    frob_norm = np.linalg.norm(x)
    print("Frobenius norm: ", frob_norm)




def main():
    reshape_array()
    change_sign()
    inner_product()
    frob_norm()


if __name__ == "__main__":
    main()
