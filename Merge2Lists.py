    # - Take two lists as input.
    # - If either list is empty, stop the process since there’s nothing meaningful to merge.
    # - Next, combine both lists into a single list. To sort this combined list, follow these steps:
        # - 1. Begin at the start of the list with the first element.
        # - 2. Compare each element with the one immediately after it.
        # - 3. If the current value is greater than its neighbor, swap them.
        # - 4. Continue this process, moving through the list until you reach the end.
        # - 5. Repeat the comparisons as needed until the list is fully ordered.
    # - Finally, print the merged and sorted list.

import sys

listInput1 = list(map(int, input("Enter a sorted list of numbers: ").split()))
listInput2 = list(map(int, input("Enter another sorted list of numbers: ").split()))

if listInput1 == []:
    sys.exit("Next Time Input The List")
if listInput2 == []:
    sys.exit("Next Time Input The List")
    
listInput1.extend(listInput2)
 
lengthOflistInput1 = len(listInput1)
for index in range(lengthOflistInput1):
    for nextIndex in range(0, lengthOflistInput1 - index - 1):
        if listInput1[nextIndex] > listInput1[nextIndex + 1]:
            listInput1[nextIndex], listInput1[nextIndex + 1] = listInput1[nextIndex + 1], listInput1[nextIndex]
    
print(f"Your new list is {listInput1}")

    # - Case #1: They are the same list.
    # - Input: [3, 6, 1, 4] & [3, 6, 1, 4]
    # - Output: [1, 1, 3, 3, 4, 4, 6, 6]

    # - Case #2: They are already sorted.
    # - Input: [1, 2, 3, 4, 5, 6] & [7, 8, 9, 10]
    # - Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]    

    # - Case #3: They aren't sorted.
    # - Input: [-1, 6, 3, 0] & [20, 101, 86, 7, 1]
    # - Output: [-1, 0, 1, 3, 6, 7, 20, 86, 101]

    # - Case #4: There is no list.
    # - Input: [] & [1, 0]
    # - Output: Next Time Input A List     

    # - Case #5: The list has non-number elements.
    # - Input: [str, bo, False] & [1.4, -1, i]
    # - Output: Error    

    # - Case #6: Every elements is the same.
    # - Input: [1, 1, 1] & [1, 1, 1, 1, 1]
    # - Output: [1, 1, 1, 1, 1, 1, 1, 1]    