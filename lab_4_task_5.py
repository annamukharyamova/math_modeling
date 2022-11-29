import numpy as np

def square(x, r, h, c, a, b):
    if x == 0:
        s =  np.pi * r ** 2
        print(s)
    elif x == 3:
        s = 0.5 * h * c
        print(s)
    elif x == 4:
        s = a * b
        print(s)
      
square(3, 0, 8, 4, 0, 0)
        




