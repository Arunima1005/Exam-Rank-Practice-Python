class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        n = set(nums)
        return len(n)!=len(nums)

s = Solution()
print(s.hasDuplicate([1, 2, 3, 3]))
print(s.hasDuplicate([1, 2, 3, 4]))


## AI - It returns immediately when it encounters a duplicate (early termination), potentially saving work.

# class Solution:
#     def hasDuplicate(self, nums: list[int]) -> bool:
#         seen = set()

#         for num in nums:
#             if num in seen:
#                 return True
#             seen.add(num)

#         return False