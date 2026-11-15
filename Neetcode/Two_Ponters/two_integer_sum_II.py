class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left = 0
        right = len(numbers) - 1
        while left < right:
            total = numbers[left] + numbers[right]

            if total == target:
                return [left+1, right+1]
            elif total < target:
                left += 1
            else:
                right -= 1

s = Solution()
print(s.twoSum(numbers = [1,2,3,4], target = 3))
print(s.twoSum(numbers=[-1,0], target=-1))
print(s.twoSum(numbers=[-5,-3,0,2,4,6,8], target=5))



# print(s.twoSum())


## MY Logic

# class Solution:
#     def twoSum(self, numbers: list[int], target: int) -> list[int]:
#         for i in range(len(numbers)):
#             for j in range(len(numbers)):
#                 if i != j and numbers[i] + numbers[j] == target:
#                     return [i+1,j+1]
