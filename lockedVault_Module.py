def isPalindrome(str):
    if str[::-1] == str:
        return True
    else:
        return False

def getVowelCount(str):
    vowels = "aeiouyAEIOUY"
    count = 0
    for char in str:
        if char in vowels:
            count +=1
    return count

def reverseString(str):
    return str[::-1]

