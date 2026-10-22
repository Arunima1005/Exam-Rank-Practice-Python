def constellation_mapper(stars: list[tuple[int, int]], dim: int) -> list[str]:
    result = [['.'] * dim for _ in range(dim)]

    for x, y in stars:
        if 0 <= x < dim and 0 <= y < dim:
            result[x][y] = '*'
    return ["".join(r) for r in result]

print(constellation_mapper([(0, 0), (1, 1), (2, 2)], 3))  # Expected: ['*..', '.*.', '..*']
# print(constellation_mapper([(1, 1), (0, 1), (2, 1), (1, 0), (1, 2)], 3))  # Expected: ['.*.', '***', '.*.']
# print(constellation_mapper([], 2))  # Expected: ['..', '..']
# print(constellation_mapper([(0, 0), (0, 0), (1, 1)], 2))  # Expected: ['*.', '.*']
# print(constellation_mapper([(0, 0), (5, 5)], 3))  # Expected: ['*..', '...', '...']
# print(constellation_mapper([(1, 0), (1, 1), (1, 2)], 3))  # Expected: ['...', '***', '...']