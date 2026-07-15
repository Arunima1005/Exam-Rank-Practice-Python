class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        strs = s.split()
        return len(strs[-1])
    
        # return len(s.split()[-1]) -- one line approach

s = Solution()
print(s.lengthOfLastWord("Hello World"))
print(s.lengthOfLastWord("   fly me   to   the moon  "))
print(s.lengthOfLastWord("luffy is still joyboy"))

# ============Without split function
# class Solution:
#     def lengthOfLastWord(self, s: str) -> int:
#         length = 0
#         i = len(s) - 1

#         while i >= 0 and s[i] == " ":
#             i -= 1

#         while i >= 0 and s[i] != " ":
#             length += 1
#             i -= 1

#         return length