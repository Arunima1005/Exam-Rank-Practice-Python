# **Python Cheat Sheet**

## **Variables are dynamically typed**
```
n = 0
print("n = ", n)
```
Result 
```
n = 0
```
Another type
```
n = "abc"
print("n = ", n)
```
Result
```
n = abc
```

## **Multiple assignment**

```
n, m = 0, "abc"
```

## **Increment**
```
n = n + 1   # good
n += 1      # good
n ++        # bad
```

## **None is null (absence of value)**
```
n = 4
n = None
print("n = ", n)
```
Result:
```
n = None
```
## **If statements don't need paraentheses or curly braces**
```
n = 1
if n > 2
    n -= 1
elif n == 2:
    n *= 2
else:
    n = 2
```
## **Parantheses needed for multi-line conditions.**
### and = &&
### or = ||
```
n, m = 1, 2
if ((n > 2) and
    n != m) or (n == m):
    n += 1
```
## **While loop**
```
n = 0
while n < 5:
    print(n)
    n += 1
```
Result:
```
0
1
2
3
4
```

## **For loop**
### Looping from i = 0 to i = 4
```
for i in range(5):
    print(i)
```
Result:
```
0
1
2
3
4
```
### Looping from i = 2 to i = 5
```
for i in range(2,6):
    print(i)
```
Result:
```
2
3
4
5
```
### Looping from i = 5 to i = 2
```
for i in range(5, 1, -1):
    print(i)
```
Result:
```
5
4
3
2
```
## **Division**
```
# Division is decimal by default
print(5/2)          # 2.5

# Double slash rounds down
print(5 // 2)       # 2

# Negative numbers will round down
print(-3 / 2)       # -2

# A workaround for ounding towards zero is to use decimal division and then convert to int.
print(int(-3 / 2))  # -1
```
## **Modulo**
```
print(10 % 3)       # 1
print(-10 % 3)      # 2 (Not similar like other languages)

# To be consistent with other languages modulo 
import math
print(math.fmod(-10, 3))    # -1.0
```
## **Math Helper**
```
import math
print(math.floor(3 / 2)) 
print(math.ceil(3 / 2)) 
print(math.sqrt(2))
print(math.pow(2,3))
```
### Max / Min Int
```
float("inf")
float("-inf")
```
### Python numbers are infinite so they never overflow
```
import math
print(math.pow(2, 200)) # dont overflow

# But still less than infinity
print(math.pow(2, 200) < float("inf"))  #True
```
## Arrays (called lists in python)
```
arr = [1, 2, 3]
print(arr)      # [1, 2, 3]

# can be used as stack
arr.append(4)
arr.append(5)
print(arr)      #[1, 2, 3, 4, 5]

arr.pop()
print(arr)      #[1, 2, 3, 4]

arr.insert(1, 7) #Big O
print(arr)      #[1, 7, 2, 3, 4]

arr[0] = 0
arr[3] = 0
print(arr)      #[0, 7, 2, 0, 4]
```
### Initialize arr of size n with default value of 1
```
n = 5
arr = [1] * n
print(arr)          # [1, 1, 1, 1, 1]
print(len(arr))     # 5
```
### Careful: -1 is not out of bounds, it's the last value
```
arr = [1, 2, 3]
print(arr[-1])             # 3 (last value)

# Indexing -2 is the second to last value ......
print(arr[-2])
```
### Sublists (aka slicing)
```
arr = [1, 2, 3, 4]
print(arr[1:3])         # [2, 3]

#Similar to for-loop ranges, last index is non-inclusive
print(arr[0:4])         #[1, 2, 3, 4]
```
### Unpacking
```
a, b, c = [1, 2, 3]
print(a, b, c)          # 1 2 3
```
### Loop through arrays
```
nums = [1, 2, 3]
```
```
# Using index
for i in range(len(nums)):
    print(nums[i])
```
Result:
```
1
2
3
```
```
# Without index
for n in nums
    print(n)
```
Result:
```
1
2
3
```
```
# With index and value (if you need both balue and index)
for i, n in enumerate(nums):
    print(i, n)
```
Result:
```
0 1
1 2
2 3
```
### Loop through multiple arrays simultaneously with unpacking
```
nums1 = [1, 3, 5]
nums2 = [2, 4, 6]
for n1, n2 in zip(num1, num2):
    print(n1, n2)
```
Result:
```
1 2
3 4
5 6
```
### Reverse
```
nums = [1, 2, 3]
nums.reverse()
print(nums)         #[3, 2, 1]
```
### Sorting
```
arr = [5, 4, 7, 3, 8]
arr.sort()
print(arr)         #[3, 4, 5, 7, 8]

#reverse order
arr.sort(reverse=True)
print(arr)          #[8, 7, 5, 4, 3]

#order list of strings
arr = ["bob", "alice", "jane", "doe"]
arr.sort()
print(arr)          #['alice', 'bob', 'doe', 'jane']

#Custom sort (by length of string)
arr.sort(key=lambda x: len(x))
```
### List Comprehension
```
arr = [i for i in range(5)]
print(arr)          #[0, 1, 2, 3, 4]

arr = [i+1 for i in range(5)]
print(arr)          #[0, 2, 4, 6, 8]
```
### 2-D list
```
arr = [[0] * 4 for i in range(4)]
```
## **String**
```
s = "abc"
print(s[0:2])       #ab

# They are immutable
s[0] = "A"      # we cannot modify value

# This create a new string
s += "def"
print(s)        #abcdef

# Valid numeric strings can be converted
print(int("123") + int("123"))          # 246

# Numbers can be converted to strings
print(str(123) + str(123))              # 123123

# ASCII value of a char
print(ord("a"))         # 97
print(ord("b"))         # 98

## Combine a list of strings (with  an empty string delimitor)
string = ["ab", "cd", "ef"]
print("".join(strings))     # abcdef
```
## **Queue (double ended queue)**
```
from collections import deque

queue = deque()
queue.append(1)
queue.append(2)
print(queue)        # deque([1, 2])

queue.popleft()
print(queue)        # deque([2])

queue.appendleft(1)
print(queue)        # deque([1, 2])

queue.pop()
print(queue)        # deque([1])
```
## **HastSet**
```
mySet = set()
mySet.add(1)
mySet.add(2)
print(mySet)        # {1, 2}

print(len(mySet))   # 2

print(1 in mySet)   # True
print(3 in mySet)   # False

mySet.remove(2)
print(2 in mySet)   # False

# list ti set
print(set([1, 2, 3]))

# Set comprehension
mySet = { i for i in range(5)}
print(mySet)        # {0, 1, 2, 3, 4}
```

