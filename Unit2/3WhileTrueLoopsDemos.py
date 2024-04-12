# print hello repeatedly forever
# while True:
#     print("hello")

# square numbers until the user types in -1
# while True:
#     num = int(input("Type in a number to square (or -1 to stop): "))

#     if num == -1:
#         break

#     print(num * num)

num = int(input("Type in a number to square (or -1 to stop): "))    
while True:
    if num == -1:
        break
    print(num * num)