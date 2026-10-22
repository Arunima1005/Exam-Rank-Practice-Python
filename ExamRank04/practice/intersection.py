# def list_intersection_finder(lists: list[list[int]]) -> list[int]:
#     if not lists or any(not l for l in lists):
#         return []
#     first = set(lists[0])
#     for lst in lists[1:]:
#         first = first.intersection(set(lst))
#     return sorted(first)


def list_intersection_finder(lists: list[list[int]]) -> list[int]:
    if not lists or any(not l for l in lists):
        return []
    first = lists[0].copy()
    for lst in lists[1:]:
        first = [i for i in first if i in lst]
    return sorted(set(first))


print(list_intersection_finder([[1, 2, 3], [2, 3, 4], [2, 3, 5]]))  # Expected: [2, 3]
print(list_intersection_finder([[1, 2, 3, 4], [2, 4, 6, 8], [4, 8, 12]]))  # Expected: [4]
print(list_intersection_finder([[1, 1, 2, 3], [1, 2, 2, 3], [1, 2, 3, 3]]))  # Expected: [1, 2, 3]
print(list_intersection_finder([[1, 2, 3], [4, 5, 6]]))  # Expected: []
print(list_intersection_finder([]))  # Expected: []
print(list_intersection_finder([[1, 2, 3], []]))  # Expected: []
print(list_intersection_finder([[5]]))  # Expected: [5]