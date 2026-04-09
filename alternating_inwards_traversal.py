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