# program to find the number of occurrences of each vowel present in the given string

s = "roshan"  
v = ['a','e','i','o','u','A','E','I','O','U']  
l=[]
for ch in s:
    if ch in v:
        l.append(ch)
print(l) # vowels in a string
for ch in s:
    if ch in v:
        print(f"{ch} occurs {s.count(ch)} times") # occurence
        