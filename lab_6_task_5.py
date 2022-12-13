import matplotlib.pyplot as plt
import numpy as np

def lissagy_plotter(A, B, a, b, t):
    o = np.pi / 2
    x = A * np.sin(a * t + o)
    y = B * np.sin(b * t)

    X, Y = np.meshgrid(x, y)

    plt.plot(x, y, label='lissagy')
    plt.xlabel('coord - x')
    plt.ylabel('coord - y')
    plt.axis('equal')
    plt.savefig('pic_5.png')

lissagy_plotter(1, 2, 1, 0.5, 3)