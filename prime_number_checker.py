#Prime Number Checker

def prime_checker(number):
    is_prime = True
    for i in range(2,(number-1)):
        if(number%i==0):
            is_prime = False
    if is_prime:
        print("It is a Prime Number")
    else:
        print("It is not a Prime Number")

n = int(input("Enter a number"))
prime_checker(number=n)