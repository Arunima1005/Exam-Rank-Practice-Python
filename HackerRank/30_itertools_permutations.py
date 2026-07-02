from itertools import permutations

if __name__ == "__main__":
    string, num = input().split()
    lst = []
    for p in permutations(string, int(num)):
        lst.append("".join(p))
    lst.sort()
    for l in lst:
        print(l)


# Better Way

# from itertools import permutations

# string, k = input().split()

# for perm in permutations(sorted(string), int(k)):
#     print("".join(perm))