def printHelp():
    print("Example phrase: 3 + 23")
    print("Example phrase: 45 * 234")
    print("Rules need to be followed.")


def add(a,b):
    return a + b


def subtract(a,b):
    return a-b


def divide(a,b):
    return "undefined" if b == 0 else a // b #Use integer division


def  multiply(a,b):
    return a * b


def evaluate(a, b, operator):
    if operator == "+":
        return add(a,b)
    if operator == "-":
        return subtract(a,b)
    if operator == "*":
        return multiply(a,b)
    if operator == "/":
        return divide(a,b)