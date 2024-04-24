# # slicing
original = "example"

# single letter
# part1 = original[1]
# print("Just extracted:", part1)

# range of letters
# includes left index,
# does not include right index
# part2 = original[2:5]
# print("Just extracted:", part2)

# # left bound not included - 
# # goes from the start
# part3 = original[:3]
# print("Just extracted:", part3)


# # right bound not included - 
# part4 = original[3:]
# print("Just extracted:", part4)

# ## using `in`
# original = "example"
# print("m" in original)
# print("s" in original)
# print("amp" in original)
# print("plm" in original)

# ## using string.find()
original = "example"
# print( original.find("m") )
# print( original.find("s") )
print( original.find("amp") )









# target2 = "xam"
# print(original.find(target2))
# target3 = "xamb"
# print(original.find(target3))