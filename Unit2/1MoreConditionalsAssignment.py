# print("########## 2.1.1 ##########")
#word = input("PLease type in a word: ")
#print("there are " ,len(word), " letters in the word " , word)
#print("Thank you!")
# print("########## 2.1.2 ##########")
#number = float(input("Please type in a number: "))
#print("Integer part: ", int(number))
#print("Decimal part: ", (float(number)-(int(number))))
# print("########## 2.1.3 ##########")
#agetovote = input("How old are you? ")
#if int(agetovote) < 18:
#    print("you are not able to vote")
#elif int(agetovote) >= 18:
#    print("You may vote!")
# print("########## 2.1.4 ##########")
#n1 = int(input("Please type in the first number: "))
#n2 = int(input("Please type in the second number: "))
#if n1 > n2:
#    print("the greater number was: ", n1)
#if n1 < n2:
#    print("the greater number was: ", n2)
#if n1 == n2:
#    print("The numbers are equal!: ", n1)
# print("########## 2.1.5 ##########")
#print("person 1: ")
#n1 = input("Name: ")
#a1 = input("Age: ")
#print("person 2: ")
#n2 = input("Name: ")
#a2 = input("Age: ")
#if n1 > n2:
#    print("the elder is ", n1)
#if n1 < n2:
#    print("the elder is ", n2)
#if n1 == n2:
#    print(n1 , " and " , n2 , "are the same age")
# print("########## 2.1.6 ##########")
n1 = (input("Please type in the 1st word: "))
n2 = (input("Please type in the 2st word: "))
if n1 > n2:
    print(n1, "comes alphabetically last. ")
elif n1 < n2:
    print(n2, "comes alphabetically last. ")
if n1 == n2:
    print("You gave the same word twice.")