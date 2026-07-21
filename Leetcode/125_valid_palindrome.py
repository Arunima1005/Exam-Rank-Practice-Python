class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = [n.lower() for n in s if n.isalnum()]
        print(st)
        return st == st[::-1]
    
s=Solution()
print(s.isPalindrome("0P"))