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