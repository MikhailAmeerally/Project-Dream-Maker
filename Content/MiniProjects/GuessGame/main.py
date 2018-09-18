import random

#Generating a random number from 1 to 10
secretNumber = random.randint(1,10)

userGuess = None

while userGuess != secretNumber:
    userGuess = input("Enter a number from 1 to 10: ")
    userGuess = int(userGuess)
    if userGuess > secretNumber:
        print("Too high")
    elif userGuess < secretNumber:
        print("Too low.")

if(userGuess == secretNumber):
    print("You win!")

'''
Solution for GuessGame
'''