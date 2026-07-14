if __name__ == "__main__":
    n = int(input())

    num = set(map(int, input().split()))

    N = int(input())

    for _ in range(N):
        comm= input().split()
        match comm[0]:
            case "pop":
                num.pop()
            case "remove":
                num.remove(int(comm[1]))
            case "discard":
                num.discard(int(comm[1]))

    print(sum(num))

