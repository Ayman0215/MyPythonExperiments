#1
"""
student_name = "Zara"
student_age = 14
print(f"Hi, my name is {student_name} and I am {student_age} years old.")
"""

#2
"""
apple_count = 6
milk_price = 3.49
is_organic = True
grocery_store_name = "FreshMart"

print(type(apple_count))
print(type(milk_price))
print(type(is_organic))
print(type(grocery_store_name))
"""

#3
"""
favSport = input("What is your favorite sport: ")

print(f"You enjoy playing {favSport}!")
"""

#4
"""
gift_card = "10"
cash_on_hand = 20
total_cash = int(gift_card) + cash_on_hand
print(f"You got a $10 gift ard and already have $20. That means now you have ${total_cash} in total.")
"""

#5
"""
temperature_fahrenheit = 45
if temperature_fahrenheit <= 50:
    print(True)
else:
    print(False)
"""

#6
"""
age = int(input("What is your age: "))

if (age >= 13 ) and (age <= 19):
    print("You are a teenager")
else:
    print("You are not a teenager")
"""

#7
"""
movieAge = input("Are you at least 18 years old (Write either 'Yes' or 'No'): ")
idNeeded = input("Do you have a student ID (Write either 'Yes' or 'No'): ")

if (movieAge == "Yes") or (idNeeded == "Yes"):
    print("You are eligible for a ticket.")
else:
    print("Sorry, you aren't eligible.")
"""

#12
"""
age = 16
age_str = "16"
if age == age_str:
    print("True")
elif age != age_str:
    print("False")
else:
    print("Error")
"""

#1 : B

#2 : B

#3 : D

#4 : B

#5 : C

#6
"""
temps = [68, 72, 76, 81, 65, 90]

for i in temps:
        print(i)
"""

#7
"""
fact_num = int(input("Choose a number: "))
product = fact_num

while fact_num > 1:
    product = product * (fact_num - 1)
    fact_num -= 1
    print("Inside loop", fact_num, product)

print("Outside loop", product)
"""

#8
"""
for i in range(1,101):
    if (i % 3 == 0) and (i % 5 == 0) :
        print("FizzBuzz :", i)
    elif i % 5 == 0 :
        print("Buzz :", i)
    elif i % 3 == 0:
        print("Fizz :", i)
    else:
        print("Nothing but :", i)
"""

#9
"""
rows = 5

for i in range (1, rows + 1):
    print(" " * (rows - i), end="")
    print("*" * (2 * i - 1))
"""    

#6

"""
# Visit each number
#     - Check whether the number in the list is equals to the numberToFind
#     - If it is equals, says "Found Number" and stop here.
#     - If it is not equal, do nothing here.
"""
"""
import sys
nums = list(map(int, input("Enter list of nums (Don't use commas!): ").split()))  #nums = []
numberToFind = int(input("Input another value: "))  #numberToFind = 0

for num in nums:     # 
    if num == numberToFind:     #
        print(f"One of your list's nums is {numberToFind}!")     #
        sys.exit(0)

print(f"Didn't find {numberToFind}")    #

# Test cases
# Test case 1 - number in the list
#  10 2 3 41
#  3
# expected output: Found 3 in the list
# Program output: 
#    One of your list's nums is 3
# worked or failed !!
#
# Test case 2 - number is NOT in the list
# 1 2 3 4
# 5
# expected output: Didn't find 5 in the list
# Program output: Didn't find 5
#
# Test case 3 - Single element list
# 1
# 0
# expected output: Didn't find 0 in the list
# Program output: Didn't find 0
#
# Test case 4 - Empty list
# 
# 0
# expected output: Didn't find 0 in the list
# Program output:
#
#
"""

