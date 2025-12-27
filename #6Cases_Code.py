#-------------------------------------------------------------------------------------#
import unittest
#-------------------------------------------------------------------------------------#
alphabet = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
#-------------------------------------------------------------------------------------#
def has(chars, string):
    for char in chars:
        if char in string:
            return True
    return False

def letterChecker(string1, alphabet):
    return has(alphabet, string1)

def caseChecker(string1, Found):
    if Found:
        if string1 == string1.upper():
            return "Uppercase"
        elif string1 == string1.lower():
            return "Lowercase"
        else:
            return "Mixed Case"
    else:
        return "Special Case"
#-------------------------------------------------------------------------------------#
class AnagramCode(unittest.TestCase):

    def test_all_uppercase(self):
        result = caseChecker("HELLO", letterChecker("HELLO", alphabet))
        self.assertEqual(result, "Uppercase")

    def test_all_lowercase(self):
        result = caseChecker("hello", letterChecker("hello", alphabet))
        self.assertEqual(result, "Lowercase")

    def test_mixed_case(self):
        result = caseChecker("HeLLo", letterChecker("HeLLo", alphabet))
        self.assertEqual(result, "Mixed Case")

    def test_all_punctuation(self):
        result = caseChecker("!!?@ /...^", letterChecker("!!?@ /...^", alphabet))
        self.assertEqual(result, "Special Case")

    def test_empty_string(self):
        result = caseChecker("", letterChecker("", alphabet))
        self.assertEqual(result, "Special Case")
#-------------------------------------------------------------------------------------#
if __name__ == "__main__":
    unittest.main()
#-------------------------------------------------------------------------------------#