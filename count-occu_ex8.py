s=input("Enter a string")
sr=input("Enter the word to be searched;")
x=s.split(" ")
c=0
for i in x:
    if(i==sr):
        c+=1
print("the total occurance of the word",sr,"is",c)