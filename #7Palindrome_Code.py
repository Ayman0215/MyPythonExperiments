<<<<<<< Updated upstream
#----------------------------------------------------------------#
import unittest
#----------------------------------------------------------------#
def is_palindrome(string1):
    
    if string1 == "":
        return False

    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    has_letter = False

    for char in string1:
        if char in letters:
            has_letter = True

    if not has_letter:
        return False

    if string1 == string1[::-1]:
        return True
    else:
        return False
#----------------------------------------------------------------#
class AnagramCode(unittest.TestCase):

    def test_palindromeWithLetters(self):
        self.assertEqual(is_palindrome("racecar"), True)

    def test_notPalindromeWithLetters(self):
        self.assertEqual(is_palindrome("apple"), False)

    def test_palindromeWithPunctuation(self):
        self.assertEqual(is_palindrome("!.??.!"), False)

    def test_notPalindromeWithPunctuation(self):
        self.assertEqual(is_palindrome("/@\\?"), False)

    def test_emptyString(self):
        self.assertEqual(is_palindrome(""), False)
#----------------------------------------------------------------#
if __name__ == "__main__":
    unittest.main()
=======
#----------------------------------------------------------------#
import unittest
#----------------------------------------------------------------#
def is_palindrome(string1):

    if string1 == string1[::-1]:
        return True
    else:
        return False
#----------------------------------------------------------------#
class AnagramCode(unittest.TestCase):

    def test_palindromeWithLetters(self):
        self.assertEqual(is_palindrome("racecar"), True)

    def test_notPalindromeWithLetters(self):
        self.assertEqual(is_palindrome("apple"), False)

    def test_palindromeWithPunctuation(self):
        self.assertEqual(is_palindrome("!.??.!"), True)

    def test_notPalindromeWithPunctuation(self):
        self.assertEqual(is_palindrome("/@\\?"), False)

    def test_emptyString(self):
        self.assertEqual(is_palindrome(""), True)
#----------------------------------------------------------------#
if __name__ == "__main__":
    unittest.main()
>>>>>>> Stashed changes
#----------------------------------------------------------------#