print("program to to add elements of list to a set")
s1={"python","Django","Javascript"}
l1=["java","c"]
print(type(s1),s1)
print(type(l1),l1)
for e in l1 :
    s1.add(e)

print(type(s1),s1)