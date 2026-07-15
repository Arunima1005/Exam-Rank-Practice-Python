

class Solution:
    # 
    def isValid(self, s: str) -> bool:       
        open_parenthesis = ["(", "{", "["]
        close_parenthesis = [")", "}", "]"]
        close=[]
        for i in range(len(s)):
            if s[i] in open_parenthesis:
                # print(f" if {s[i]}")
                j = open_parenthesis.index(s[i])
                close.insert(0, close_parenthesis[j])
            elif s[i] in close_parenthesis and len(close) > 0 and close[0]==s[i]:
                # print(f" elif {s[i]}")
                close.pop(0)
            else:
                # print(f" else {s[i]}")
                return False
        return len(close) == 0

# ####another way of my program...
# class Solution:
#     def isValid(self, s: str) -> bool:
#         open_parenthesis = ["(", "{", "["]
#         close_parenthesis = [")", "}", "]"]

#         close = []

#         for char in s:
#             if char in open_parenthesis:
#                 j = open_parenthesis.index(char)
#                 close.append(close_parenthesis[j])

#             elif char in close_parenthesis and close and close[-1] == char:
#                 close.pop()

#             else:
#                 return False

#         return len(close) == 0


# ## with dictionary
# class Solution:
#     def isValid(self, s: str) -> bool:
#         pairs = {
#             "(": ")",
#             "{": "}",
#             "[": "]"
#         }

#         stack = []

#         for char in s:
#             if char in pairs:
#                 stack.append(pairs[char])

#             elif stack and stack[-1] == char:
#                 stack.pop()

#             else:
#                 return False

#         return not stack




s = Solution()
print(s.isValid("()"))
print(s.isValid("()[]{}"))
print(s.isValid("(]"))
print(s.isValid("([])"))
print(s.isValid("([)]"))
