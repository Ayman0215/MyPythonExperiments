#----------------------------------------------------------------#
import pytest
from print_every_3rd_num import printEveryThird
#----------------------------------------------------------------#
@pytest.mark.parametrize(
    "input_list, expected_output",
    [
        ([1, 2, 3, 4, 5, 6], "1\n4\n"),
        ([], ""),
        ([1], "1\n"),
        ([1, 2], "1\n"),
        ([1, 2, 3], "1\n"),
        ([6, 5, 4, 3, 2, 1], "6\n3\n"),
    ],
)
#----------------------------------------------------------------#
def test_print_every_third(capsys, input_list, expected_output):
    result = printEveryThird(input_list)
    captured = capsys.readouterr()
    assert captured.out == expected_output
    assert result is None
#----------------------------------------------------------------#