class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = ""
        for p in s:
            if p.isalnum():
                result += p.lower()
        return result == result[::-1] 

s = Solution()
print(s.isPalindrome(s = "Was it a car or a cat I saw?"))
print(s.isPalindrome(s = "tab a cat"))
# s.isPalindrome(s = "abc?vv")