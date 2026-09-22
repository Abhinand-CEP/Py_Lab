num=[]
n=int(input("Enter the number of elements in list:"))
for i in range(0,n):
    e=int(input("Enter the element:"))
    num.append(e)
print("the list of numbers is:",num)
print("the positive list of numbers is:")
for i in range(0,n):
    if num[i]>0:
        print(num[i])