#1.	Write a Python function reverse_string() that takes a string as input and returns the reversed string.
"""""
x = input("Enter A Name: ")

def reverse_string():
    return x[::-1]

reverse_string()
"""""
#Write a for loop that prints the numbers from 1 to 10.
"""""
for x in range(1,11):
    print(x)
"""""
#Write a while loop that prints the numbers from 10 to 1 in descending order.
"""""
x = 10
while x > 0 :
    print(x)
    x = x - 1
"""""
#Write a function calculate_area() that takes the length and width of a rectangle as parameters and returns the area of the rectangle.
"""""
x = int(input("Enter a Width : "))
y = int(input("Enter a Length : "))
def calculate_area():
    z = x * y
    z = str(z)
    print("Your Area is " + z)

calculate_area()
"""""
a = 0
b = 1
sequence = []
while a <= 50:
    sequence.append(a)
    c=b
    b =a+b
    a= c
    print(sequence)