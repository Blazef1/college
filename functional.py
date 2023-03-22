import numpy as np
import matplotlib.pyplot as plt


def quadro():
    x = np.linspace(1, 3, 10)
    y = x ** 2 - 2 * x + 1
    plt.plot(x, y)
    plt.show()

def line():
    x = np.linspace(-10, 10, 10)
    y = x + 3
    plt.plot(x, y)
    plt.show()

def cube():
    x = np.linspace(-15, 15, 15)
    y = x ** 3
    plt.plot(x, y)
    plt.show()

