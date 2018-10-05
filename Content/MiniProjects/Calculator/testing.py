import unittest
from functions import *


class TestAddition(unittest.TestCase):

    def test_add_zero(self):
        self.assertEqual(add(1, 0), 1, "1 + 0")
        self.assertEqual(add(15, 0), 15, "15 + 0")

    def test_add_single_digits(self):
        self.assertEqual(add(1, 1), 2, "1 + 1")
        self.assertEqual(add(9,1), 10, "9 + 1")

    def test_add_more_than_one_digit(self):
        self.assertEqual(add(10,10), 20, "10 + 10")
        self.assertEqual(add(10, 11), 21, "10 + 11")
        self.assertEqual(add(10, 1), 11, "10 + 1")
        self.assertEqual(add(100, 1), 101, "100 + 1")
        self.assertEqual(add(100, 10), 110, "100 + 10")
        self.assertEqual(add(100,200), 300, "100 + 200")
        self.assertEqual(add(100, 123), 223, "100 + 123")

    def test_add_negatives(self):
        self.assertEqual(add(5,-1), 4, "5 + -1")
        self.assertEqual(add(-5, 10), 5, "-5 + 10")
        self.assertEqual(add(-5, -5), -10, "-5 + -5")
        self.assertEqual(add(-50, -5), -55, "-50 + -5")
        self.assertEqual(add(-50,-50), -100, "-50 + -50")


class TestSubtraction(unittest.TestCase):

    def test_minus_zero(self):
        self.assertEqual(subtract(1, 0), 1, "1 - 0")
        self.assertEqual(subtract(15, 0), 15, "15 - 0")

    def test_minus_single_digits(self):
        self.assertEqual(subtract(1, 1), 0, "1 - 1")
        self.assertEqual(subtract(11, 1), 10, "11 - 1")

    def test_minus_more_than_one_digit(self):
        self.assertEqual(subtract(20, 10), 10, "20 - 10")
        self.assertEqual(subtract(20, 11), 9, "20 - 11")
        self.assertEqual(subtract(10, 1), 9, "10 - 1")
        self.assertEqual(subtract(100, 1), 99, "100 - 1")
        self.assertEqual(subtract(120, 10), 110, "120 - 10")
        self.assertEqual(subtract(200, 50), 150, "200 - 150")
        self.assertEqual(subtract(3000, 123), 2877, "3000 - 123")

    def test_minus_negatives(self):
        self.assertEqual(subtract(5,-1), 6, "5 - -1")
        self.assertEqual(subtract(-5, 10), -15, "-5 - 10")
        self.assertEqual(subtract(-5, -5), 0, "-5 - -5")
        self.assertEqual(subtract(-50, -5), -45, "-50 + -5")
        self.assertEqual(subtract(-50,50), -100, "-50 -50")