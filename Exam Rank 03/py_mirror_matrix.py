def mirror_matrix(matrix: list[list[int]]) -> list[list[int]]:
    for row in range(len(matrix)):
        matrix[row] = matrix[row][::-1]
    return matrix


print(mirror_matrix([[1,2,3],[4,5,6]]))
print(mirror_matrix([[1,2],[3,4],[5,6]]))
print(mirror_matrix([[7]]))
print(mirror_matrix([[1,2,3,4]]))
print(mirror_matrix([[-1,-2],[-3,-4]]))


# ###Pythonic way---best option
# def mirror_matrix(matrix: list[list[int]]) -> list[list[int]]:
#     return [row[::-1] for row in matrix]

#### Using reverse 
# for num_lst in matrix:
    #     num_lst.reverse()
    # return matrix


#### If slicing ([::-1]) was forbidden
# def mirror_matrix(matrix):
    # result = []

    # for row in matrix:
    #     new_row = []
    #     for i in range(len(row) - 1, -1, -1):
    #         new_row.append(row[i])
    #     result.append(new_row)

    # return result