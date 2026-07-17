def inter(s1: str, s2: str) -> str:
    result = []
    for c in s1:
        if c in s2 and c not in result:
            result.append(c)
    return "".join(result)


print(inter("hello", "world"))
print(inter("banana", "band"))
print(inter("abcabc", "bc"))
print(inter("abc", "xyz"))
print(inter("", "abc"))

### not good performance wise as concatenating string....better performance in list
# def inter(s1: str, s2: str) -> str:
#     """
#     Returns a string with the characters that appears
#     in both strings, without repetitions.
#     Characters are added in the order that
#     they appear in the first string.
#     """
#     res: str = ""
#     for c in s1:
#         if c not in res and c in s2:
#             res += c
#     return res


## using set
# def inter(s1: str, s2: str) -> str:
#     result = []
#     chars = set(s2)

#     for c in s1:
#         if c in chars and c not in result:
#             result.append(c)

#     return "".join(result)