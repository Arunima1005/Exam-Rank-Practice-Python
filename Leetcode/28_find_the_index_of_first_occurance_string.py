class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        for i in range(len(haystack) - len(needle) + 1):

            for j in range(len(needle)):
                if haystack[i + j] != needle[j]:
                    break
            else:
                return i

        return -1


### using slicing ---- best option
# 
# class Solution:
#     def strStr(self, haystack: str, needle: str) -> int:

#         for i in range(len(haystack) - len(needle) + 1):
#             if haystack[i:i+len(needle)] == needle:
#                 return i

#         return -1 

        ### in  build function ------------------
        # return haystack.find(needle)
s = Solution()
print(s.strStr("leetcode", "code"))
print(s.strStr("sadbutsad", "sad"))
print(s.strStr("leetcode", "ddde"))