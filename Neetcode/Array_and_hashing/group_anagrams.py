from collections import defaultdict
class Solution:

    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        done = defaultdict(list)

        for s in strs:
            new = "".join(sorted(s))
            done[new].append(s)
        return list(done.values())

s = Solution()
print(s.groupAnagrams(["act","pots","tops","cat","stop","hat"]))
print(s.groupAnagrams(["X"]))
print(s.groupAnagrams([""]))
print(s.groupAnagrams(["",""]))
print(s.groupAnagrams(["act","pots","tops","cat","stop","hat", "cat"]))

# ## Not good approach ----:(
# from collections import Counter

# class Solution:

#     def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
#         final: list[str] = []

#         done = []

#         for i in range(len(strs)):
#             s: dict[str, int] = Counter(strs[i])
#             result: list[str] = []
#             found = False
#             if i not in done:
#                 found = True
#                 result.append(strs[i])
#                 done.append(i)    
#             for j in range(len(strs)):                 
#                 if (s == Counter(strs[j]) and j not in done): 
#                     found = True            
#                     result.append(strs[j])
#                     done.append(j)
#             if found:
#                 final.append(result)
#         return final
