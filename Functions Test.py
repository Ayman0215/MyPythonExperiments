import sys
    
'''
import sys

def calculate_discount(price, discount):
    discount = discount/100
    if discount > 1:
        sys.exit()
    else:
        sale = price - (price * discount)
        return(f"Here is your final price: {sale}")

print(calculate_discount(100, 30))
'''



#1

"""

# - Create a "maxi" function, called at the end of the "findListMaxBelowThreshold", to return the max below threshold, by finding & storing the "value"s inputted. 

def maxi(value):    # - ...
    
    if len(value) == 0: # - ...
        sys.exit()
    max = value[0]  # - ...
    
    for item in range(1, len(value)):   # - ...
        if value[item] > max:
            max = value[item]   # - ...
    return max

# - Create a "findListMaxBelowThreshold" function by using the "maxi" function, 
#    repeating an "if" statement for the element in the list, that is less than the threshold value.
# - Create a "givenList" and "givenThreshold" that take the user input and 
#    use the "findListMaxBelowThreshold" on them.

# Inputs: list, threshold below which we want the max
# Outputs: maximum number below the threshold in the given list
# how
#     - Create a new lsit called belowThreshold - contains all number below threshold
#     - maxi to find max in belowThreshold

def findListMaxBelowThreshold(list, threshold): # - ...
    
    #if list == [] or None:
    #    sys.exit("No list provided!")
    #if threshold == None:
    #    sys.exit("No value provided!")
                            
    # - Checks if the num is below threshold and assigns it to the variable.
    belowThreshold = [  # - ...
        num for num in list     # - ...
        if num < threshold  # - ...
        ]
    
    if not belowThreshold:  # - ...
        return None
    if belowThreshold == None:  # - ...
        return "No value below threshold."

    return maxi(belowThreshold)  # - ...

givenList = list(map(int, input("Enter list of numbers: ").split()))
givenThreshold = int(input("Give a threshold value: "))

print(f"Here is your max below the threshold: {findListMaxBelowThreshold(givenList, givenThreshold)}")

# - Case #1:

# - Input: [1 2 3 4 5] , 4
# - Output: 3

# - Case #2:

# - Input: [1 2 3 4 5] , 1
# - Output: No value below threshold

# - Case #3:

# - Input: []
# - Output: No list provided

"""

#2

# Inputs: list, threshold below which we want the max
# Outputs: maximum number below the threshold in the given list
# how
#     - Create a new lsit called belowThreshold - contains all number below threshold
#     - maxi to find max in belowThreshold

def findListMaxBelowThresholdV3(threshold_2):    # - ...
    
    values = list(map(int, input("Enter list of numbers: ").split()))

    if len(values) == 0: # - ...
        sys.exit()

    max = values[0] 
    for num in values:
        if num < threshold_2:
            if num > max:
                max = num
     
    return max

givenThreshold = int(input("Give a threshold value: "))

print(f"Here is your max below the threshold: {findListMaxBelowThresholdV3(givenThreshold)}")

#3

# - ...
# - ...