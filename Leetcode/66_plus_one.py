from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = ""
        for d in digits:
            num = num + str(d)
        digits = list(str(int(num)+1))
        return list(map(int, digits))

# ### better way----------
# class Solution:
#     def plusOne(self, digits: List[int]) -> List[int]:
#         num = "".join(map(str, digits))
#         return list(map(int, str(int(num) + 1)))

n = Solution()
print(n.plusOne([1,2,3]))
