# Program to print the characters present at even index and odd index seperately for the given string

s = 'roshan'
print("Characters at even position")
length = len(s)
i = 0
while (i < length):
    print(s[i])
    i+=2
print("Characters at odd position")
i=1
while (i < length):
    print(s[i])
    i+=2
print("This can also be achieved by Slice function")
    