n=int(input("enter the no of terms"))
a=0
b=1
print(a,'\n')
for i in range(1,n):
    c=a+b
    a=b
    b=c
    print(a,'\n')
