# print("########## 2.2.1 ##########")
# number = int(input("What is your age: "))
# if number >= 5:
#     print("Ok, you are", number ,"years old")
# elif number <= 5:
#     print("I suspect you can't write quite yet...")
# elif number <= 0:
#     print("that must be a mistake")
# # print("########## 2.2.2 ##########")
# name = input("Please type in your name: ")
# if name == "Morty" or name == "Ferdie" :
#     print("I think you are one of Mickey mouses nephews")
# elif name == "Huey" or name == "Dewey" or name == "Louie" :
#     print("I think you might be one of Donald Duck's nephews.")    
# else : print("You're not a nephew of any character I know of.")
# # print("########## 2.2.3 ##########")
number = int(input("Type in percent: "))
if number >= 59:
    print("F")
elif number >= 60 and number <= 69:
    print("D")
elif number >= 70 and number <= 79:
    print("C")
elif number >= 80 and number <= 89:
    print("B")
elif number >= 90 and number <= 100:
    print("A")
elif number <=0 or number >> 100: 
    print("impossible!") 
# print("########## 2.2.4 ##########")
# number = int(input("Number: "))
# if number %3 == 0:
#     print("Fizz", end="")
# if number %5 == 0:
#     print("Buzz")

# else:
#     print("")
# print("########## 2.2.5 ##########")
# ly = int(input("Please type in a year: "))
# if ly %4 == 0 and (ly %400 == 0 or ly %100 != 0):
#     print("that year is a leap year. ")
# else:
#     print("that year is not a leap year")
# print("########## 2.2.6 ##########")
l1 = (input("1st letter: "))
l2 = (input("2nd letter: "))
l3 = (input("3rd letter: "))
if l1 > l2 and l1 < l3:
    print("the letter in the middle is ", l1)
if l2 > l1 and l2 < l3:
    print("the letter in the middle is ", l1)

