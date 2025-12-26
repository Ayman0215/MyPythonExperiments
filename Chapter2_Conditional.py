#One-Way Conditional
#Checks if a number is greater than 100. If the number is greater than 100, print "The number is large."
"""""
number = input("Enter A Word: ")
try :
    number = int(number)
    print("Error")
except :
    if number == "pneumonoultramicroscopicsilicovolcanoconiosis" :
        print("This word is large")
    else :
        print("This word is small")
print("Next Task")

#Two Way Conditional
#Checks if a number is even or odd.
#If the number is even, print: "The number is even."
#If the number is odd, print: "The number is odd."

number2 = input("Enter A Number: ")
number2 = int(number2)
if number2 % 2 == 0 :
    print("The number is even.")
else :
    print("The number is odd.c")
print("Next Task")

#Classify a person's age into the following categories
#Below 13 : "Child"
#13 to 19: "Teenager"
#20 to 64: "Adult"
#65 and above: "Senior"

age = input("What Is Your Age: ")
age = int(age)
if age < 13 :
    print("You Are A Child")
elif age in range(13,19) :
    print("You Are A Teenager")
elif age in range(20,64) :
    print("You Are An Adult")
elif age in range(65,120) :
    print("You Are A Senior")
elif age >= 121 :
    print("You Are Supposed To Be Dead, Congrates That You Lived To" , age)
print("Next Task")

#Takes a number as input
#Checks whether the number is positive, negative, or zero
#Print the appropriate message:
#."Positive", "Negative", "Zero"

number3 = input("I Need Another Number: ")
number3 = int(number3)
if number3 <= -1 :
    print("Your Number Is Negative")
elif number3 >= 1 :
    print("Your Number Is Positive")
else :
    print("Your Number Is Neither Positive or Negative, But Zero Itself")
print("Next Task")

# Write a function to calculate the square of a number.

def Squaring(x):
    result = x ** 2
    return result

Number4 = input("Give A Number: ")
Number4 = int(Number4) 
print("Your New Number is" , Squaring(Number4))
"""""
# Create a function that takes a list of numbers and returns their sum.
        
def CalcUpto10() :
    intArray = [100,200,300,400]  
    for i, data in  enumerate(intArray) :
        print('i =' ,i)
        print('intArray[i] = ',intArray[i])
        print(" ")

    j=0
    while(j < 5) :
        print('j =' ,j)
        print('intArray[j] = ',intArray[j])
        print(" ")

        
CalcUpto10()