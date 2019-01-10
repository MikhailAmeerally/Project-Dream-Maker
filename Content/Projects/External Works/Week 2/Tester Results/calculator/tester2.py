def add(x,y):
    total = x + y
    return total

def minus(x,y):
    total = x - y
    return total

def multiply(x,y):
    total = x * y
    return total

def divide(x,y):
    total = x / y
    return total

def sum_of_square(x,y):
    x = x * x
    y = y * y
    total = x + y
    return total

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

    elif operation == "+x":
        total = sum_of_squares(num1,num2)

    return total
