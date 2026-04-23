#----------------------------------------------------------------#
import pytest
from toUpperCase import toUpperCase
#----------------------------------------------------------------#
@pytest.mark.parametrize(
   "input_str, expected_output",
   [
       ("abc", "ABC\n"),
       ("AbC", "ABC\n"),
       ("123", "123\n"),
       ("", "\n"),
   ],
)
#----------------------------------------------------------------#
def test_to_uppercase(capsys, input_str, expected_output):
   result = toUpperCase(input_str)
   captured = capsys.readouterr()
   assert captured.out == expected_output
   assert result is None
#----------------------------------------------------------------#
