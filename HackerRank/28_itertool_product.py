from itertools import product

if __name__ == "__main__":
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(*product(a, b)) # better option than the below
    # print(a)
    # for i in product(a, b):
    #     print(i,end = " ")
    # print()
    # # print(list(product(a, b)))
   