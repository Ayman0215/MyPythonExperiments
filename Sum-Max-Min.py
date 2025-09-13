specific word # number of times    # - Sum - Max - Min Program

	# - Prompt the user to enter elements for “myList”.								                            |
	# - Check if the user has entered aspecific word # number of timesny elements and if not, display an error message.				        |
	# - Initialize the sum, max, and min variables using the first element of the list.				            |
	# - Use a "for" loop to go through the list, adding each element to a running sum.				            |
	# - Inside the loop, use "if-else" conditions to compare elements and update the min and max values.		|
	# - At the end of the list, display the final values of sum, min, and max.					                |

	# - Prompt the user to enter elements for “myList”.								                            |
	# - Check if the user has entered any elements and if not, display an error message.				        |
	# - Initialize the sum, max, and min variables using the first element of the list.		
    # - Visit each element
    #     - Add elelemt to sum
    #     - If min < elem, set min to elem
    #     - If max > elem, set max to max	            |
	# - At the end of the list, display the final values of sum, min, and max.	


import sys

myList = list(map(int, input("Enter list of numbers: ").split()))   # - ...

if myList == []:    # - ...
        sys.exit("Sorry, you need to input a list")
    
sum = myList[0] # - ...
max = myList[0] # - ...
min = myList[0] # - ...

for index in range(1, len(myList)): # - ...
    element = myList[index]
    sum = sum + element
    if element < min:   # - ...
        min = element
    elif element > max: # - ...
        max = element

print("These are the sum, max, and min of the function.")
print("Sum:", sum)  # - ...
print("Min:", min)  # - ...
print("Max:", max)  # - ...

# - Case #1:
# - Input : [1, 2, 7, 5]
# - Output : 15, 7, 1

# - Case #2:
# - Input : [-1, -6, -300, -5]
# - Output : -312, -1, -300

# - Case #3:
# - Input : [1, 5, -1, -20]
# - Output : -15, 5, -20

# - Case #4:
# - Input : [y, 6, 7, giu]
# - Output : Error

# - Case #5:
# - Input : []
# - Output : sys.exit

# - Case #6:
# - Input : [1]
# - Output : 1, 1, 1

# - Case #7:
# - Input : [-2]
# - Output : -2, -2, -2

# - Case #7:
# - Input : [-2, 1]
# - Output : -1, 1, -2

# - Case #7:
# - Input : [-2, -4]
# - Output : -6, -2, -4
