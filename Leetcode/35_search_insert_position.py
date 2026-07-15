# from typing import List
# class Solution:
#     def searchInsert(self, nums: List[int], target: int) -> int:
#         for i in range(len(nums)):
#             if nums[i] == target:
#                 return i
#             if nums[i] > target:
#                 return i
#             # else:
#             #     return i+1
#         return i+1
    
# better approch
from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i, num in enumerate(nums):
            if num >= target:
                return i

        return len(nums)
    

# #### Binary Search --------Nice Approach nlog n
# class Solution:
#     def searchInsert(self, nums: List[int], target: int) -> int:
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

#         return left
s = Solution()
print(s.searchInsert([1,3,5,6],5))
print(s.searchInsert([1,3,5,6],2))
print(s.searchInsert([1,3,5,6],7))
        