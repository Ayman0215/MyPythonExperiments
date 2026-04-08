#----------------------------------------------------------------#
import unittest
#----------------------------------------------------------------#
def alternatingInwardsTraversalNumbers(nums):
    left = 0
    right = len(nums) - 1
    while left <= right:
        print(nums[left])
        left +=1
        if left < right:
            print(nums[right])
            right -= 1
    return None
#----------------------------------------------------------------#
class TestAlternatingInwardsTraversalNumbers(unittest.TestCase):
    def test_NormalList(self):
        self.assertIsNone(alternatingInwardsTraversalNumbers([1, 2, 3, 4, 5])) # 1, 5, 2, 4, 3

    def test_NoList(self):
        self.assertIsNone(alternatingInwardsTraversalNumbers([])) #

    def test_OneIndexList(self):
        self.assertIsNone(alternatingInwardsTraversalNumbers([1])) # 1

    def test_TwoIndexList(self):
        self.assertIsNone(alternatingInwardsTraversalNumbers([1, 2])) # 1, 2

    def test_3IndexList(self):
        self.assertIsNone(alternatingInwardsTraversalNumbers([1, 2, 3])) # 1, 3, 2
#----------------------------------------------------------------#
if __name__ == "__main__":
    unittest.main()
#----------------------------------------------------------------#
