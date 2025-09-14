import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def power(x, y):
    return pow(x, y)

def factorial(x):
    if x == 0:
        return 1
    else:
        return  x * factorial(x - 1)

def squareroot(x):
    return math.sqrt(x)