l=[];
n=int(input("Enter the limit: "))
print("Enter the numbers")
for i in range(0,n):
    num=int(input(''))
    l.append(num)
print(l)
s=0
for i in range(0,n):
    s=s+l[i]
print("sum of numbers is",s)
