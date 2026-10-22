def palindrome(s: str) -> bool:
    return s == s[::-1]


def palindrome_partitioner(s: str) -> int:
    if palindrome(s) or len(s) <= 1:
        return 0

    result = len(s) - 1
    
    for i in range(1, len(s)):
        left = s[:i]
        right = s[i:]

        cut = (palindrome_partitioner(left) + palindrome_partitioner(right) + 1)

        result = min(result, cut)
    return result

print(palindrome_partitioner("aab"))   # 1
print(palindrome_partitioner("aba"))   # 0
print(palindrome_partitioner("abc"))   # 2
print(palindrome_partitioner(""))      # 0
print(palindrome_partitioner("a"))     # 0
