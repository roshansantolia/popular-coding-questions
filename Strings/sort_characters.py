# program to sort characters of the string, first alphabet symbols followed by digits

s='r1o2s3h4a5n6'  
alphabets=[]  
digits=[]  
for ch in s:  
    if ch.isalpha():  
        alphabets.append(ch)  
    else:  
        digits.append(ch)  
output=''.join(sorted(alphabets)+sorted(digits))  
print(output)