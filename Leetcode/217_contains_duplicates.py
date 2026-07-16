from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for n in range(len(nums)):
            if nums[n] in nums[n+1:]:
                return True
        return False
    
s = Solution()
print(s.containsDuplicate([1,2,3,1]))
print(s.containsDuplicate([1,2,3,4]))

# ### Using enumerate
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         for i, num in enumerate(nums):
#             if num in nums[i + 1:]:
#                 return True
#         return False


## Using SET---best approach
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False
