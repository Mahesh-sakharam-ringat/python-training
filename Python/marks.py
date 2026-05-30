sub1=int(input("Enter subject 1 marks"))
sub2=int(input("Enter subject 2 marks"))
sub3=int(input("Enter subject 3 marks"))
sub4=int(input("Enter subject 4 marks"))
sub5=int(input("Enter subject 5 marks"))

# Calculating total,average,and percentage
total = sub1+sub2+sub3+sub4+sub5
average =total / 5
percentage =(total / 500) * 100

# Printing the result
print ("Total marks:",total)
print("your percentage:",percentage)

#Grading logic based on percentage
if percentage >= 75:
    print("Result :Distinction")
elif percentage >= 60:
    print("Result :First class")

elif percentage >=45:
    print("Result :pass class")
else:
    print("Result :fail")    