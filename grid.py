# Given an array of values you need to map the values on to a grid. 
# Return an array of objects containing the original value, and a row and col that would represent the position of where the object would map on the grid. 
# Assume the length of the original array is always a square e.g. 4, 9, 16 etc. Assume the grid has an equal height and width.

def grid (arr):
    length = len(arr)  # length = 16 items
    width = int(length ** .5)
    output = []
    for i in range(0, length, width):
        subarray = arr[i:i+width]
        output.append(subarray)
    return output

def location(n):
    
    

print(grid([5, 1, 9, 3]))

# output: 
# [ {5: (0, 0)}, 
#   {1: (0, 1)}, 
#   {9: (1: 0)}, 
#   {3: (1, 1)} ]

# [ 
#     { value: 1,
#       row: 0,
#       col: 0},
# ]