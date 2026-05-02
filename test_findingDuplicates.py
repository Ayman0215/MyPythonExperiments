#----------------------------------------------------------------#
import pytest
from findingDuplicates import printDuplicates
#----------------------------------------------------------------#
@pytest.mark.parametrize(
    "input_list, expected_output",
    [
        ([1,2,3,2,1], "1\n2\n"),
        ([5,5,5], "5\n"),
        ([1,2,3], ""),
    ],
)
#----------------------------------------------------------------#
def test_print_duplicates(capsys, input_list, expected_output):
    result = printDuplicates(input_list)
    captured = capsys.readouterr()
    assert set(captured.out.strip().split()) == set(expected_output.strip().split())
    assert result is None
#----------------------------------------------------------------#