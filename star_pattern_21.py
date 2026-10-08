n=int(input("enter the upper limit:"))
for i in range(0,n):
    print("\n")
    for j in range(0,i+1):
        print("* \t",end=" ")
for i in range(n,0,-1):
    print("\n")
    for j in range(0,i-1):
        print("* \t",end=" ")