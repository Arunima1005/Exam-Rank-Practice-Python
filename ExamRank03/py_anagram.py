# Problem 13: Valid Anagram
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# Examples:
# s = "anagram", t = "nagaram" → True
# s = "rat", t = "car" → False
# s = "listen", t = "silent" → True


from collections import Counter

def anagram(s1: str, s2: str) -> bool:
    f1 = ""
    f2 = ""
    for s in s1:
        if s.isalpha():
            f1 = f1 + s
    for s in s2:
        if s.isalpha():
            f2 = f2 + s

    return Counter(f1.lower()) == Counter(f2.lower())

print(anagram("listen", "silent"))
print(anagram("Triangle", "Integral"))
print(anagram("Dormitory", "Dirty Room"))
print(anagram("hello", "world"))
print(anagram("", ""))
print(anagram("abc", "abcc"))
# true true true false true false


## another option

# from collections import Counter

# def anagram(s1: str, s2: str) -> bool:
#     s1 = "".join(c.lower() for c in s1 if c.isalpha())
#     s2 = "".join(c.lower() for c in s2 if c.isalpha())

#     return Counter(s1) == Counter(s2)




### with Sort

# def anagram(s1: str, s2: str) -> bool:
#     s1 = sorted(c.lower() for c in s1 if c.isalpha())
#     s2 = sorted(c.lower() for c in s2 if c.isalpha())

#     return s1 == s2


# ## Manual without build -in function

# def anagram(s1: str, s2: str) -> bool:
#     counts = {}

#     for c in s1.lower():
#         if c.isalpha():
#             counts[c] = counts.get(c, 0) + 1

#     for c in s2.lower():
#         if c.isalpha():
#             counts[c] = counts.get(c, 0) - 1

#     return all(v == 0 for v in counts.values())