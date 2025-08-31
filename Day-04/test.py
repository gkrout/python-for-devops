import sys

def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b

a = float(sys.argv[1])
b = float(sys.argv[3])
operator = sys.argv[2]

if operator == 'add':
    print(f"The sum of {a} and {b} is {add(a, b)}")
elif operator == 'subtract':
    print(f"The difference of {a} and {b} is {subtract(a, b)}") 
elif operator == 'multiply':
    print(f"The product of {a} and {b} is {multiply(a, b)}")
