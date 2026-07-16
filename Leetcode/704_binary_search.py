from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for index, n in enumerate(nums):
           if n == target:
               return index
        return -1
    
s = Solution()
print(s.search(nums = [-1,0,3,5,9,12], target = 9))

### Binary search

# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         left = 0
#         right = len(nums) - 1

#         while left <= right:
#             mid = (left + right) // 2

#             if nums[mid] == target:
#                 return mid

#             if nums[mid] < target:
#                 left = mid + 1
#             else:
#                 right = mid - 1

#         return -1