def constellation_mapper(stars: list[tuple[int, int]], dim: int) -> list[str]:
    arr = []
    for x in range(dim):
        s = '.' * dim
        arr.append(s)
    for (x, y) in stars:
        if x < 0 or x >= dim or y < 0 or y >= dim:
            continue
        st = list(arr[x])
        st[y] = '*'
        arr[x] = "".join(st)
    return arr            

print(constellation_mapper([(0, 0), (1, 1), (2, 2)], 3))  # Expected: ['*..', '.*.', '..*']
print(constellation_mapper([(1, 1), (0, 1), (2, 1), (1, 0), (1, 2)], 3))  # Expected: ['.*.', '***', '.*.']
print(constellation_mapper([], 2))  # Expected: ['..', '..']
print(constellation_mapper([(0, 0), (0, 0), (1, 1)], 2))  # Expected: ['*.', '.*']
print(constellation_mapper([(0, 0), (5, 5)], 3))  # Expected: ['*..', '...', '...']
print(constellation_mapper([(1, 0), (1, 1), (1, 2)], 3))  # Expected: ['...', '***', '...']


# AI implementation


# def constellation_mapper(
#     stars: list[tuple[int, int]], dim: int
# ) -> list[str]:
#     grid = [["."] * dim for _ in range(dim)]

#     for row, col in stars:
#         if 0 <= row < dim and 0 <= col < dim:
#             grid[row][col] = "*"

#     return ["".join(row) for row in grid]

