from collections import Counter

if __name__ == "__main__":
    X = int(input())
    shoe_sizes = list (map(int, input().split()))
    N = int(input())
    shoe_customer = []
    for _ in range(N):
        lst = list(map(int, input().split()))
        shoe_customer.append(lst)
    count_shoe = Counter(shoe_sizes)
    total_cost = 0
 

    # Better OPtion the below one 
    for size, price in shoe_customer:
        if count_shoe[size] > 0:
            total_cost += price
            count_shoe[size] -= 1
    print(total_cost)

# all together better solution
# for _ in range(N):
#     size, price = map(int, input().split())

#     if count_shoe[size] > 0:
#         total_cost += price
#         count_shoe[size] -= 1


# -- down another option
       # for size, price in shoe_customer:
    #     # print(f"{size}-{price}")
    #     for shoe, c in count_shoe.items():
    #         # print(count_shoe)
    #         if shoe == size and c> 0:
    #             count_shoe.subtract([shoe])
    #             total_cost += price
    #             break

    