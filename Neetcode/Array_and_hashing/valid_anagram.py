from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        scounter = Counter(s)
        tcounter = Counter(t)
        return scounter == tcounter

s = Solution()
print(s.isAnagram(s = "racecar", t = "carrace"))
print(s.isAnagram(s = "jar", t = "jam"))
print(s.isAnagram(s = "x", t = "x"))

# ## HAsh map
# from collections import Counter

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         return Counter(s) == Counter(t)

# ## Sorting
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         return sorted(s) == sorted(t)

#     ## Array Approach

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False

#         count = [0] * 26

#         for i in range(len(s)):
#             count[ord(s[i]) - ord('a')] += 1
#             count[ord(t[i]) - ord('a')] -= 1

#         return all(x == 0 for x in count)