def array_rotation_detector(arr1: list, arr2: list) -> bool:
    if not arr1 and not arr2:
        return True
    for i in range(len(arr1)):
        new = arr1[i:]
        new.extend(arr1[:i])
        if new == arr2:
            return True
    return False


print(array_rotation_detector([1, 2, 3, 4, 5], [4, 5, 1, 2, 3]))  # Expected: True
print(array_rotation_detector([1, 2, 3, 4, 5], [5, 1, 2, 3, 4]))  # Expected: True
print(array_rotation_detector([1, 2, 3], [3, 2, 1]))  # Expected: False
print(array_rotation_detector([1, 2], [1, 2, 3]))  # Expected: False
print(array_rotation_detector([], []))  # Expected: True