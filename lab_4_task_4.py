import numpy as np

def y(a, b, n):
    x = np.linspace(a, b, n)
    y = x ** 2
    print(y)

y(-10, 10, 100)