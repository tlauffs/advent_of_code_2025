from typing import List

DIRECTIONS = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),          (0, 1),
    (1, -1),  (1, 0),  (1, 1)
]

def count_neighbors(r_idx: int, c_idx: int) -> int:
    count = 0
    for dr, dc in DIRECTIONS:
        row = r_idx + dr
        col = c_idx + dc
        if row < 0 or row >= len(grid):
            continue
        if col < 0 or col >= len(grid[row]):
            continue
        if grid[row][col] == "@":
            count += 1
    return count

def count_removable_neighbors(grid: List[List[str]], remove_rolls: bool = False) -> int:
    result = 0
    for r_idx, row in enumerate(grid):
        for c_idx, col in enumerate(row):
            if col != "@":
                continue
            if count_neighbors(r_idx, c_idx) <= 3:
                result += 1
                if remove_rolls:
                    grid[r_idx][c_idx] = "."
    return result

grid = []
with open("input.txt") as f:
    for line in f:
        grid.append(list(line.strip()))
result_part1 = count_removable_neighbors(grid)

result_part2 = 0
while (True):
    count = count_removable_neighbors(grid, True)
    result_part2 += count
    if count == 0:
        break

print('part1: ', result_part1)
print('part2: ', result_part2)

