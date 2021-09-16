# program to remove duplicate characters from the given input String

s ='AZZZBCDABBCDABBBBCCCCDDDDEEEEEF'
l = []
for ch in s:
    if ch not in l:
        l.append(ch)

print(f"{''.join(l)}")

#  find the number of occurrences of each character present in the given string
for ch in sorted(l):  
    print('{} occurrs {} times'.format(ch,s.count(ch)))    