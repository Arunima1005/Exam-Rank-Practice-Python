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