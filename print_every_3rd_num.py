#----------------------------------------------------------------#
def printEveryThird(nums):
    for i in range(0, len(nums), 3):
        print(nums[i])

#----------------------------------------------------------------#
listOfNums = list(map(int, input("Enter list of numbers: ").split()))
printEveryThird(listOfNums)
#----------------------------------------------------------------#
