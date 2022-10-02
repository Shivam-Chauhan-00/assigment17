print("program to add item from another set to the current set")
s1={"java","python","SQL"}
s2={"C","Cpp","NoSQL"}
print(s1)
print(s2)
for e in s2 :
    s1.add(e)
print(s1)