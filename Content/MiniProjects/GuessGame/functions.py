def help():
    print('''Guess Game \n
            Goal is to guess a number between 1 and 10.
            If you need to exit the game early, enter "exit".
            Game does not support decimal inputs, and does not
            do error checking.''')

def guess_number(user_number, secret_number):
    return [True, "Correct"] if user_number == secret_number else [False, too_high_or_too_low(user_number,secret_number)]



def too_high_or_too_low(user_number, secret_number):
    return "Too High" if user_number > secret_number else "Too Low"

def parse_user_guess(user_guess):
    if(user_guess == "help"):
        help()
        return True
    elif user_guess == "exit":
        exit()

    return False