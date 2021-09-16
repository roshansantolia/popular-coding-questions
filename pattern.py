# pattern 

print("Right Angle Triangle\n")

n = int(input("Enter the no of rows = "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*", end="")
    print("")
print("\n")  
    
print("Opp Right Angle Triangle\n")
for i in range(1,n+1):
    print(" "*(n-i),end="")
    print("*"*i)
print("\n")

print("Equivalent Triangle\n")
for i in range(1,n+1):
    print(" "*(n-i),end="")
    print("* "*i)
print("\n")

