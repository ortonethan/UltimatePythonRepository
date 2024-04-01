
print("########## 1.5.1 ##########")

print("########## 1.5.2 ##########")

print("########## 1.5.3 ##########")

print("########## 1.5.4 ##########")

print("########## 1.5.5 ##########")

print("########## 1.5.6 ##########")

print("########## 1.5.7 ##########")

print("########## 1.5.8 ##########")
# Fix the program
points = int(input("How many points are on your card? "))
if points < 100:
    points *= 1.1
    print("Your bonus is 10 %")

if points >= 100:
    points *= 1.15
    print("Your bonus is 15 %")

print("You now have", points, "points")

print("########## 1.5.9 ##########")
