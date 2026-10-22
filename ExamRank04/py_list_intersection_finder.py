# Write a function that finds the intersection of multiple sorted lists.
# Return a new list containing elements that appear in ALL input lists, in sorted order.

# The function should:
# - Return elements that appear in ALL lists
# - Result should be sorted in ascending order
# - Remove duplicates from the result
# - Handle empty input or empty lists gracefully
# - If any list is empty, the intersection is empty
# Function signature

def list_intersection_finder(lists: list[list[int]]) -> list[int]:
    if lists == [] or any(l == [] for l in lists):
        return []
    result = set(lists[0])

    for l in lists[1:]:
        result = result.intersection(set(l))
    return sorted(result)

    
print(list_intersection_finder([[1, 2, 3], [2, 3, 4], [2, 3, 5]]))  # Expected: [2, 3]
print(list_intersection_finder([[1, 2, 3, 4], [2, 4, 6, 8], [4, 8, 12]]))  # Expected: [4]
print(list_intersection_finder([[1, 1, 2, 3], [1, 2, 2, 3], [1, 2, 3, 3]]))  # Expected: [1, 2, 3]
print(list_intersection_finder([[1, 2, 3], [4, 5, 6]]))  # Expected: []
print(list_intersection_finder([]))  # Expected: []
print(list_intersection_finder([[1, 2, 3], []]))  # Expected: []
print(list_intersection_finder([[5]]))  # Expected: [5]

## MY logic

# def list_intersection_finder(lists: list[list[int]]) -> list[int]:
#     if not lists or any(not l for l in lists):
#         return []

#     result = lists[0].copy()

#     for l in lists[1:]:
#         result = [i for i in result if i in l]

#     return sorted(set(result))





### CONCEPT

# result.intersection(l)	Keep common elements
# result.intersection_update(l)	Update the existing set with common elements


## AI implemenation


# def list_intersection_finder(lists: list[list[int]]) -> list[int]:
#     if not lists or any(not lst for lst in lists):
#         return []

#     result = set(lists[0])

#     for lst in lists[1:]:
#         result &= set(lst)

#     return sorted(result)






# def list_intersection_finder(lists: list[list[int]]) -> list[int]:
#     if not lists or any(not l for l in lists):
#         return []

#     result = set(lists[0])

#     for l in lists[1:]:
#         result.intersection_update(l)

#     return sorted(result)


