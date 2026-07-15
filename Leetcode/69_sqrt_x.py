class Solution:
    def mySqrt(self, x: int) -> int:
        n = 0
        while n * n <= x:
            n += 1
        # print(n)
        return(n -1 )

s = Solution()
print(s.mySqrt(8))



## in build function

# import math

# class Solution:
#     def mySqrt(self, x: int) -> int:
#         return int(math.sqrt(x))