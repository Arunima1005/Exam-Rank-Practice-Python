# Problem 18: Monotonic Array
# An array is monotonic if it is either monotone increasing or monotone decreasing.
# An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]

# An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j]
# Given an integer array nums, return true if the array is monotonic, or false otherwise.
# Examples:
# [1, 2, 2, 3] → True (increasing)
# [6, 5, 4, 4] → True (decreasing)
# [1, 3, 2] → False (neither)
# [3, 3, 3, 3] → True (both increasing and decreasing)

def monotonic_check_array(nums):
    increasing = True
    decreasing = True

    for a, b in zip(nums, nums[1:]):
        if a > b:
            increasing = False
        if a < b:
            decreasing = False

    return increasing or decreasing

print(monotonic_check_array([1, 2, 2, 3])) 
print(monotonic_check_array([6, 5, 4, 4]))  
print(monotonic_check_array([1, 3, 2]))  
print(monotonic_check_array([3, 3, 3, 3]))    


# def monotonic_check_array(nums):
#     if len(nums) < 2:
#         return True

#     direction = 0

#     for a, b in zip(nums, nums[1:]):
#         if a < b:
#             direction = 1
#             break
#         elif a > b:
#             direction = -1
#             break

#     if direction == 1:
#         return all(a <= b for a, b in zip(nums, nums[1:]))

#     if direction == -1:
#         return all(a >= b for a, b in zip(nums, nums[1:]))

#     return True
# print(monotonic_check_array([1, 2, 2, 3])) 
# print(monotonic_check_array([6, 5, 4, 4]))  
# print(monotonic_check_array([1, 3, 2]))  
# print(monotonic_check_array([3, 3, 3, 3]))    


##pythonic way

# def isMonotonic(nums: list[int]) -> bool:
#     return all(nums[i] <= nums[i+1] for i in range(len(nums)-1)) or \
#            all(nums[i] >= nums[i+1] for i in range(len(nums)-1))