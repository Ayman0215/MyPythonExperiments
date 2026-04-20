#----------------------------------------------------------------#
def checkPalindrome(string1):
   left = 0
   right = len(string1) - 1

   while left < right:
       if string1[left] != string1[right]:
           print("Not Palindrome")
           return
       left += 1
       right -= 1

   print("Palindrome")
#----------------------------------------------------------------#
