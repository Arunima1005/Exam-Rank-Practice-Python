

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []

        for i in range(len(nums)):

            # Skip duplicate fixed numbers
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])

                    left += 1
                    right -= 1

                    # Skip duplicate left values
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    # Skip duplicate right values
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif total < 0:
                    left += 1

                else:
                    right -= 1

        return result




################## My logic
# class Solution:
#     def threeSum(self, nums: list[int]) -> list[list[int]]:
#         result = []
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 for k in range(j+1, len(nums)):
#                     if nums[i] + nums[j] + nums[k] == 0:
#                         num = sorted([nums[i],nums[j],nums[k]])
#                         if num not in result:
#                             result.append(num)
#         return result


# class Solution:
#     def threeSum(self, nums: list[int]) -> list[list[int]]:
#         res = set()
#         nums.sort()
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 for k in range(j + 1, len(nums)):
#                     if nums[i] + nums[j] + nums[k] == 0:
#                         tmp = [nums[i], nums[j], nums[k]]
#                         res.add(tuple(tmp))
#         return [list(i) for i in res]



s = Solution()
print(s.threeSum(nums = [-1,0,1,2,-1,-4]))
print(s.threeSum(nums = [0,1,1]))
print(s.threeSum(nums = [0,0,0]))