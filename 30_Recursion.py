                                #Recursion
# 5 * 4 * 3 * 2 * 1
'''
Recursion is the process of defining something in terms of itself.
'''

def factorial(n):
    if n == 0 or n==1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(7))

# Quick Quiz: Write a program to print the Fibonacci sequence
# f(0) = 0
# f(1) = 1
# f(2) = f(1) + f(0)
# f(n) = f(n-1) + f(n-2)

# 0 1 1 2 3 5 8....
def fibonacci(f):
    if f == 0 or f == 1:
        return 1
    else:
        return fibonacci(f-1) + fibonacci(f-2)

print(fibonacci(12))