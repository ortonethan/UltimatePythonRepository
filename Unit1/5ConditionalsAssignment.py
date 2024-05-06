
#print("########## 1.5.1 ##########")
#year = int(input("Please type in a number:"))
#if year == int(1984):
#    print("Orwell")
#print("########## 1.5.2 ##########")
#number = int(input("Please type in a number:"))
#if number < 0 :
#    number = number*-1
#print("The absolute value of this number is", number)
#print("########## 1.5.3 ##########")
#Name = (input("What is your name? "))
#if Name != "jerry":
#    portions = int(input("How many portions of soup?"))
#    print("The total cost is", portions*5.9)
#print("Next Please!")
#print("########## 1.5.4 ##########")
#number = int(input("Type in a number:"))
#if number < 1000:
#    print("This number is less than 1000")
    # if number < 100:
    #     print("This number is less than 100")
    #     if number < 10:
    #         print("This number is less than 10")
#print("Thank you!")
# print("########## 1.5.5 ##########")
# n1 = int(input("Number 1: "))
# n2 = int(input("Number 2: "))
# op = input("Operaton: ")
# if op == "add":
#     print(n1, "+", n2 ,"=", n1+n2)
# if op == "subtract":
#     print(n1, "-", n2 ,"=", n1-n2)
# if op == "add":
#     print(n1, "*", n2 ,"=", n1*n2)
# if op == "divide":
#     print(n1, "/", n2 ,"=", n1/n2)
# print("########## 1.5.6 ##########")
# t = int(input("Type in a temperature (F): 101"))
# c = (t-32)*(5/9)
# if c > 0:
#     print("Brr! It's cold in here!")
# else:
#     print(t ,"degrees farenheit equals", c , "degrees celsius" )
# print("########## 1.5.7 ##########")
# h = int(input("Hourly wage: "))
# hw = int(input("Hours worked: "))
# d = (input("Day of the week:  "))
# if d == "Sunday":
#     print("Daily Wages: ", h*hw*2)
# else:
#     print("Daily Wages: ", h*hw)
print("########## 1.5.8 ##########")
# Fix the program
points = int(input("How many points are on your card? "))
if points < 100:
    points *= 1.1
    print("Your bonus is 10 %")
    print("You now have", points, "points")

elif points >= 100:
    points *= 1.15
    print("Your bonus is 15 %")
    print("You now have", points, "points")

print("########## 1.5.9 ##########")
print("What is the weather forcast tomorrow?")