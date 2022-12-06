a0 = 1
a1 = 1

def fib(n):
  for n in range (0, n, 1):
    print(f'iteration:{iter}')
    a2 = a0 + a1
    print(a2)
    a0 = a1
    a1 = a2
  
fib(5)
