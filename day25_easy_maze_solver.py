from collections import deque

MAZE = [
    "###########",
    "#S        #",
    "# ### ### #",
    "#   #     #",
    "### ##### #",
    "#         #",
    "# ### ### #",
    "#       #E#",
    "###########",
]

# Find start and end
for r, row in enumerate(MAZE):
    for c, ch in enumerate(row):
        if ch == "S":
            start = (r, c)
        elif ch == "E":
            end = (r, c)

# BFS
queue = deque([start])
came_from = {start: None}

while queue:
    r, c = queue.popleft()

    if (r, c) == end:
        break

    for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        nr, nc = r + dr, c + dc

        if MAZE[nr][nc] != "#" and (nr, nc) not in came_from:
            came_from[(nr, nc)] = (r, c)
            queue.append((nr, nc))

# Display path
if end not in came_from:
    print("No path found")
else:
    grid = [list(row) for row in MAZE]
    step = came_from[end]
    steps = 0

    while step != start:
        grid[step[0]][step[1]] = "."
        step = came_from[step]
        steps += 1

    for row in grid:
        print("".join(row))

    print("Shortest path:", steps, "steps")