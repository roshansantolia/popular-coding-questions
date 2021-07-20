# TC = O(n*2) | SC = O(n)
def palindrome1(string):
    reversed_string = ""
    for i in reversed(range(len(string))):
        reversed_string += string[i]
    if (reversed_string == string):
        print("It is a Palindrome")
    else:
        print("It is not a palindrome")


# TC = O(n) | SC = O(n)
def palindrome2(string):
    reversed_list = []
    for i in reversed(range(len(string))):
        reversed_list.append(string[i])
    if (("".join(reversed_list)) == string):
        print("It is a Palindrome")
    else:
        print("It is not a palindrome")


# TC = O(n) | SC = O(n)
# Using below Tail recursion we can make SC=O(1) but it depends on compiler
def palindrome3(string, i=0):
    j = len(string) - 1 - i
    if (i > j):
        return True
    if string[i] != string[j]:
        return False
    return palindrome3(string, i + 1)


#   return True if (i>j) else string[i]==string[j] and palindrome3(string, i+1)

# TC = O(n) | SC = O(1)
def palindrome4(string):
    left_pointer = 0
    right_pointer = len(string) - 1
    while left_pointer < right_pointer:
        if string[left_pointer] != string[right_pointer]:
            return False
        left_pointer += 1
        right_pointer -= 1
    return True


string = "abcdcba"

palindrome1(string)
palindrome2(string)
print(palindrome3(string))
print(palindrome4(string))

