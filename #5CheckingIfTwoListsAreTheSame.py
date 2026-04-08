#----------------------------------------------------------------#
import unittest
#----------------------------------------------------------------#
def compareTwoLists(listA, listB):
    if len(listA) != len(listB):
        return False
    index = 0
    while index < len(listA):
        if listA[index] != listB[index]:
            return False
        index += 1
    return True
#----------------------------------------------------------------#
class TestCompareTwoLists(unittest.TestCase):
    def test_NormalLists(self):
        self.assertEqual(compareTwoLists([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]), True)

    def test_NotSameIndexesLists(self):
        self.assertEqual(compareTwoLists([1, 2, 3, 4], [1, 2, 3, 4, 5]), False)

    def test_NotSameElementsLists(self):
        self.assertEqual(compareTwoLists([1, 2, 3, 4, 5], [1, 2, 3, 4, 6]), False)

    def test_NoLists(self):
        self.assertEqual(compareTwoLists([], []), True)
#----------------------------------------------------------------#
if __name__ == "__main__":
    unittest.main()
#----------------------------------------------------------------#