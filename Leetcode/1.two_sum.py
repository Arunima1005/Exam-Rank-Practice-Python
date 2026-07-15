class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                current_sum = nums[i] + nums[j]

                if current_sum == target:
                    return [i, j]
s = Solution()
print(s.twoSum([1, 2, 4, 7, 3], 9))

# ###Enumerate
# class Solution:
#     def twoSum(self, nums: list[int], target: int) -> list[int]:
#         for i, first in enumerate(nums):
#             for j in range(i + 1, len(nums)):
#                 if first + nums[j] == target:
#                     return [i, j]

### O(n)

# class Solution:
#     def twoSum(self, nums: list[int], target: int) -> list[int]:
#         seen = {}

#         for i, num in enumerate(nums):
#             complement = target - num

#             if complement in seen:
#                 return [seen[complement], i]

#             seen[num] = i

# s = Solution()
# print(s.twoSum([1, 2, 4, 7, 3], 9))