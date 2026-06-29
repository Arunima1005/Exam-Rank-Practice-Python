if __name__ == "__main__":
    n,m = map(int, (input().split()))
    j = 1
    for j in range(1, n, 2):
        print(((".|.")*j).center(m, "-"))
    print("WELCOME".center(m, "-"))
    j = n
    for j in range(n-2, -1, -2):
        print(((".|.")*j).center(m, "-"))