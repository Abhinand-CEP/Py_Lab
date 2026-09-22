num=[]
n=int(input("Enter the number of elements: "))
print("Enter the element: ")
for i in range(0,n):
    e=int(input())
    num.append(e)
print("\n the list of integers is ",num)
for i in range(0,n):
    if num[i]>100:
        num[i]="over"
print("The new changed list of integers is ",num)