import matplotlib.pyplot as plt
import numpy as np

def log_spiral_plotter(b):
    f = np.arange(0, 8 * np.pi, 0.01)
    r = np.e ** (b * f)
    x = r * np.cos(f)
    y = r * np.sin(f)

    plt.plot(x, y, label='log spiral')
    plt.xlabel('coord - x')
    plt.ylabel('coord - y')
    plt.axis('equal')
    plt.savefig('pic_4.1.png')

# log_spiral_plotter(0.1)

def arh_spiral(k):
    f = np.arange(0, 8 * np.pi, 0.01)
    r = k * f
    x = r * np.cos(f)
    y = r * np.sin(f)

    plt.plot(x, y, label='arh spiral')
    plt.xlabel('coord - x')
    plt.ylabel('coord - y')
    plt.axis('equal')
    plt.savefig('pic_4.2.png')

#arh_spiral(0.2)

def gesl_spiral(k):
    f = np.arange(0.01, 8 * np.pi, 0.01)
    r = k / np.sqrt(f)
    x = r * np.cos(f)
    y = r * np.sin(f)

    plt.plot(x, y, label='gesl spiral')
    plt.xlabel('coord - x')
    plt.ylabel('coord - y')
    plt.axis('equal')
    plt.savefig('pic_4.3.png')

#gesl_spiral(0.3)

def rosa_spiral(k):
    f = np.arange(0.01, 8, 0.01)
    r = np.sin(k * f)
    x = r * np.cos(f)
    y = r * np.sin(f)

    plt.plot(x, y, label='rosa spiral')
    plt.xlabel('coord - x')
    plt.ylabel('coord - y')
    plt.axis('equal')
    plt.savefig('pic_4.4.png')

rosa_spiral(17)
