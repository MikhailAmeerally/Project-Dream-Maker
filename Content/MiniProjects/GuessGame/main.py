import random
from functions import *
#Generating a random number from 1 to 10
secret_number = random.randint(1,10)

user_guess = None
keep_guessing = True

while keep_guessing:
    user_guess = input("Enter a number from 1 to 10: ")

    help_or_exit = parse_user_guess(user_guess)

    print(help_or_exit)
    if(help_or_exit):
        continue

    user_guess = int(user_guess)
    state = guess_number(user_guess,secret_number)
    keep_guessing,response = not state[0], state[1]

    print(response)


print("You win!")

'''
Solution for GuessGame
'''