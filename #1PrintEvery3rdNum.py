#----------------------------------------------------------------#
import unittest
#----------------------------------------------------------------#
def printEveryThird(nums):
    for i in range(0, len(nums), 3):
        print(nums[i])
    return None
#----------------------------------------------------------------#
class TestPrintEveryThird(unittest.TestCase):
    def test_NormalList(self):
        self.assertIsNone(printEveryThird([1, 2, 3, 4, 5, 6])) # 1, 4

    def test_NoList(self):
        self.assertIsNone(printEveryThird([])) # 

    def test_OneIndexList(self):
        self.assertIsNone(printEveryThird([1])) # 1

    def test_TwoIndexList(self):
        self.assertIsNone(printEveryThird([1, 2])) # 1 

    def test_ThreeIndexList(self):
        self.assertIsNone(printEveryThird([1, 2, 3])) # 1 

    def test_ReverseList(self):
        self.assertIsNone(printEveryThird([6, 5, 4, 3, 2, 1])) # 6, 3
#----------------------------------------------------------------#
if __name__ == "__main__":
    unittest.main()
#----------------------------------------------------------------#