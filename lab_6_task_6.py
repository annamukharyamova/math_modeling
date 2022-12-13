import matplotlib.pyplot as plt
import numpy as np

def ellips(p, e):
    f = np.arange(-0.5, 6 , 0.01)
    r = p / (1 + e * np.cos(f))
    x = r * np.cos(f)
    y = r * np.sin(f)

    plt.plot(x, y, label='ellips')
    plt.xlabel('coord - x')
    plt.ylabel('coord - y')
    plt.axis('equal')
    plt.savefig('pic_6.png')

ellips(10, 0.5)
