import numpy as np

def add(a, b):
    return a + b


def substract(a, b):
    return a - b


def multiply(a, b):
    """This is a function that really does a multiplication of two numbers a ad b and returns the results"""
    return a * b


print(add(10, 5))

def  mean(numbers):
    return np.mean(numbers)

numbers = [1,2,3]

print(mean(numbers))
