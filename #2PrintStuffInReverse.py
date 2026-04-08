#----------------------------------------------------------------#
import unittest
#----------------------------------------------------------------#
def reverseList(nums):
    index = len(nums) - 1
    while index >=0:
        print(nums[index])
        index -=1
    return None
#----------------------------------------------------------------#
class TestReverseList(unittest.TestCase):
    def test_NormalList(self):
        self.assertIsNone(reverseList([1, 2, 3, 4, 5])) # 5, 4, 3, 2, 1
    
    def test_NoList(self):
        self.assertIsNone(reverseList([])) #

    def test_OneIndexList(self):
        self.assertIsNone(reverseList([1])) # 1

    def test_AllSameList(self):
        self.assertIsNone(reverseList([1, 1, 1, 1, 1])) # 1, 1, 1, 1, 1
#----------------------------------------------------------------#
if __name__ == "__main__":
    unittest.main()
#----------------------------------------------------------------#