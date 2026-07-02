from itertools import combinations_with_replacement

if __name__ == "__main__":
    string, num = input().split()
    string = sorted(string)
    k = int(num)

    for p in combinations_with_replacement(string, k):
        print("".join(p))