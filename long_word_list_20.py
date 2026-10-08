l=[]
n=int(input("Enter the no of words in list"))
print("Enter the words")
for i in range(0,n):
    a=input("")
    l.append(a)
print("the list is ",l)
leng=len(l[0])
s=l[0]
for i in range(1,n):
    if (len(l[i])>leng):
        s=l[i]
        leng=len(s)
print("the longest word is ",s)
print("the length of the word is ",leng)
