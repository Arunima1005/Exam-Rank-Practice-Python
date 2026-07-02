from itertools import groupby

if __name__ == "__main__":
    string = input()
    g_group = groupby(string, key = lambda c : c)
    for key, group in g_group:
        print(f"({len(list(group))}, {int(key)})", end = " ")
    print()

# better verison
# from itertools import groupby

# string = input()

# for key, group in groupby(string):
#     count = len(list(group))
#     print((count, int(key)), end=" ")