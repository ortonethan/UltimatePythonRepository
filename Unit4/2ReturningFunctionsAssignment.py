def greatest_number(n1, n2, n3):
    if n1 >= n2 and n1 >= n3:
        return n1
    elif n2 >= n1 and n2 >= n3:
        return n2
    elif n3 >= n1 and n3 >= n2:
        return n3
    
    print(greatest_number(3, 4, 1)) #4
    print(greatest_number(99, -4, 7)) #99
    print(greatest_number(0, 0, 0)) #0

