def array_rotation_detector(arr1: list, arr2: list) -> bool:
    if len(arr1) != len(arr2):
        return False
    if arr1 == arr2 == []:
        return True
    for _ in range(len(arr1)):
        last = arr2.pop()
        arr2.insert(0,last)
        if arr1 == arr2:
            return True
    return False

print(array_rotation_detector([1, 2, 3, 4, 5], [4, 5, 1, 2, 3]))  # Expected: True
print(array_rotation_detector([1, 2, 3, 4, 5], [5, 1, 2, 3, 4]))  # Expected: True
print(array_rotation_detector([1, 2, 3], [3, 2, 1]))  # Expected: False
print(array_rotation_detector([1, 2], [1, 2, 3]))  # Expected: False
print(array_rotation_detector([], []))  # Expected: True



# AI implementation

# def array_rotation_detector(arr1: list, arr2: list) -> bool:
#     if len(arr1) != len(arr2):
#         return False

#     return len(arr1) == 0 or any(
#         arr1[i:] + arr1[:i] == arr2
#         for i in range(len(arr1))
#     )


# def array_rotation_detector(arr1: list, arr2: list) -> bool:
#     if len(arr1) != len(arr2):
#         return False

#     return arr2 in [arr1[i:] + arr1[:i] for i in range(len(arr1))] or arr1 == arr2 == []

# def array_rotation_detector(arr1: list, arr2: list) -> bool:
#     if len(arr1) != len(arr2):
#         return False

#     return arr2 in [arr1[i:] + arr1[:i] for i in range(len(arr1))] or arr1 == arr2 == []