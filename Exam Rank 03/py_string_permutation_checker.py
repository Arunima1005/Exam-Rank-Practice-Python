def string_permutation_checker(s1: str, s2: str) -> bool:
    return sorted(s1) == sorted(s2)   


# from collections import Counter
# def string_permutation_checker(s1: str, s2: str) -> bool:
#     return Counter(s1) == Counter(s2)


print(string_permutation_checker("abc", "bca"))
print(string_permutation_checker("abc", "def"))
print(string_permutation_checker("listen", "silent"))
print(string_permutation_checker("hello", "bello"))
print(string_permutation_checker("", ""))
print(string_permutation_checker("a", ""))
print(string_permutation_checker("Abc", "abc"))
print(string_permutation_checker("a gentleman","elegant man"))
#true false true false true false false true
