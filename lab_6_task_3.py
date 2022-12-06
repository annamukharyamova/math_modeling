import matplotlib.pyplot as plt
import numpy as np

def ellips_plotter(a, b):
    x = np.arange(-2*radius, 2*radius, 0.1)
    y = np.arange(-2*radius, 2*radius, 0.1)

    X, Y = np.meshgrid(x, y)

    fxy = X**2 / a**2 + Y**2 / b**2 - 1

    plt.contour(X, Y, fxy)
    plt.axis('equal')
    plt.savefig('pic_1.png')

ellips_plotter(2, 3)
