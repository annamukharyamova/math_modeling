import numpy as np
a = np.arange(10)
print(a)

def my_func(a):
    b = np.sum(a) / len(a)
    print(b)

my_func(a)