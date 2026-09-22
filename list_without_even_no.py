num=[]
n=int(input("enter the no. of elements:"))
print("enter the elements:")
for i in range(0,n):
    numb=int(input())
    num.append(numb)
print("original list :", num)
u_l=[]
for i in range(0,n):
    if num[i]%2!=0:
        u_l.append(num[i])
print("updated list :", u_l)

