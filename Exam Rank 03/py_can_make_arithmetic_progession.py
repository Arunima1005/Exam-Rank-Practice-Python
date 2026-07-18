# Problem 17: Can Make Arithmetic Progression
# A sequence of numbers is called an arithmetic progression 
# if the difference between any two consecutive elements is the same. 
# Given an array of numbers arr, 
# return true if the array can be rearranged to form an arithmetic progression. 
#   Otherwise, return false.
# Examples:
# [3, 5, 1] → True (can be rearranged to [1, 3, 5] with difference 2)
# [1, 2, 4] → False
# [1, 3, 5, 7] → True (difference is 2)


def can_make_arithmetic_progession(x):
    if len(x) < 2:
        return True
    x.sort()
    diff = x[1]-x[0]
    
    for n1, n2 in zip(x, x[1:]):
        if n2-n1 != diff:
            return False
        
    return True

print(can_make_arithmetic_progession([3, 5, 1]))
print(can_make_arithmetic_progession([1, 2, 4]))
print(can_make_arithmetic_progession([1, 3, 5, 7]))

## without zip

# def can_make_arithmetic_progression(arr: list[int]) -> bool:
#     if len(arr) < 3:
#         return True

#     arr = sorted(arr)

#     diff = arr[1] - arr[0]

#     for i in range(2, len(arr)):
#         if arr[i] - arr[i - 1] != diff:
#             return False

#     return True