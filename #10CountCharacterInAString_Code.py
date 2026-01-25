def count_character(text, char):
    count = 0
    for letter in text:
        if letter == char:
            count += 1
    return count

text = str(input("Enter a string: "))
char = str(input("Enter a character to count: "))
result = count_character(text, char)