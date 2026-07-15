class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        n = x
        num = 0
        while n > 0:
            num = num * 10 + n % 10
            n = n//10
        return x == num
# with string reverse
# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         s = str(x)
#         return s == s[::-1]


s = Solution()
print(s.isPalindrome(-121))
print(s.isPalindrome(121))
print(s.isPalindrome(567))