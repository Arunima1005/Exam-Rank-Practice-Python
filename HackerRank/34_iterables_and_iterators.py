from itertools import combinations

if __name__ == "__main__":
    n = int(input())
    string = input().split()
    k = int(input())
    com = list(combinations(string, k))  
    count = 0
    for p in com:
        if 'a' in p:
            count += 1
    print(count/len(com))


# #better option
# from itertools import combinations

# com = list(combinations(string, k))

# count = sum('a' in p for p in com)

# print(count / len(com))