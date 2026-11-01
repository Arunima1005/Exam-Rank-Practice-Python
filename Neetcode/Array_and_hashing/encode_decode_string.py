import re

class Solution:

    def encode(self, strs: list[str]) -> str:
        encoded_string = []
        for s in strs:
            new = str(len(s)) + '#' + s
            encoded_string.append(new)

        return "".join(encoded_string)

    def decode(self, s: str) ->list[str]:
        decoded_string = []
        i = 0
        
        while i < len(s):
            index = s.find('#',i)
            l = int(s[i:index])
            decoded_string.append(s[index+1:index + l+1])
            i = index + l + 1

        return decoded_string


s = Solution()
st = s.encode(strs = ["Hello","World"])
print(s.decode(s = st))
st = s.encode(["we","say",":","yes","!@#$%^&*()"])
print(s.decode(st))

## Using - two pointer approach
#  def decode(self, s: str) -> List[str]:
#         result = []
#         i = 0

#         while i < len(s):
#             j = i

#             while s[j] != '#':
#                 j += 1

#             length = int(s[i:j])

#             start = j + 1
#             end = start + length

#             result.append(s[start:end])

#             i = end

#         return result


## Using Regex 

    
    # def decode(self, s: str) ->list[str]:

    #     matches = re.finditer(r"\d+#", s)
    #     result = []

    #     for match in matches:
    #         start = match.start()
    #         end = match.end()
    #         l = int(s[start:end-1])
    #         result.append(s[end:end+l])
    #     return result

