#----------------------------------------------------------------#
def printUpperStrings(list1):
    print(list(map(str.upper, list1)))
#----------------------------------------------------------------#
lst1 = list(map(str, input("Enter list of strings: ").split()))
printUpperStrings(lst1)