def add(x,y):
    return x + y

def minus(x,y):
    return x - y
    
def multiply(x,y):
    return x * y

def divide(x,y):
    return round(x / y,2)

def square_root(x):
    return round(x ** 0.5,2)

def x_raised_to_y(x,y):
    return x ** y

def calculator(num1, num2=0, operation):
    total = 0
    
    if operation == "x":
        return multiply(num1,num2)
        
    elif operation == "+":
        return add(num1,num2)

    elif operation == "-":
        return minus(num1,num2)

    elif operation == "/":
        return divide(num1,num2)

    elif operation == "_/":
        return square_root(num1)
    
    elif operation == "^":
        return x_raised_to_y(num1,num2)

    else:
        return 0
