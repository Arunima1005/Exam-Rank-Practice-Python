from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nlist = []
        for n in nums:
            if n not in nlist:
                nlist.append(n)
        
        # for i in range(len(nlist)):
        #     nums[i] = nlist[i]
        nums[:] = nlist #good approach than for loop
        # print(nums)
        return len(nlist)
    
s = Solution()
print(s.removeDuplicates([1,1,2]))