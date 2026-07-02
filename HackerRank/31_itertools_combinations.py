from itertools import combinations

if __name__ == "__main__":
    string, num = input().split()
    k = int(num)
    string = sorted(string)
    for i in range(1,k+1):
        for p in combinations(sorted(string), i):
            print("".join(p))