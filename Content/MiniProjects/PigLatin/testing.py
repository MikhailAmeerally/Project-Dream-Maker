import unittest
from PigLatin import *

class TestPigLatin(unittest.TestCase):

    def test_pig_latin_vowel_start(self):
        self.assertEqual(pigLatinVowel("enter"), "enterway")
        self.assertEqual(pigLatinVowel("array"), "arrayway")
        self.assertEqual(pigLatinVowel("igloo"), "iglooway")
        self.assertEqual(pigLatinVowel("undone"), "undoneway")
        self.assertEqual(pigLatinVowel("on"), "onway")

    def test_pig_latin_cluster(self):
        self.assertEqual(pigLatinCluster("cheese"), "eesechay")
        self.assertEqual(pigLatinCluster("knicks"), "icksknay")
        self.assertEqual(pigLatinCluster("stupid"), "upidstay")

    def test_pig_latin_regular_words(self):
        self.assertEqual(convertWord("hello"), "ellohay")
        self.assertEqual(convertWord("mouse"), "ousemay")

    def test_convert_phrase(self):
        self.assertEqual(convertToPigLatin("Knicks on the stupid"), "icksknay onway ethay upidstay")
        self.assertEqual(convertToPigLatin("computer science"), "omputercay iencescay")