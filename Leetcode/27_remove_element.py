from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nlist = []
        for n in nums:
            if n != val:
                nlist.append(n)
        # for i in range(len(nlist)):
        #     nums[i] = nlist[i]
        nums = nlist[:]
        # print(nums)
        return len(nums)
s = Solution()
print(s.removeElement([3,2,2,3], 3))