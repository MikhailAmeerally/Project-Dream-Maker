from functions import evaluate

print("This calculator only uses + - * /")
print("You are more than welcomed to make it more advanced.")
print("For help, type 'help'")

while(True):
    phrase = input("Enter phrase: ")
    if phrase.strip() == "help":
        printHelp()
    elif phrase == "exit":
        break
    else:
        phrase = phrase.strip().split()
        a = None
        b = None
        operator = None
        aFlag = True
        for i in phrase:
            if i not in ['+', '-', '*', '/']:
                if aFlag:
                    a = int(i)
                    aFlag = False
                else:
                    b = int(i)
                    a = evaluate(a, b, operator)
            else:
                operator = i
        print(a)