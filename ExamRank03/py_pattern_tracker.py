def pattern_tracker(text: str) -> int:
    count = 0
    for s1, s2 in zip(text,text[1:]):
        if s2.isdigit() and s1.isdigit() and int(s2) == int(s1)+1:
            
            count += 1
    return count


print(pattern_tracker("123"))
print(pattern_tracker("12a34"))
print(pattern_tracker("987654321"))
print(pattern_tracker("01234567"))
print(pattern_tracker("abc"))
print(pattern_tracker("1a2b3c4"))
print(pattern_tracker("112233"))
pattern_tracker("01234567")


## Using Ord in build function

# def pattern_tracker(text: str) -> int:
#     count = 0
#     for a, b in zip(text, text[1:]):
#         if a.isdigit() and b.isdigit() and ord(b) == ord(a) + 1:
#             count += 1
#     return count





##without zip --not better option

# def pattern_tracker(text: str) -> int:
#     """
#     Counts the number of valid consecutive digit pairs
#     in a string. A valid pair consists of two adjacent
#     digits where the second digit is exactly one greater
#     than the first. A 9 followed by a 0 is NOT a valid pair.
#     """
#     counter = 0
#     for i in range(len(text) - 1):
#         if (
#             text[i].isdigit() and
#             text[i + 1].isdigit() and
#             (int(text[i]) + 1 == int(text[i + 1]))
#         ):
#             counter += 1
#     return counter