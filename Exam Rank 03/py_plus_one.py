# Problem 15: Plus One
# You are given a large integer represented as an integer array digits, 
# where each digits[i] is the ith digit of the integer. 
# The digits are ordered from most significant to least significant. 
# Increment the large integer by one and return the resulting array of digits.
# Examples:
# [1, 2, 3] → [1, 2, 4]
# [4, 3, 2, 1] → [4, 3, 2, 2]
# [9] → [1, 0]
# [9, 9, 9] → [1, 0, 0, 0]

# def plus_one(num :list[int]):
#     result = 0
#     for n in num:
#         result = result * 10 + n
#     return list(map(int, str(result+1)))

def plus_one(num :list[int]):
    result = "".join(map(str, num))
    return list(map(int, str(int(result) + 1)))

print(plus_one([1, 2, 3]))
print(plus_one([4, 3, 2, 1]))
print(plus_one([9]))
print(plus_one([9, 9, 9]))