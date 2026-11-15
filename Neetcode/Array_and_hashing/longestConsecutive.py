class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        lst = sorted(set(nums))
        if len(lst) == 0:
            return 0
        current = 1
        longest= 1
        # print(lst)
        for j in range(len(lst)):            
            if lst[j] == lst[j - 1] + 1:
                current += 1
            else:
                current = 1
            if longest < current:
                longest = current
                
        return longest



## - My Logic
# class Solution:
#     def longestConsecutive(self, nums: list[int]) -> int:
#         lst = sorted(set(nums))
#         if len(lst) == 0:
#             return 0
#         longest = 1
#         print(lst)
#         for j in range(len(lst)):
#             current = 1
#             for i in range(j, len(lst)):        
#                 if i+1 < len(lst) and lst[i] + 1 == lst[i+1]:
#                     current += 1
#                 else:
#                     if longest < current:
#                         longest = current
#                     break
#         return longest

s=Solution()
print(s.longestConsecutive(nums = [2,20,4,10,3,4,5]))
print(s.longestConsecutive(nums = [0,3,7,2,5,8,4,6,0,1]))
print(s.longestConsecutive(nums = [1,0,1,2]))
print(s.longestConsecutive(nums = [100,4,200,1,3,2]))
print(s.longestConsecutive(nums = []))
print(s.longestConsecutive(nums = [100,4,200,1,3,2, 201, 202, 203, 444,204, 205, 205, 206]))
        