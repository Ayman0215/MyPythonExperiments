#----------------------------------------------------------------#
import pytest
from checkPalindrome import checkPalindrome
#----------------------------------------------------------------#
@pytest.mark.parametrize(
   "input_str, expected_output",
   [
       ("madam", "Palindrome\n"),
       ("racecar", "Palindrome\n"),
       ("hello", "Not Palindrome\n"),
       ("", "Palindrome\n"),
   ],
)
#----------------------------------------------------------------#
def test_check_palindrome(capsys, input_str, expected_output):
   result = checkPalindrome(input_str)
   captured = capsys.readouterr()
   assert captured.out.strip() == expected_output.strip()
   assert result is None
#----------------------------------------------------------------#
