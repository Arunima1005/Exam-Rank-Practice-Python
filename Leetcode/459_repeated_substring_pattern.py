class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        print((s + s)[1:-1])
        return s in (s + s)[1:-1]
    
s = Solution()
print(s.repeatedSubstringPattern("dabcdabcd"))
print(s.repeatedSubstringPattern("abababababab"))
print(s.repeatedSubstringPattern("aba"))
print(s.repeatedSubstringPattern("abcabcabcabc"))
print(s.repeatedSubstringPattern("aaa"))