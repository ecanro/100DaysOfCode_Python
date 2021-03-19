def add(n1, n2):
    return n1 +n2

def substract(n1, n2):
    return n1 -n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1/n2

#higher order function
def calculator(n1, n2, func):
    return func(n1, n2)

print(calculator(5, 2, divide))