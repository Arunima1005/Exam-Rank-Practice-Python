class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        return all(nums[i+1] >= nums[i] for i in range(len(nums)-1)) \
            or all(nums[i+1] <= nums[i] for i in range(len(nums)-1))