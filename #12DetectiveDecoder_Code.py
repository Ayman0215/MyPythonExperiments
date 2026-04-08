message = str(input("Enter here: "))

for i in range(len(message) - 2):
    code = message[i:i+3]
    if code.isdigit():
        print(f"Code found: {code}")