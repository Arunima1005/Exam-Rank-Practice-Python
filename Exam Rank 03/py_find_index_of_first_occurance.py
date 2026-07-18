# Problem 12: Find Index of First Occurrence
# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
# Examples:
# haystack = "sadbutsad", needle = "sad" → 0
# haystack = "leetcode", needle = "leeto" → -1
# haystack = "hello", needle = "ll" → 2

def find_index_of_first_occurance(haystack :str, needle: str) -> int:
    for i in range(len(haystack) - len(needle)+ 1):
        if haystack[i: i+len(needle)] == needle:
            return i
    
    return -1


### Using build in function find
# def find_index_of_first_occurance(haystack :str, needle: str) -> int:
#     try:
#         return haystack.index(needle)
#     except ValueError:
#         return -1


print(find_index_of_first_occurance(haystack = "sadbutsad", needle = "sad"))
print(find_index_of_first_occurance( haystack = "leetcode", needle = "leeto"))
print(find_index_of_first_occurance(haystack = "hello", needle = "ll"))