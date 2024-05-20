fn = input("Please type in First Name: ")
ln = input("Please type in Last Name: ")
gpa = int(input("Please type in GPA: "))
days = 0
s = 0
ln[0] <= "K"
if ln[1] >= "K":
    days = "Monday & Thursday"
if ln[1] <= "L":
    days = "Tuesday & Friday"
if gpa >= 3.86:
    s = 16000
elif gpa >= 3.7 and gpa <= 3.85:
    s = 12000
elif gpa >= 3.5 and gpa <= 3.69:
    s = 8000
elif gpa >= 3.25 and gpa <= 3.49:
    s = 4000
elif gpa >= 3.25:
    s = 0
print("Hello, ", fn ,". You should report to school on ", days ,". You are eligibile for a scholarship of", s , ".")