s=input("enter the strung:")
l=len(s)
print(l)
for i in range(0,l) :
 print(s.count(s[i]))

count=0
for i in s :
    if i =="1" :
        count +=1
    print("the string is:",i)
   
