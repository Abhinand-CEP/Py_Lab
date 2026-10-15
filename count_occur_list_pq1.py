names = []
n = int(input("Enter number of names: "))
print("Enter the names: ")
for i in range(n):
    na= input("")
    names.append(na)
c= 0
for na in names:
    c+= na.lower().count("a")
print("Occurrence of 'a':",c)