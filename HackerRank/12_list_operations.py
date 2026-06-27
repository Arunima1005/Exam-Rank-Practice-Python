if __name__ == '__main__':
    N = int(input())
    l = []
    for _ in range(N):
        var = input()
        command = var.split()
        # operation, *args = input().split() --- nice way to do
        match command[0]:
            case "append":
                l.append(int(command[1]))
            case "insert":
                l.insert(int(command[1]), int(command[2]))
            case "print":
                print(l)
            case "remove":
                l.remove(int(command[1]))
            case "sort":
                l.sort()
            case "pop":
                l.pop()
            case "reverse":
                l.reverse()
    # print(l)
