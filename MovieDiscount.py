
#3

# - ...
# - ...
# - ...
# - ...
# - ...

import sys

movie = str(input("Hello, what is the movie you re watching today? The options are Jurassic Park, F1, Superman, & Fantastic Four: "))
numberOfPeople = int(input("And how many people are going to that movie? "))
ifTheyAreAMember = str(input("Is any one in your party a member of Python Theaters? Please say Yes or No: "))

manyPeopleGratutity = 0.1
memberDiscount = 0.15
salesTax = 0.09

if numberOfPeople <= 0:
    sys.exit("Sorry, but if you keep joking around you aren't allowed to go. Bye")

if movie != " Jurassic Park" or "F1" or "Superman" or "Fantastic Four":
    movie = str(input("Sorry, try again. Please tell me what movie you are watching? The options are Jurassic Park, F1, Superman, & Fantastic Four: "))
elif movie == "Jurassic Park" :
    moviePrice = 12
elif movie == "F1" :
    moviePrice = 15
elif movie == "Superman" :
    moviePrice = 10
elif movie == "Fantastic Four" :    
    moviePrice = 12

if ifTheyAreAMember == "Yes" or "yes" :
    if numberOfPeople >= 6 :
        subtotal = (1 - memberDiscount) * ((1 + manyPeopleGratutity) * ((moviePrice * numberOfPeople) * (1 + salesTax))) 
    else:
        subtotal = (1 - memberDiscount) * (((moviePrice * numberOfPeople) * (1 + salesTax))) 
else:
    print("You are telling me you aren't a member. If you are one, please try again")
    if numberOfPeople >= 6 :
        subtotal = (1 + manyPeopleGratutity) * ((moviePrice * numberOfPeople) * (1 + salesTax))
    else:
        subtotal = ((moviePrice * numberOfPeople) * (1 + salesTax))

subtotal = round(int(subtotal), 2)

print(f"Here is your recipet: Your subtotal is ${subtotal}, by going to the {movie} movie with {numberOfPeople} people.")

# - Case #1: Number of People is less than 6.

# - Input: F1, 1, No
# - Ouput:

# - Case #2: Number of People is greater than 6.

# - Input: Superman 8, Yes
# - Ouput:

# - Case #3: The group has a member.

# - Input: Jurassic Park, 3, Yes
# - Ouput:

# - Case #4: The group doesn't have a member.

# - Input: Fantastic Four, 2, No
# - Ouput: 
