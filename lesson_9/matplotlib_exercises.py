import numpy as np
from matplotlib import pyplot as plt


def init_range():
    x = np.linspace(-1, 1, 1000)
    return x


def one_over_x(x):
    y = 1/x
    return y


def plot(x, y):
    plt.plot(x, y)
    plt.show()


def main():
    x = init_range()
    y = one_over_x(x)
    plot(x, y)


if __name__ == "__main__":
    main()

