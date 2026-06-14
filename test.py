class Cell:
    def __init__(self):
        self.north = True
        self.south = True
        self.east = True
        self.west = True

rows = 3
cols = 3

grid = [[Cell() for _ in range(cols)] for _ in range(rows)]

def render(grid):
    rows = len(grid)
    cols = len(grid[0])

    # top border
    print("█" * (cols * 2 + 1))

    for r in range(rows):
        line = "█"

        for c in range(cols):
            cell = grid[r][c]

            line += " "

            if cell.east:
                line += "█"
            else:
                line += " "

        print(line)

        bottom = ""

        for c in range(cols):
            cell = grid[r][c]

            if cell.south:
                bottom += "██"
            else:
                bottom += "█ "

        print(bottom + "█")

# grid[0][0].east = False
# grid[0][1].west = False

render(grid)