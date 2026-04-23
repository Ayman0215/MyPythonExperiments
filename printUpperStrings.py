#----------------------------------------------------------------#
def printUpperStrings(list1):
    for i in range(len(list1)):
        result = ""
        for j in range(len(list1[i])):
            result += list1[i][j].upper()
        list1[i] = result
    print(list1)
#----------------------------------------------------------------#
lst1 = list(map(str, input("Enter list of strings: ").split()))
printUpperStrings(lst1)