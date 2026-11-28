grid = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
]


def show(grid):
    for row in grid:
        line = ""
        for cell in row:
            if cell == 1:
                line = line + "O "
            else:
                line = line + ". "
        print(line)


def count_neighbours(grid, r, c):
    count = 0
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue                      # skip the cell itself
            nr = r + dr
            nc = c + dc
            if 0 <= nr < 5 and 0 <= nc < 5:   # stay inside the board
                count = count + grid[nr][nc]
    return count


for generation in range(4):
    print("Generation", generation)
    show(grid)
    print()

    new_grid = []
    for r in range(5):
        new_row = []
        for c in range(5):
            n = count_neighbours(grid, r, c)
            if grid[r][c] == 1 and (n == 2 or n == 3):
                new_row.append(1)             # stays alive
            elif grid[r][c] == 0 and n == 3:
                new_row.append(1)             # is born
            else:
                new_row.append(0)             # dies or stays empty
        new_grid.append(new_row)
    grid = new_grid