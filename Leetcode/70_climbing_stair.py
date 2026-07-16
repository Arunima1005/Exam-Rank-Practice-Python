class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        return self.climbStairs(n-1) + self.climbStairs(n-2)
    

s = Solution()
print(s.climbStairs(3))



#### Memorize concept -- good otherwise time limit croosed for recursion

# class Solution:
#     def climbStairs(self, n: int) -> int:
#         memo = {}

#         def climb(n: int) -> int:
#             if n <= 2:
#                 return n

#             if n not in memo:
#                 memo[n] = climb(n - 1) + climb(n - 2)

#             return memo[n]

#         return climb(n)