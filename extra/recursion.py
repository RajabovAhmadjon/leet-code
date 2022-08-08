"""
Recursion Functions
1) hello
2) hello n times
3) Sum 1+2+3+4+5 = 15
4) Factorial 5! = 1*2*3*4*5 = 120
5) Fibonacci 0,1,1,2,3,5,8,13,21,34,55
"""

# def hello(x):
#     if x == 0:
#         return
#     else:
#         print("Hello World!")
#         hello(x - 1)
# hello(3)

# def sum(y):
#     if y == 0:
#         return 0
#     elif y == 1:
#         return 1
#     else:
#         return y + sum(y - 1)
# print(sum(10))

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)
# print(factorial(5))

def fibonacci(m):
    if m == 0:
        return 0
    elif m == 1:
        return 1
    else:
        return fibonacci(m - 1) + fibonacci (m - 2)
print(fibonacci(10))