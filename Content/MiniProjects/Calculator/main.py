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
        a = ""
        b = ""
        operator = None
        aFlag = True
        for i in phrase:
            if i not in ["+", "-", "*", "/"]:
                if aFlag:
                    a = a + i
                    print(a)
                else:
                    b = b + i
                    print(b)
            else:
                if not operator:
                    operator = i
                    a = int(a.strip())
                    aFlag = False
                else:
                    b = b + i
        b = int(b.strip())
        a = evaluate(a, b, operator)
        print(a)