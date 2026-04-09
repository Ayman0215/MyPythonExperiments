#-------------------------------------------------------------------------------------#
def caseChecker(string):
    isUpper = False
    isLower = False

    for char in string:
        if char.isupper():
            isUpper = True
        elif char.islower():
            isLower = True

        if isUpper and isLower:
            return "mixed case"

    if isUpper and not isLower:
        return "uppercase"
    elif not isUpper and isLower:
        return "lowercase"
    
    return "no letters"
#-------------------------------------------------------------------------------------#
str1 = str(input("Enter a string"))
caseChecker(str1)