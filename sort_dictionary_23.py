d1={}
n=int(input("enter the no. of elements"))
print("enter key,value and repeat for dictionary")
for i in range(n):
    key=input("")
    v=input("")
    d1[key]=v
print("dictionary is ",d1)
d1_asc=sorted(d1.items())
print(" dictionary in ascending order is ",d1_asc)
d1_dsc=sorted(d1.items(),reverse=True)
print(" dictionary in descending order is ",d1_dsc)