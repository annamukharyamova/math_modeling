import numpy as np
a = np.arange(11)
print(a)

def my_func(a):
    c = 1
    for i in a:
        c = i * c
        print(c)

my_func(a)