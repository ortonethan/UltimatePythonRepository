# age = int(input("Enter your age"))

# # offer kids menu for people aged 5-11
# if age >= 5 and age <= 11:
#     print("Here's a kids menu")

# score = int(input("Enter your percent score"))

# # print a message if they've entered an impossible score
# if score < 0 or score > 100:
#     print("I think you entered an invalid score")

# # another way
# if not (score >= 0 and score <= 100):
#     print("I think you entered an invalid score")

number = int(input("Enter a number"))

# print whether the number is odd or even. Numbers below 1 aren't 
if number <= 0:
    print("number is negative or zero")
else:
    if number % 2 == 0:
        print("number is even")
    else:
        print("number is odd")