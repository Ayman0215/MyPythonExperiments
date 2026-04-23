#----------------------------------------------------------------#
def toUpperCase(string1):
   result = ""
   for i in string1:
       result += i.upper()
   print(result)
#----------------------------------------------------------------#
str1 = str(input("Put a string : "))
toUpperCase(str1)