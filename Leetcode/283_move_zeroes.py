from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        result = []
        for n in nums:
            if n != 0:
                result.append(n)
                
        for _ in range(length - len(result)):
            result.append(0)

        nums[:] = result
        # print(result)

s = Solution()
s.moveZeroes([0,0,1])


## Better option from my one

# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         result = [n for n in nums if n != 0]
#         result.extend([0] * (len(nums) - len(result)))
#         nums[:] = result


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