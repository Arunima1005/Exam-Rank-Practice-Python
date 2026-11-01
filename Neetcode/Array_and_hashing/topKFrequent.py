from collections import Counter

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        c = Counter(nums)
        result = []

        for _ in range(k):
            max = sorted(c.values(), reverse=True)
            # print(f"max = {max}")
            for n, count in c.items():
                if max[0] == count:
                    result.append(n)                
                    c[n] = 0
                    break              
        return result

s = Solution()
print(s.topKFrequent(nums = [1,2,2,3,3,3], k = 2))
print(s.topKFrequent(nums = [7,7], k = 1))
print(s.topKFrequent(nums = [1,2], k = 2))



### Better Approach

# from collections import Counter

# class Solution:
#     def topKFrequent(self, nums: list[int], k: int) -> list[int]:
#         c = Counter(nums)

#         result = sorted(c, key=c.get, reverse=True)

#         return result[:k]