#7
"""
# - Visit each number in list
# - Divide each by two and find the remander
# - If the remander is 0 or 1 state the index and number

import sys

list_numbs = list(map(int, input("Enter list of nums (Don't use commas!): ").split()))    # ...

if list_numbs == [] or None:
    sys.exit(1)

index = 0

for nums in list_numbs:  # ...
    if nums % 2 == 0:   # ...
        print(f"One of your nums in the list, the number {nums} is even!")   # ...
        print(f"This number is at Index {index}!")  # ...
        index += 1

    elif nums % 2 == 1 or -1: # ...
        print(f"One of your nums in the list, the number {nums} is odd!")    # ...
        print(f"This number is at Index {index}!")  # ...
        index += 1
    
    else:
        print("Your number is a under the catergory of a COMPLEX NUMBER. You have escaped a VALUE-ERROR")   # ...
    break
    sys.exit()

# - Case #1: All nums are odd.

# Input : [1, -5, 3, -7]
# Output:
# Number of even nums: 0
# Number of odd nums: 4

# - Case #2: All nums are even.

# Input : [0, -4, -2, 6]
# Output : EVEN EVEN EVEN EVEN

# - Case #3: All nums are either even or odd.

# Input : [-1, 6,- 4, 7]
# Output : ODD EVEN EVEN ODD

# - Case #4: The inputted values are either a float or imaginary number. 

# Input : [1.4, -3, 8, 9i ]
# Output : TypeError or "You have escaped a VALUE-ERROR"

# Empty case:
# Expected: 
"""

#8
"""
# - Ask user for "how_many_people"
# - Find if it is greater, lesser, or equal to 8.
# - Calculate "sales_tax" from there

import sys

how_many_people = int(input("Hello! Welcome to our restaurant! How many seat do you need for how many people you have: "))
hmp = how_many_people # ...

if hmp <= 0:
    hmp =  int(input("Sorry! Try Again! How many seat do you need for how many people you have: "))

elif hmp < 8 :  # ...
    bill_amount = ((hmp * 10) + (hmp * 10 * 0.09))     # ...

elif hmp >= 8 :   # ...
    bill_amount_without_salestax = (hmp * 10)
    bill_amount_without_grayuity = bill_amount_without_salestax + (bill_amount_without_salestax * 0.09)
    bill_amount = (bill_amount_without_grayuity) + 0.15(bill_amount_without_grayuity)  # ...

else:  # When would we ever get here ??
    print("Your number is a under the catergory of a COMPLEX NUMBER. You have escaped a VALUE-ERROR")   # ...
    sys.exit()

print(f"Your meal will cost ${round(bill_amount, 2)}! I hope you enjoy!") # ...

# - Case #1: "hmp" is greater than 8.

# Input : 9
# Output : $112.82

# - Case #2: "hmp" is less than 8.

# Input : 3
# Output : $32.70

# - Case #3: "hmp" is less than 0.

# Input : -1
# Output : ValueErrpr/Try Again or "You have escaped a VALUE-ERROR"
"""

#4

# - It reads through the range of the list and sets the max_num to the current.

# - Next, it checks for the next "index" of the list 

# - ...

# - ...
"""
import sys

listInput = list(map(int, input("Enter list of nums (Don't use commas!): ").split()))   # - ...

if listInput == []: # - ...
    sys.exit(1)

listOutput = []

print(f"This is the list you inputted: {listInput}")    # - ...

for listIndex in range(len(listInput)):  # - ...
    max_num = listIndex  # - ...
    for index in range(listIndex + 1, len(listInput)):   # - ...
        if listInput[index] > listInput[max_num]:   # - ...
            max_num = index # - ...
    listInput[listIndex], listInput[max_num] = listInput[max_num], listInput[listIndex]   # - ...

listOutput.extend(listInput)  # - ...
print(f"This is your original array: {listInput}")
print(f"This is your sorted list: {listOutput}")
"""

# - Case #1: Normal Unsorted List

# Input: [0, -7, 10, 5]
# Output: [-7, 0, 5, 10]

# - Case #2: No List

# Input: []
# Output: sys.exit

# - Case #3: Already Sorted List

# Input: [1, 2, 3, 4, 5 , 6, 7]
# Output: [1, 2, 3, 4, 5 , 6, 7]

# define findListMaxBelowThreshold

listInput = numbers = list(map(int, input("Enter list of numbers: ").split()))

def findListMaxBelowThreshold(a_list, thresholdValue):
    for listIndex in range(len(listInput)):  # - ...
        max_num = listIndex  # - ...
    for index in range(listIndex + 1, len(listInput)):   # - ...
        if listInput[index] > listInput[max_num]:   # - ...
            max_num = index # - ...
    listInput[listIndex], listInput[max_num] = listInput[max_num], listInput[listIndex]
    ...
    ...

import sys

actualList = [7, 21, 0, -1, 4, 42]
list2 = []

max = sys.maxsize
for index in range(len(actualList)):
    threshold = max
    max = findListMaxBelowThreshold(actualList, threshold)
    list2.append(max)
