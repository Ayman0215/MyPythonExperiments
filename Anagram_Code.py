#-------------------------------------------------------------------------------------#
import unittest
import sys
#-------------------------------------------------------------------------------------#
def removeEachCharacterFromWord(val, string2):
    #
    for i in range(len(string2)):
        if string2[i] == val:
            string2 = string2[:i] + string2[i + 1:]
            return True, string2
    #
    return False, string2
    #
#-------------------------------------------------------------------------------------#
def isAnagram(string1, string2):
    #
    string1 = string1.lower()
    string2 = string2.lower()
    #
    if len(string1) != len(string2):
        return False
    #
    for val in string1:
        found, string2 = removeEachCharacterFromWord(val, string2)
        if found == False:
            return False
    return True
    #
#-------------------------------------------------------------------------------------#
class AnagramCode(unittest.TestCase):
    #
    def test_same_string(self):
        result = isAnagram("aab", "aba")
        self.assertEqual(result, True)
    #
    def test_same_string_capitalized(self):
        result = isAnagram("STRing", "strING")
        self.assertEqual(result, True)
    #
    def test_same_string_with_double_letters(self):
        result = isAnagram("strring", "striing")
        self.assertEqual(result, False)
    #
    def test_same_string_backwards(self):
        result = isAnagram("string", "gnirts")
        self.assertEqual(result, True)
    #    
    def test_same_string_different_length(self):
        result = isAnagram("string", "string ")
        self.assertEqual(result, False)
    #
    def test_standard_anagrams(self):
        result = isAnagram("string", "snigrt")
        self.assertEqual(result, True)
    #    
    def test_same_string_punctuation(self):
        result = isAnagram("string!", "string?")
        self.assertEqual(result, False)
    #
#-------------------------------------------------------------------------------------#
if __name__ == '__main__':
    unittest.main()
else:
    sys.exit() 
#-------------------------------------------------------------------------------------#