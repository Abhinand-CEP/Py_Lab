s=input("enter string")
if s[-3:]=="ing":
    s=s+"ly"
else:
    s=s+"ing"
print("the new string is",s)