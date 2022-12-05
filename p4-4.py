DS=int(input("Enter marks of the first subject: "))
OS=int(input("Enter marks of the second subject: "))
python=int(input("Enter marks of the third subject: "))
RDBMS=int(input("Enter marks of the fourth subject: "))

avg=float((DS+OS+python+RDBMS)/4)
if(avg>=90):
    print("Grade: A")
elif(avg>=80 and avg<89):
    print("Grade: B")
elif(avg>=70 and avg<79):
    print("Grade: C")
elif(avg>=60 and avg<69):
    print("Grade: D")
elif(avg>=50 and avg<59):
    print("Grade: E")    
else:
    print("Grade: F")
    
    