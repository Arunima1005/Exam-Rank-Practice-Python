# Problem 16: Sign of the Product of an Array
# Implement a function signFunc(x) that returns:

# 1 if x is positive
# -1 if x is negative
# 0 if x is equal to 0
# You are given an integer array nums. Let product be the product of all values in the array. Return signFunc(product).
# Examples:
# [-1, -2, -3, -4, 3, 2, 1] → 1
# [1, 5, 0, 2, -3] → 0
# [-1, 1, -1, 1, -1] → -1

from functools import reduce

# help(reduce)

def signFunc(x):
    num = reduce(lambda x,y : x * y, x)
    if num == 0:
        return 0
    if num > 0:
        return 1
    return -1


# ### only checking sign
# def signFunc(nums):
#     negatives = 0

#     for n in nums:
#         if n == 0:
#             return 0

#         if n < 0:
#             negatives += 1

#     return -1 if negatives % 2 else 1


def signFunc(nums):
    negatives = 1

    for n in nums:
        if n == 0:
            return 0

        if n < 0:
            negatives *= -1

    return negatives

print(signFunc( [-1, -2, -3, -4, 3, 2, 1] ))
print(signFunc( [1, 5, 0, 2, -3] ))
print(signFunc( [-1, 1, -1, 1, -1] ))
