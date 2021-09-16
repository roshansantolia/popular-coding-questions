# Program to reverse internal content of each word

s = "My name is roshan"
l = s.split()
l1=[]
for word in l:
    l1.append(word[::-1])
print(f"{' '.join(l1)}")