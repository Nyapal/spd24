# Problem 1
# Given an array a of n numbers and a target value t, find two numbers whose sum is t.
# Example: a=[5, 3, 6, 8, 2, 4, 7], t=10  [3, 7] or [6, 4] or [8, 2]

def problemOne (n, t):
    output = []
    for num in n:
        possible_sum = t - num 

        if possible_sum in n:
            forst = output.append([num,])
            second = output.append(possible_sum)
        # print(num)
    return output

if __name__ == "__main__":--
    solution = problemOne([5, 4, 2, 7], 6)
    print(solution)