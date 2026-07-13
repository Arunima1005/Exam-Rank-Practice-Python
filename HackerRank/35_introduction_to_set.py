def average(array):
    # your code goes here
    heights = set(array)
    length = len(heights)
    return round(sum(heights)/length,3)
    # return length
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)