import random


def create_initial_grid(rows, cols):
    return [[random.choice([0, 1]) for _ in range(cols)] for _ in range(rows)]


def next_gen(grid):
    rows = len(grid)
    cols = len(grid[0])
    new_grid = [[0 for _ in range(cols)] for _ in range(rows)]

    for row in range(rows):
        for col in range(cols):
            live_neighbors = count_live_neighbors(grid, row, col)
            if grid[row][col] == 1:
                new_grid[row][col] = 1 if live_neighbors in [2, 3] else 0
            else:
                new_grid[row][col] = 1 if live_neighbors == 3 else 0
    return new_grid


def count_live_neighbors(grid, row, col):
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
                  (0, 1), (1, -1), (1, 0), (1, 1)]
    rows = len(grid)
    cols = len(grid[0])
    count = 0
    for dr, dc in directions:
        r, c = row + dr, col + dc
        if 0 <= r < rows and 0 <= c < cols and grid[r][c] == 1:
            count += 1
    return count

