class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        result = [1] * len(nums)
        left = 1
        right = 1
        for i in range(len(nums)):
            result[i] = left
            left *= int(nums[i])

        for i in range(len(nums)-1, -1, -1):
            result[i] *= right
            right *= int(nums[i])
        return result


s = Solution()
print(s.productExceptSelf(nums = [1,2,4,6]))
print(s.productExceptSelf(nums = [-1,0,1,2,3]))

## my approach - not good:(
# from functools import reduce

# class Solution:
#     def productExceptSelf(self, nums: list[int]) -> list[int]:
#         result = []
#         for i in range(len(nums)):
#             new_list = nums[:i] + nums[i+1:]
#             new = reduce(lambda x, y: x*y, new_list)
#             result.append(new)
#         return result