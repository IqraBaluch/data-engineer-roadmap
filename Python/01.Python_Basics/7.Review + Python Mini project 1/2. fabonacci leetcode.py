"""
Write a function that returns the n-th Fibonacci number. 
 The sequence starts 0, 1, 1, 2, 3, 5, 8. So fib(0) is 0, fib(1) is 1, and fib(6) is 8.


a = 0



"""

def fabonacci(n):
    a = 0
    b = 1

    for i in range(n):
        temp = a +b
        a = b
        b = temp
    return a
print(fabonacci(2))