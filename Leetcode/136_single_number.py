from typing import List
from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = Counter(nums)
        # print(result)
        for key,value in result.items():
            if value == 1:
                return key

s = Solution()
print(s.singleNumber([1,0,1]))


# using dict
# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         counts = {}

#         for num in nums:
#             counts[num] = counts.get(num, 0) + 1

#         for key, value in counts.items():
#             if value == 1:
#                 return key