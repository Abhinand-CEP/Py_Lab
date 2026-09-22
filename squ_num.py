l=[]
n=int(input("Enter the number of elements:"))
print("Enter the numbers:")
for i in range(0,n):
    num=int(input())
    l.append(num)
print("the square of the given numbers are : ")
for i in range(0,n):
    print(l[i]**2)