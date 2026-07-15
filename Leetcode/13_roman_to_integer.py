class Solution:
    def romanToInt(self, s: str) -> int:
        roman ={
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        num = 0
        n = []
        for c in s:
            n.append(roman[c])
        for i in range(len(n)):
            # print(num)
            if i < len(n)-1 and n[i] >= n[i+1]:
                num = num + n[i]
            else:
                num = num - n[i]
        return num
            

s = Solution()
print(s.romanToInt("MCMXCIV"))
print(s.romanToInt("LVIII"))
print(s.romanToInt("III"))

# ##pydantic way
# class Solution:
#     def romanToInt(self, s: str) -> int:
#         roman = {
#             "I": 1,
#             "V": 5,
#             "X": 10,
#             "L": 50,
#             "C": 100,
#             "D": 500,
#             "M": 1000,
#         }

#         total = 0

#         for current, nxt in zip(s, s[1:]):
#             if roman[current] < roman[nxt]:
#                 total -= roman[current]
#             else:
#                 total += roman[current]

#         return total + roman[s[-1]]



# #### Right to left traverse using reversed string method
# class Solution:
#     def romanToInt(self, s: str) -> int:
#         roman = {
#             "I": 1,
#             "V": 5,
#             "X": 10,
#             "L": 50,
#             "C": 100,
#             "D": 500,
#             "M": 1000,
#         }

#         total = 0
#         previous = 0

#         for c in reversed(s):
#             value = roman[c]

#             if value < previous:
#                 total -= value
#             else:
#                 total += value

#             previous = value

#         return total