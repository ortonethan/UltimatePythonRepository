print("########## 1.4.1 ##########")
user_string = input("please type in number" )
number = int(user_string)
print( user_string + " times 5 is", number*5)
print("########## 1.4.2 ##########")
name = input("what is your name?")
year = input("which year where you born?")
intyear = int(year)
age = (2024-intyear)
print("Hi" + name + " ,you will be " , age , "years old at the end of the year 2024")
print("########## 1.4.3 ##########")
n = input("how many days?")
number = int(n)
siad= (number*86400)
print("Seconds in that many days:", siad)
print("########## 1.4.4 ##########")
# Fix the code
number1 = int(input("Please type in the first number: "))
number2 = int(input("Please type in the second number: "))
number3 = int(input("Please type in the third number: "))

product = (number1 * number2 * number3)

print("The product is", product)

print("########## 1.4.5 ##########")
number1 = int(input("Number 1: "))
number2 = int(input("Number 2: "))
print("The sum of the numbers is", number1+number2)
print("The product of the numbers is", number1*number2)
print("########## 1.4.6 ##########")
number1 = int(input("Number 1: "))
number2 = int(input("Number 2: "))
number3 = int(input("Number 3: "))
number4 = int(input("Number 4: "))
print("the sum of the numbers is", number1+number2+number3+number4,"and the mean is", (number1+number2+number3+number4)/4)
print("########## 1.4.7 ##########")
times = float(input("How many times a week do you eat at the student cafeteria?"))
price = float(input("The price of a typical student lunch?"))
groceries = float(input("How much money do you spend on groceries in a week?"))

Daily = (((times)*(price))+(groceries)/7)
weekly= (((times)*price)+groceries)
print()
print("Average food expenditure:")
print("Daily: $", str(Daily))
print("Weekly: $", str(weekly))
print("########## 1.4.8 ##########")
age = int(input("how old are you?"))
if age >= 18:
    print("you are old enough to vote")
    print("is your ballot")
print("next in line please")