## **HastMap (aka Dict)**
```
myMap = {}
myMap["alice"] = 88
myMap["bob"] = 77
print(myMap)            # {'alice': 88, 'bob': 77}
print(len(myMap))       # 2

myMap["alice"] = 80
print(myMap)            # {'alice': 80, 'bob': 77}

print("alice" in myMap)     # True
myMap.pop("alice")
print("alice" in myMap)     # False

myMap = {"alice": 90, "bob": 70}
print(myMap)            #  {"alice": 90, "bob": 70}

# Dict comprehension
myMap = {i: 2*i for i in rang(3)}   
print(myMap)             # {0: 0, 1: 2, 2: 4}

myMap = {"alice": 90, "bob": 70}
for key in myMap:
    print(key, myMap[key])      # alice 90
                                # bob 70

for val in myMap.values():
    print(val)      # 90
                    # 70

for key, val in myMap.items():
    print(key, val)             # alice 90
                                # bob 70
```
## **Tuple (immutable)**
```
tup = (1, 2, 3)
print(tup)
print(tup[0])
print(tup[-1])

# can't modify
tup[0] = 0

# can be used as key for hash map/set
myMap = {(1, 2): 3}
print(myMap[(1, 2)])

mySet = set()
mySet.add((1, 2))

print((1, 2) in mySet)

# Lists can't be keys
myMap[[3, 4]] = 5
```
## **Heaps**
```
import headq

minHeap = []
headq.heappush(minHeap, 3)
headq.heappush(minHeap, 2)
headq.heappush(minHeap, 4)

# Min is always at index 0
print(minHeap[0])           # 2

while len(minHeap):
    print(headq.heappop(minHeap))       # 2 3 4

# No max heaps by default, work around is to use min heap and multiply by -1 when push and pop
maxHeap = []
heapq.headpush(maxHeap, -3)
heapq.headpush(maxHeap, -2)
heapq.headpush(maxHeap, -4)

# Max is always at index 0
print(-1 * maxHeap[0])      # 4

while len(maxHeap):
    print(-1 * headq.heappop(maxHeap))       # 4 3 2

# Build heap from initial values
arr = [2, 1, 8, 4, 5]
heapq.heapify(arr)
while arr:
    print(heapq.heappop(arr))   # 1 2 4 5 8
```
# **Functions**
```
def myFunc(n, m):
    return n * m

print(myFunc(3, 4))         # 12

# Nested functions have access to outer variables
def outer(a, b):
    c = "c"

    def inner():
        return a + b + c
    return inner()

print(outer("a", "b"))          # abc
```