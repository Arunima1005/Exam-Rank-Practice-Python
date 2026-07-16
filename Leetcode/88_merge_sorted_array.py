from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        merge_list = nums1[:m]
        for i in range(n):
            merge_list.append(nums2[i])
    
        merge_list.sort()
        for p in range(len(merge_list)):
            nums1[p]=merge_list[p]
        # print(merge_list)
        # nums1 = merge_list
        print(nums1)

s = Solution()
s.merge([1,2,3,0,0,0], 3, [2,5,6], 3)

## merge_list = nums1[:m] + nums2

#OR

# merge_list = nums1[:m]
# merge_list.extend(nums2)

### Nice way to copy from one list to existing list
# merge_list.sort()

# nums1[:m+n] = merge_list



# class Solution:
#     def merge(self, nums1, m, nums2, n):
#         merged = nums1[:m]
#         merged.extend(nums2)
#         merged.sort()
#         nums1[:m+n] = merged