def hidenp(small: str, big: str) -> bool:
    count = 0
    index = 0
    for c in small:
        for i in range(index, len(big)):
            # print(c, big[i])
            if c == big[i]:
                count += 1
                break
        index = i + 1

    # print(count)
    if count == len(small):
        return True
    return False


print(hidenp("abc", "a1b2c3"))
print(hidenp("ace", "abcde"))
print(hidenp("sing","subsequence testing"))
print(hidenp("", "abc"))
print(hidenp("aec", "abcde"))
print(hidenp("abc", "ab"))
print(hidenp("aaaa", "aaa"))


# ##pythonic way-----best option
# def hidenp(small: str, big: str) -> bool:
#     """
#     Checks if the string 'small' is a subsequence of 'big'.
#     A subsequence means all characters of 'small' appear in 'big'
#     in the same order, but not necessarily consecutively.
#     """
#     it = iter(big)
#     return all(c in it for c in small)



# ### another
# def hidenp(small: str, big: str) -> bool:
#     count = 0
#     index = 0

#     for c in small:
#         for i in range(index, len(big)):
#             if c == big[i]:
#                 count += 1
#                 break
#         index = i + 1

#     return count == len(small)




# def hidenp(small: str, big: str) -> bool:
#     i = 0
#     j = 0

#     while i < len(small) and j < len(big):
#         if small[i] == big[j]:
#             i += 1
#         j += 1

#     return i == len(small)