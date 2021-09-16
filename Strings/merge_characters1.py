# program to merge characters of 2 strings into a single string by taking characters alternatively

s1 = 'roshan'
s2= 'reeeee'
output = ''
i,j = 0,0
# while ((i<len(s1)) or (j<len(s2))):
#     output = output + s1[i] + s2[j]
#     i = i+1
#     j = j+1
# print("Only works if string have same length")
print(output)
print("works if string have different length")
while i<len(s1) or j<len(s2):  
    if i<len(s1):  
        output=output+s1[i]  
        i=i+1  
    if j<len(s2):  
        output=output+s2[j]  
        j=j+1     
print(output)