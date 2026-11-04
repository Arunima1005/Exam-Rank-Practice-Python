class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums.sort()
        result = {}
        i = 0
        while i < len(nums) :
            n = nums[i]
            # print(n)
            j = 0
            while j < len(nums):
                if n +1 == nums[j] and i != j:
                    result[n] = nums[j]
                    # print(result)
                    break
                j += 1
            i += 1
        return result

s=Solution()
print(s.longestConsecutive(nums = [2,20,4,10,3,4,5]))
        