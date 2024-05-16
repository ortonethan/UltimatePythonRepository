# # ========== 3.2.1 ==========
# w = input("please type in a string: ")
# a = int(input("please type in an amount: "))
# print((w*a))
# # ========== 3.2.2 ==========
# s1 = input("please type in string 1: ")
# s2 = input("please type in string 1: ")
# if len(s1) > len(s2):
#     print(s1, "is longer")
# elif len(s2) > len(s1):
#     print(s2, "is longer")
# else:
#     print("strings are equally long")
# # ========== 3.2.3 ==========
# w = input("please type in a string")
# p = len(w)-1
# while p >= 0:
#     print(w[p])
#     p -= 1
# # ========== 3.2.4 ==========
# w = input("please type in a string")
# p = len(w)-1
# if len(w) >= 2:
#     if(w[p - 1]) == (w[1]):
#         print("the second and second to last character are", w[1])
#     else:
#         print("the second and second to last characters are different")
# # ========== 3.2.5 ==========
# w = int(input("width: "))
# print("#"*w)
# # ========== 3.2.6 ==========
# w = int(input("width: "))
# h = int(input("height: "))
# while h > 0:
#     print("#"*w)
#     h -= 1
# # ========== 3.2.7 ==========
# while True:
#     s1 = input("please type in a string: ")
#     if s1 != "":
#         print(s1)
#         print("-"*len(s1))
#     else:
#         break
# # ========== 3.2.8 ==========
# s1 = input("please type in a string: ")
# print("*"*(20-len(s1)))
# # ========== 3.2.9 ==========
# w = input("word: ")
# l = int(len(w)/2)
# print("")
# print("*"*30)
# if len(w) % 2 == 0:
#     print("*"+(" "*(14-l)) + w + (" "*(14-l)) + "*")
# else:
#     print("*"+(" "*(14-l)) + w + (" "*(13-l)) + "*")
# print("*"*30)
