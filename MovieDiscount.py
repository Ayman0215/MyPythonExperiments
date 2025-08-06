
#3

# - ...
# - ...
# - ...
# - ...
# - ...

import sys

movie = str(input("Hello, what is the movie you are watching today? The options are Jurassic Park, F1, Superman, & Fantastic Four: "))
numberOfPeople = int(input("And how many people are going to that movie? "))
ifTheyAreAMember = str(input("Is any one in your party a member of Python Theaters? Please say Yes or No: "))
movies = ["Jurassic Park", "F1", "Superman", "Fantastic Four"]

manyPeopleGratutity = 0.1
memberDiscount = 0.15
salesTax = 0.09

if numberOfPeople <= 0:
    sys.exit("Sorry, but if you keep joking around you aren't allowed to go. Bye")

if movie not in movies:
    movie = str(input("Sorry, try again. Please let me know what movie you are watching? The options are Jurassic Park, F1, Superman, & Fantastic Four: "))
elif movie == "Jurassic Park" or "Fantastic Four" :
    moviePrice = 12
elif movie == "F1" :
    moviePrice = 15
elif movie == "Superman" :
    moviePrice = 10

if ifTheyAreAMember == "Yes" or "yes" :
    if numberOfPeople >= 6 :
        subtotal = (1 - memberDiscount) * ((1 + manyPeopleGratutity) * ((moviePrice * numberOfPeople) * (1 + salesTax))) 
    else:
        subtotal = (1 - memberDiscount) * (((moviePrice * numberOfPeople) * (1 + salesTax))) 
else:
    print("Since you aren't a member, you won't receive a discount.")
    if numberOfPeople >= 6 :
        subtotal = (1 + manyPeopleGratutity) * ((moviePrice * numberOfPeople) * (1 + salesTax))
    else:
        subtotal = ((moviePrice * numberOfPeople) * (1 + salesTax))

subtotal = round(float(subtotal), 2)

print(f"Here is your recipet: Your subtotal is ${subtotal}, by going to the {movie} movie with {numberOfPeople} people.")

# - Case #1: Number of People is less than 6.

# - Input: F1, 1, No
# - Ouput: $11.12

# - Case #2: Number of People is greater than 6.

# - Input: Superman 8, Yes
# - Ouput:$97.84

# - Case #3: The group has a member.

# - Input: Jurassic Park, 3, Yes
# - Ouput:$33.35

# - Case #4: The group doesn't have a member.

# - Input: Fantastic Four, 2, No
# - Ouput: $22.24
