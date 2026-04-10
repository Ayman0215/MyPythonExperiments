#----------------------------------------------------------------#
import pytest
from compare_two_lists import compareTwoLists
#----------------------------------------------------------------#
@pytest.mark.parametrize(
    "listA, listB, expected",
    [
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], True),
        ([1, 2, 3, 4], [1, 2, 3, 4, 5], False),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 6], False),
        ([], [], True),
    ],
)
#----------------------------------------------------------------#
def test_compare_two_lists(listA, listB, expected):
    result = compareTwoLists(listA, listB)
    assert result == expected
#----------------------------------------------------------------#