list=[1,2,2,3,1,4,4,3,2,7]
print(list)
l1=[]
for i in list:
    if i not in l1:
        l1.remove(i)
        #list.remove(i)
print(l1)        
