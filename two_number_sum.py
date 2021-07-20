array = [3,5,-4,8,11,1,-1,6]
targetsum = 13

# First Solution using 2 for loops
# TC = O(n*2) | SC = O(1)

def two_number_sum1(array, targetsum):
    for i in range(len(array)-1):
        first_number = array[i]
        for j in range(i+1,len(array)):
            second_number = array[j]
            if first_number + second_number == targetsum:
                print(first_number,second_number)
    return None

# Second Solution using hash tables: data + x = targetsum ==> x = targetsum - data
# TC = O(n) | SC = O(n)

def two_number_sum2(array, targetsum):
    hashtable = {}
    for data in array:
        x = targetsum - data
        if x in hashtable:
            print(x , data)
        else:
            hashtable[data] = "Added"

# Third Solution using left and right mark in sorted array
# adding,comparing and changing marker
# TC = O(nlogn) | SC = O(1)

def two_number_sum3(array, targetsum):
    array.sort()
    left = 0
    right = len(array)-1
    while left < right:
        sum = array[left] + array[right]
        if sum == targetsum:
            print (array[left], array[right])
            left = len(array)
        elif sum < targetsum:
            left += 1
        elif sum > targetsum:
            right -= 1


# Testing Functions
two_number_sum1(array, targetsum)
two_number_sum2(array, targetsum)
two_number_sum3(array, targetsum)