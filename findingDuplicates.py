#----------------------------------------------------------------#
def printDuplicates(list1):
    for i in range(len(list1)):
        for j in range(i + 1, len(list1)):
            if list1[i] == list1[j]:
                seen = False
                for k in range(i):
                    if list1[k] == list1[i]:
                        seen = True
                        break
                if not seen:
                    print(list1[i])
                break
#----------------------------------------------------------------#
lst1 = list(map(int, input("Enter list of numbers: ").split()))
printDuplicates(lst1)