#----------------------------------------------------------------#
import pytest
from printUpperStrings import printUpperStrings
#----------------------------------------------------------------#
@pytest.mark.parametrize(
   "input_list, expected_output",
   [
       (["A", "B"], "['A', 'B']\n"),
       (["hello", "world"], "['HELLO', 'WORLD']\n"),
       (["Ab", "cD"], "['AB', 'CD']\n"),
       ([], "[]\n"),
   ],
)
#----------------------------------------------------------------#
def test_print_upper_strings(capsys, input_list, expected_output):
   result = printUpperStrings(input_list)
   captured = capsys.readouterr()
   assert captured.out == expected_output
   assert result is None
#----------------------------------------------------------------#
