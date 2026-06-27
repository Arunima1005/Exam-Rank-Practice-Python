if __name__ == '__main__':
    n = int(input())
    arr = set(map(int, input().split()))
    arr.remove(max(arr))
    print(max(arr))

    # n = int(input())
    # arr = map(int, input().split())
    # arr1 = list(arr)
    # num = max(arr1)
    # arr1.remove(num)
    # while num == max(arr1): ///if list has all 6 6 6..then next line will throw error as list is empty
    #     arr1.remove(num)
    # # print(f" Score borad : {arr1}")
    # print(max(arr1))

   