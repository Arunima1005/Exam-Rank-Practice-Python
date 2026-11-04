def check_duplicate_number(row: list[str]) -> bool:
    row_d = []
    for i in range(len(row)):
        if row[i].isdigit():
            row_d.append(row[i])
    if len(row_d) != len(set(row_d)):
        return False
    return True

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        for row in board:
            if not check_duplicate_number(row):
                return False

        for col in range(len(board[0])):
            column = [row[col] for row in board]
            if not check_duplicate_number(column):
                return False

        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                # print("Box starts at:", box_row, box_col)
                result = []
                for r in range(box_row, box_row + 3):
                    for c in range(box_col, box_col + 3):
                        result.append(board[r][c])
                if not check_duplicate_number(result):
                    return False
                    
        return True
s = Solution()
print(s.isValidSudoku(board =
[["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]
))
