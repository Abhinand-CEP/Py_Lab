n1=int(input("enter the first number"))
n2=int(input("enter the second number"))
n=min(n1,n2)
for i in range(1,n+1):
    if n1%i==0 and n2%i==0:
        gcd=i
print("the gcd of ",n1," and ",n2," is ",gcd)