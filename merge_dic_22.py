d1={}
d2={}
n1=int(input("enter no of elements in first dictionary:"))
n2=int(input("enter no of elements in second dictionary:"))
print("enter key then value and repeat for dictionary 1")
for i in range(n1):
    key=input("")
    v=input("")
    d1[key]=v
print("enter key then value and repeat for dictionary 2")
for i in range(n2):
    key=input("")
    v=input("")
    d2[key]=v
print("dictionary 1 ",d1)
print("dictionary 2 ",d2)
d1.update(d2)
print("merged dictionary is",d1)