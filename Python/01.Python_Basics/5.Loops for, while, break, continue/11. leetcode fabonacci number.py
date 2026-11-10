"""

#509 Fibonacci Number. 

“The Fibonacci numbers form a sequence where each number is the sum of the two before it, starting from 0 and 1. Given n, return the n-th Fibonacci number.”

The sequence: 0, 1, 1, 2, 3, 5, 8, 13, ...

n = 2 → 1
n = 3 → 2
n = 4 → 3

"""

    
def fib(n):
    a = 0                  # F(0)
    b = 1                  # F(1)
    for _ in range(n):     # slide the pair n times
        temp = a + b
        a = b
        b = temp
    return a               # after n slides, a holds F(n)


assert fib(0) == 0
assert fib(1) == 1
assert fib(4) == 3
assert fib(9) == 34
