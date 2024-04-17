
# using 3 if statements
number = int(input("Please type in a number"))
if number > 0:
    print("number is positive")
if number < 0:
    print("number is negative")
if number == 0:
    print("number is zero")

# using elif & else instead
if number > 0:
    print("number is positive")
elif number < 0:
    print("number is negative")
else:
    print("number is zero")