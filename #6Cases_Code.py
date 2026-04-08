#-------------------------------------------------------------------------------------#
import unittest
#-------------------------------------------------------------------------------------#
def caseChecker(string):
    isUpper = False
    isLower = False
    for char in string:
        if char.isupper():
            isUpper = True
        elif char.islower():
            isLower = True
        if isUpper == True and isLower == True:
            return "mixed case"
    if isUpper == True and isLower != True:
        return "uppercase"
    elif isUpper != True and isLower == True:
        return "lowercase"
#-------------------------------------------------------------------------------------#
class AnagramCode(unittest.TestCase):
    def test_AllUppercase(self):
        self.assertEqual(caseChecker("APPLE"), "uppercase")
    
    def test_AllLowercase(self):
        self.assertEqual(caseChecker("apple"), "lowercase")
    
    def test_MixedCase(self):
        self.assertEqual(caseChecker("Apple"), "mixed case")
#-------------------------------------------------------------------------------------#
if __name__ == "__main__":
    unittest.main()
#-------------------------------------------------------------------------------------#