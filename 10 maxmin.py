print("a program to find the maximum and minimun value in a set")
s2=set()
n=int(input("enter the limit"))
s=0
while n>s :
    s2.add(int(input("enter number :")))
    s=s+1
for e in s2 :
    print(e)
print("the maximum value is",max(s2))
print("the minimum value is",min(s2))