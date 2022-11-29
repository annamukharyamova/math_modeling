import numpy as np
a = np.arange(10)
print(a)

def my_func(a):
    c = 0
    for i in a:
        c = i + c
    
    b = c / len(a)
    print(b)

my_func(a)