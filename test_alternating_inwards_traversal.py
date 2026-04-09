#----------------------------------------------------------------#
import pytest
from alternating_inwards_traversal import alternatingInwardsTraversalNumbers
#----------------------------------------------------------------#
@pytest.mark.parametrize(
    "input_list, expected_output",
    [
        ([1, 2, 3, 4, 5], "1\n5\n2\n4\n3\n"),
        ([], ""),
        ([1], "1\n"),
        ([1, 2], "1\n2\n"),
        ([1, 2, 3], "1\n3\n2\n"),
    ],
)
#----------------------------------------------------------------#
def test_alternating_inwards(capsys, input_list, expected_output):
    result = alternatingInwardsTraversalNumbers(input_list)
    captured = capsys.readouterr()
    assert captured.out.strip() == expected_output.strip()
    assert result is None
#----------------------------------------------------------------#