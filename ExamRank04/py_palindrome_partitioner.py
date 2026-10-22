
# With Recursion
def palindrome(s: str) -> bool:
    return s == s[::-1]


def palindrome_partitioner(s: str) -> int:
    if len(s) <= 1 or palindrome(s):
        return 0

    min_cuts = len(s) - 1

    for i in range(1, len(s)):
        left = s[:i]
        right = s[i:]

        cuts = (
            palindrome_partitioner(left)
            + palindrome_partitioner(right)
            + 1
        )

        min_cuts = min(min_cuts, cuts)

    return min_cuts

print(palindrome_partitioner("aab"))   # 1
print(palindrome_partitioner("aba"))   # 0
print(palindrome_partitioner("abc"))   # 2
print(palindrome_partitioner(""))      # 0
print(palindrome_partitioner("a"))     # 0




# def palindrome(s: str) -> bool:
#     return s == s[::-1]


# def palindrome_partitioner(s: str) -> int:
#     n = len(s)

#     if n <= 1 or palindrome(s):
#         return 0

#     # dp[i] = minimum cuts needed for the first i characters
#     dp = list(range(n + 1))

#     for i in range(1, n + 1):
#         for j in range(i):
#             part = s[j:i]

#             if palindrome(part):
#                 dp[i] = min(dp[i], dp[j] + 1)

#     return dp[n] - 1

# print(palindrome_partitioner("aab"))  # Expected: 1
# print(palindrome_partitioner("aba"))  # Expected: 0
# print(palindrome_partitioner("abc"))  # Expected: 2
# print(palindrome_partitioner(""))  # Expected: 0
# print(palindrome_partitioner("a"))  # Expected: 0
