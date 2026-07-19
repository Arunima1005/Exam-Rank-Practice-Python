class Solution:
    def arraySign(self, nums: list[int]) -> int:
        negatives = 1

        for n in nums:
            if n == 0:
                return 0

            if n < 0:
                negatives *= -1