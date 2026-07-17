def is_rotation(arr1: list, arr2: list) -> bool:

    if len(arr1) != len(arr2):
        return False
    if arr1 == arr2:
        return True
    temp = arr1[:] # don't modify original
    for _ in range(len(temp)-1):
        num = temp.pop()
        temp.insert(0, num)
        if temp == arr2:
            return True
    return False


print(is_rotation([1, 2, 3, 4, 5], [4, 5, 1, 2, 3]))
print(is_rotation([1, 2, 3, 4, 5], [5, 1, 2, 3, 4]))
print(is_rotation([1, 2, 3], [3, 2, 1]))
print(is_rotation([1, 2], [1, 2, 3]))
print(is_rotation([], []))

## true true false false true