import unittest
from functions import *

class GuessGameTests(unittest.TestCase):

    def test_too_high_or_too_low(self):
        self.assertEqual(too_high_or_too_low(5, 7), "Too Low", "Secret Number is 7, Your Guess: 5")
        self.assertEqual(too_high_or_too_low(5,4), "Too High", "Secret Number is 4, Your Guess: 5")

    def test_guess_number(self):
        self.assertEqual(guess_number(5, 7), [False, "Too Low"], "Secret Number is 7, Your Guess: 5")
        self.assertEqual(guess_number(5, 4), [False, "Too High"], "Secret Number is 4, Your Guess: 5")
        self.assertEqual(guess_number(5, 5), [True, "Correct"], "Secret Number is 5, Your Guess: 5")

    def test_parse_user_input(self):
        self.assertEqual(parse_user_guess("5"), False, "Entered a 5.")
        self.assertEqual(parse_user_guess("help"),True, "Entered 'help' call help()")
        with self.assertRaises(SystemExit):
            parse_user_guess('exit')
