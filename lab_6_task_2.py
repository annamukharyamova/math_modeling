import matplotlib.pyplot as plt
import numpy as np

def giperbola_plotter_1(k):
    x = np.arange(-10, 0, 0.03)
    y = k / x 

    plt.plot(x, y, label='my giperbola')
    plt.xlabel('coord - x')
    plt.ylabel('coord - y')
    plt.legend()
    plt.savefig('pic_1.png')

def giperbola_plotter_2(k):
    x = np.arange(0, 10, 0.03)
    y = k / x 

    plt.plot(x, y, label='my giperbola')
    plt.xlabel('coord - x')
    plt.ylabel('coord - y')
    plt.legend()
    plt.savefig('pic_1.png')


giperbola_plotter_1(5)
giperbola_plotter_2(5)