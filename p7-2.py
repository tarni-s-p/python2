s1={10,20,30,40}
s2={10,20,60,80,70,90}

print(s1)
print(s2)

print("add elements")
s1.add(50)
print(s1)

#print("remove elements")
#s1.remove(s2)
#print(s1)

print("elements are union")
print(s1|s2)

print("elements are intersection")
print(s1&s2)

print("elements are differefnce")
print(s1-s2)
print(s2-s1)

print("elements are symmetric difference")
print(s1^s2)

print("elements check subset of another set")
print(s1<s2)
