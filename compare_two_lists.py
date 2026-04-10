#----------------------------------------------------------------#
def compareTwoLists(listA, listB):

    lenA = len(listA)
    if lenA != len(listB):
        return False
    index = 0
    while index < lenA:

    if len(listA) != len(listB):
        return False
    index = 0
    while index < len(listA):
        if listA[index] != listB[index]:
            return False
        index += 1
    return True

#----------------------------------------------------------------#
lstA = list(map(int, input("Enter list of numbers: ").split()))
lstB = list(map(int, input("Enter list of numbers: ").split()))
compareTwoLists(lstA, lstB)
#----------------------------------------------------------------#
