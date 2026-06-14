# class Cell:
#     def __init__(self):
#         self.north = True
#         self.south = True
#         self.east = True
#         self.west = True

# rows = 3
# cols = 3

# grid = [[Cell() for _ in range(cols)] for _ in range(rows)]

# # print(grid)

# def render(grid):
#     rows = len(grid)
#     cols = len(grid[0])

#     # top border
#     print("█" * (cols * 2 + 1))

#     for r in range(rows):
#         line = "█"

#         for c in range(cols):
#             cell = grid[r][c]

#             line += " "

#             if cell.east:
#                 line += "█"
#             else:
#                 line += " "

#         print(line)

#         bottom = ""

#         for c in range(cols):
#             cell = grid[r][c]

#             if cell.south:
#                 bottom += "██"
#             else:
#                 bottom += "█ "

#         print(bottom + "█")

# grid[0][0].east = False
# grid[0][1].west = False

# grid[0][1].north = False
# grid[0][1].east = False
# render(grid)



class Cell:
    def __init__(self):
        self.north = True
        self.south = True
        self.east = True
        self.west = True


rows = 3
cols = 3

grid = [[Cell() for _ in range(cols)] for _ in range(rows)]

# Open some walls
grid[0][0].east = False
grid[0][1].west = False

grid[0][0].south = False
grid[1][0].north = False


def render(grid):
    rows = len(grid)
    cols = len(grid[0])

    # TOP BORDER
    top = "┌"

    for c in range(cols):
        top += "───"

        if c == cols - 1:
            top += "┐"
        else:
            top += "┬"

    print(top)

    # CELLS
    for r in range(rows):

        middle = "│"

        for c in range(cols):
            cell = grid[r][c]

            middle += "   "

            if cell.east:
                middle += "│"
            else:
                middle += " "

        print(middle)

        # BOTTOM WALLS
        bottom = ""

        for c in range(cols):
            cell = grid[r][c]

            if c == 0:
                if r == rows - 1:
                    bottom += "└"
                else:
                    bottom += "├"

            if cell.south:
                bottom += "───"
            else:
                bottom += "   "

            if c == cols - 1:
                if r == rows - 1:
                    bottom += "┘"
                else:
                    bottom += "┤"
            else:
                if r == rows - 1:
                    bottom += "┴"
                else:
                    bottom += "┼"

        print(bottom)


render(grid)