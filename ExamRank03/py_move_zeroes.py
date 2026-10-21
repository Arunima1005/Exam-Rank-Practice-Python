# Problem 14: Move Zeroes
# Given an integer array nums, move all 0's to the end 
# while maintaining the relative order of the non-zero elements. Note: You must do this in-place without making a copy of the array.
# Examples:
# [0, 1, 0, 3, 12] → [1, 3, 12, 0, 0]
# [0] → [0]
# [1, 2, 3] → [1, 2, 3]

def moveZeroes(nums) -> None:
    new = [n for n in nums if n!= 0]
    for _ in range(len(nums) - len(new)):
        new.append(0)
    #result.extend([0] * (len(nums) - len(result)))
    nums[:] = new
    print(nums)
    

moveZeroes([0, 1, 0, 3, 12])
moveZeroes([0])
moveZeroes([1, 2, 3])


# ## NO extra list making solution -- two pointer concept

# def moveZeroes(nums):
#     left = 0

#     for right in range(len(nums)):
#         if nums[right] != 0:
#             nums[left], nums[right] = nums[right], nums[left]
#             left += 1
#     print(nums)
# moveZeroes([0, 1, 0, 3, 12])
# moveZeroes([0])
# moveZeroes([1, 2, 3])
