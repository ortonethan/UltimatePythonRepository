terms = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,]
print(int(input("Enter expression ")))
if terms[2] == "+":
    print(terms[1]+terms[3])
elif terms[2] == "-":
    print(terms[1]-terms[3])
elif terms[2] == "*":
    print(terms[1]*terms[3])
elif terms[2] == "/":
    print(terms[1]/terms[3])