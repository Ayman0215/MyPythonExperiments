#----------------------------------------------------------------#
import pytest
from print_stuff_in_reverse import reverseList
#----------------------------------------------------------------#
@pytest.mark.parametrize(
    "input_list, expected_output",
    [
        ([1, 2, 3, 4, 5], "5\n4\n3\n2\n1\n"),
        ([], ""),
        ([1], "1\n"),
        ([1, 1, 1, 1, 1], "1\n1\n1\n1\n1\n"),
    ],
)
#----------------------------------------------------------------#
def test_reverse_list(capsys, input_list, expected_output):
    result = reverseList(input_list)
    captured = capsys.readouterr()
    assert captured.out.strip() == expected_output.strip()
    assert result is None
#----------------------------------------------------------------#