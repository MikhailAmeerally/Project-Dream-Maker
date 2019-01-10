def add(x,y):
    sum = x + y
    return sum
def minus(x,y):
    difference = x - y
    return difference
def multiply(x,y):
    product = x * y
    return product
def divide(x,y):
    quotient = x / y
    return quotient
def calculator(num1, num2, operation):
    total = 0
    if operation == "x":
        total = multiply(num1,num2)
    elif operation == "+":
        total = add(num1,num2)
    elif operation == "-":
        total = minus(num1,num2)
    elif operation == "/":
        total = divide(num1,num2)
    return total
