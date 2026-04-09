#----------------------------------------------------------------#
def reverseList(nums):
    index = len(nums) - 1
    while index >=0:
        print(nums[index])
        index -=2
#----------------------------------------------------------------#
listOfNums = list(map(int, input("Enter list of numbers: ").split()))
reverseList(listOfNums)