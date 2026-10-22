def merge_two_lists(a,b):
    i = 0
    j = 0
    result = []
    while i < len(a) and j < len(b):
        if a[i] > b[j]:
            result.append(b[j])
            j += 1
        else:
            result.append(a[i])
            i += 1
    result.extend(a[i:])
    result.extend(b[j:])
    return result


def merge_sorted_lists(lists: list[list[int]]) -> list[int]:
    result = []
    for lst in lists:
        result = merge_two_lists(result, lst)
    return result



# print(merge_two_lists([1, 3, 5], [2, 4, 6]))
# # [1, 2, 3, 4, 5, 6]

# print(merge_two_lists([1, 1, 3], [1, 2, 2]))
# # [1, 1, 1, 2, 2, 3]

# print(merge_two_lists([], [-3, 0, 4]))
# # [-3, 0, 4]

print(merge_sorted_lists([[1, 3, 5], [2, 4, 6]]))  # Expected: [1, 2, 3, 4, 5, 6]
print(merge_sorted_lists([[1, 5, 9], [2, 3, 8], [4, 6, 7]]))  # Expected: [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(merge_sorted_lists([[5], [1, 3], [2, 4]]))  # Expected: [1, 2, 3, 4, 5]
print(merge_sorted_lists([[1, 1, 2], [2, 3, 3]]))  # Expected: [1, 1, 2, 2, 3, 3]
print(merge_sorted_lists([[], [1, 2, 3]]))  # Expected: [1, 2, 3]
print(merge_sorted_lists([[]]))  # Expected: []
print(merge_sorted_lists([[-5, -1, 0], [-3, 2, 4]]))  # Expected: [-5, -3, -1, 0, 2, 4]
print(merge_sorted_lists([[10], [10], [10]]))  # Expected: [10, 10, 10]

