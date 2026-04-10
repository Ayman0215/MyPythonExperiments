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
#----------------------------------------------------------------#
listOfNums = list(map(int, input("Enter list of numbers: ").split()))
alternatingInwardsTraversalNumbers(listOfNums)

