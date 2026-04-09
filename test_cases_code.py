#-------------------------------------------------------------------------------------#
import pytest
from cases_code import caseChecker
#-------------------------------------------------------------------------------------#
@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("APPLE", "uppercase"),
        ("apple", "lowercase"),
        ("Apple", "mixed case"),
        ("aPPle", "mixed case"),
        ("", "no letters"),
        ("123", "no letters"),
    ],
)
#-------------------------------------------------------------------------------------#
def test_case_checker(input_str, expected):
    assert caseChecker(input_str) == expected
#-------------------------------------------------------------------------------------#