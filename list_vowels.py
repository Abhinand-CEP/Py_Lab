w=input("enter the word")
v="aeiouAEIOU"
v_l=[]
for i in w:
    if i in v:
        v_l.append(i)
print("Vowels in ",w," are ",v_l)