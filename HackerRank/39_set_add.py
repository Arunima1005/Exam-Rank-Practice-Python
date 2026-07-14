# if __name__ == "__main__":
#     N = int(input())
#     country = set()
#     for _ in range(N):
#         country.add(input())

    # print(len(country))

#shorter way
if __name__ == "__main__":
    n = int(input())
    countries = {input() for _ in range(n)}
    print(len(countries))
