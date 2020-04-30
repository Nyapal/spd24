# Problem 1
# Given an array a of n numbers and a target value t, find two numbers whose sum is t.
# Example: a=[5, 3, 6, 8, 2, 4, 7], t=10 [3, 7] or [6, 4] or [8, 2]

def problemOne(arr, t):
    for num in arr:
        output = []
        output.append(num)
        arr.remove(num)
        target = t - num 
        if target in arr:
            output.append(target)
            return 'The Numbers Are: ', output
        arr.append(num)
    return 'Not Found' 

test_one = problemOne([8,2,7], 10)
# print(test_one)

# Problem 2
# Given an array a of n numbers and a count k find the k largest values in the array.
# Example: a=[5, 1, 3, 6, 8, 2, 4, 7], k=3 [6, 8, 7]

def problemTwo(arr, k):
    arr.sort()
    arr_len = len(arr)
    sumn = len(arr) - k
    arr[0:arr_len]
     
    return arr[sumn:arr_len]

test_two = problemTwo([5, 1, 3, 6, 8, 2, 4, 7], 3)
# print(test_two)

# Problem 3
# Given two arrays a and b of numbers and a target value t, find a number from each array whose sum is closest to t.
# Example: a=[9, 13, 1, 8, 12, 0, 5], b=[3, 17, 4, 14, 6], t=20 [13, 6] or [4, 17] or [5, 14]

def problemThree(a, b, t):
    print(a, b, t)
    return 'yes'
test_three = problemThree([9, 13, 1, 8, 12, 4, 0, 5], [3, 17, 4, 14, 6], 20)
print(test_three)