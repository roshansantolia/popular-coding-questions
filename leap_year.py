#Leap Year

print("Check it is Leap year or Not")
year = int(input("Enter a year"))
if (year%4 == 0):
    if(year%100 == 0):
        if(year%400 == 0):
            print(year, "It is a Leap Year")
        else:
            print(year, " Not a leap Year")
    else:
        print(year, " It is a leap Year")
else:
    print(year, " Not a leap Year")