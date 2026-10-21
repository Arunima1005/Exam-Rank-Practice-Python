# Problem 19: Repeated Substring Pattern
# Given a string s, check if it can be constructed by taking a substring of it 
# and appending multiple copies of the substring together.
# Examples:
# "abab" → True (substring "ab" repeated twice)
# "aba" → False
# "abcabcabcabc" → True (substring "abc" repeated 4 times)
# "aaa" → True (substring "a" repeated 3 times)

# def repeatedSubstringPattern(s: str) -> bool:
#     flag = 0
#     for j in range(len(s)):
#         for i in range(1, len(s)):
        
#             print(i+j, i+i+j)
#             # i+j
#             print(s[j+i:i+j], s[i+j+1: i+j+i+1])

#             # if s[j:i+j] == s[i+j : i+j+j]:
#             #     flag = True


#     return flag

# def repeatedSubstringPattern(s):
#     n = len(s)

#     for length in range(1, n // 2 + 1):
#         if n % length == 0:
#             pattern = s[:length]
#             if pattern * (n // length) == s:
#                 return True

#     return False



def repeatedSubstringPattern(s):
    print((s + s)[1:-1])
    return s in (s + s)[1:-1]

print(repeatedSubstringPattern("dabcdabcd"))
print(repeatedSubstringPattern("abababababab"))
# print(repeatedSubstringPattern("aba"))
# print(repeatedSubstringPattern("abcabcabcabc"))
# print(repeatedSubstringPattern("aaa"))