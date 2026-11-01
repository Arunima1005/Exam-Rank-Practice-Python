class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i + 1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
s = Solution()
print(s.twoSum(nums = [3,4,5,6], target = 7))
print(s.twoSum(nums = [4,5,6], target = 10))
print(s.twoSum(nums = [5,5], target = 10))
print(s.twoSum(nums=[2,5,5,11], target=10))

# ## Another approach
# class Solution:
#     def twoSum(self, nums: list[int], target: int) -> list[int]:
#         hashmap = {}

#         for i in range(len(nums)):
#             complement = target - nums[i]

#             if complement in hashmap:
#                 return [hashmap[complement], i]

#             hashmap[nums[i]] = i


