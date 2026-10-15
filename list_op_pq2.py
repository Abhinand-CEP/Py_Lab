l1=[]
l2=[]
n1=int(input("enter no of elements in list 1: "))
n2=int(input("enter no of elements in list 2: "))
print("enter the values of list1")
for i in range(n1):
    val1=int(input())
    l1.append(val1)
print("enter the values of list2")
for i in range(n2):
    val2=int(input())
    l2.append(val2)
if len(l1) == len(l2):
    print("Both lists have the same length")
else:
    print(" Lists have different lengths")
if sum(l1) == sum(l2):
    print("2. Both lists have the same sum")
else:
    print("2. Lists have different sums")
for val1 in l1:
    if val2 in l2:
        common=True
        break
if common:
    print("3. Both lists have at least one common value")
else:
    print("3. No common values")

