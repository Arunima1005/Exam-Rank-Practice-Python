class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                current_sum = nums[i] + nums[j]

                if current_sum == target:
                    return [i, j]


s = Solution()
print(s.twoSum([1, 2, 4, 7, 3], 9))
