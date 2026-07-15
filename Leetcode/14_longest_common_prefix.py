from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        
        length = min(len(s) for s in strs)
        prefix_string =""
        for i in range(length):
            for first, second in zip(strs, strs[1:]):
                # print(first, second)
                if first[i] == second[i]:
                    common = True
                else:
                    common = False
                    break
            if common == True:
                prefix_string= prefix_string + first[i]
            else:
                break  
        return prefix_string



# prefix = []
# ...
# prefix.append(first[i])

# return "".join(prefix)



# ###### Another better way of my version
# from typing import List

# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         if len(strs) == 1:
#             return strs[0]

#         length = min(len(s) for s in strs)
#         prefix = ""

#         for i in range(length):
#             for first, second in zip(strs, strs[1:]):
#                 if first[i] != second[i]:
#                     return prefix

#             prefix += strs[0][i]

#         return prefix


# ## Nice way of writing with startwith function
# from typing import List
# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         prefix = strs[0]

#         for word in strs[1:]:
#             while not word.startswith(prefix):
#                 prefix = prefix[:-1]

#         return prefix

s = Solution()
print(s.longestCommonPrefix(["flower","flow","flight"]))
print(s.longestCommonPrefix(["dog","racecar","car"]))
print(s.longestCommonPrefix(["cir","car"]))
print(s.longestCommonPrefix(["dog"]))
