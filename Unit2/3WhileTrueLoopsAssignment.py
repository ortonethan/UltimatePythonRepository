# ========== 2.3.1 ==========
# while True:
#     answer = (input("Please type in a number, -1 to quit: "))

#     if answer == "no":
#         break

#     print("ok then")

# print("Thanks and bye!")

# # ========== 2.3.2 ==========
# from math import sqrt
# while True:
#     number = int(input("Please type in a number: "))

#     if number < 0:
#         print("invalid number")
#     elif number > 0:
#         print(sqrt(number))
#     elif number == 0:
#         break
#     print("Exiting...")
# ========== 2.3.3 ==========
# number = 5
# print("Countdown!")
# while True:
#   print(number)
#   number = number - 1
#   if number < 1:
#     break

# print("Now!")

# # ========== 2.3.4 ==========
# while True:
#     p1 = (input("Password: "))
#     p2 = (input("Repeat Password: "))
#     if p1 != p2:
#        print("They do not match!")
#     if p1 == p2:
#        print("User account created!")
#        break
# ========== 2.3.5 ==========
# pin = 4321
# attempts = 0
# while True:
#    p = int(input("Pin: "))
#    attempts = attempts + 1
#    if p == pin and attempts == 1:
#       print("Correct! It only took you a single attempt!")
#       break
#    elif p == pin:
#       print("Correct! It took you", attempts ,"attempts")

# ========== 2.3.6 ==========
year = int(input("year: "))
print("The next leap year after", year , "is", ((year - (year%4) +4)))

# ========== 2.3.7 ==========
string = ""
pword = ""
word = ""
while True:
    pword = word
    word = input("Please type in a word: ")
    if word != "end" and word != pword:
       string = str(str(string) + str(word) + " ")
    else:
        print(str(string))
        break
# ========== 2.3.8 ==========
string = ""
pword = ""
word = ""
while True:
    pword = word
    word = input("Please type in a word: ")
    if word != "end" and word != pword:
       string = str(str(string) + str(word) + " ")
      
    else:
        print(str(string))
        break

# ========== 2.3.9 ==========
n = ""
sum = 0
mean = 0
pos = 0
neg = 0

