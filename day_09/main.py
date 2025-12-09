def rectangle_area(p1: tuple[int,int], p2: tuple[int,int]) -> int:
    return (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)

def draw_border(red_tiles: list[tuple[int,int]], green_tiles: set[tuple[int,int]]) -> None:
    all_x = [x for x, _ in green_tiles]
    all_y = [y for _, y in green_tiles]
    min_x, max_x = min(all_x), max(all_x)
    min_y, max_y = min(all_y), max(all_y)

    for y in range(min_y, max_y + 1):
        row = ""
        for x in range(min_x, max_x + 1):
            if (x, y) in red_tiles:
                row += '\033[31m#\033[0m'  # red
            elif (x, y) in green_tiles:
                row += '\033[32mX\033[0m'  # green
            else:
                row += '.'  # default
        print(row)

def rect_is_valid(a, b, green_tiles) -> bool:
    x1, y1 = a
    x2, y2 = b

    min_x, max_x = sorted((x1, x2))
    min_y, max_y = sorted((y1, y2))

    for gx, gy in green_tiles:
        if min_x < gx < max_x and min_y < gy < max_y:
            return False

    return True

with open("input.txt") as f:
    lines = f.readlines()

red_tiles: list[tuple[int,int]] = []
for line in lines:
    x, y = map(int, line.split(','))
    red_tiles.append((x, y))

max_area = 0
for i in range(len(red_tiles)):
    for j in range(i+1, len(red_tiles)):
        area = rectangle_area(red_tiles[i], red_tiles[j])
        if area > max_area:
            max_area = area

print(f"Part 1: {max_area}")

green_tiles: set[tuple[int,int]] = set()
length = len(red_tiles)
for i in range(length):
    x, y = red_tiles[i]
    x2, y2 = red_tiles[(i+1) % length]
    green_tiles.add((x, y))
    green_tiles.add((x2, y2))
    # vertical border
    if x == x2:
        for y in range(min(y, y2), max(y, y2) + 1):
            green_tiles.add((x, y))
    # horizontal border
    if y == y2:
        for x in range(min(x, x2), max(x, x2) + 1):
            green_tiles.add((x, y))

# draw_border(red_tiles, green_tiles)
max_area_part_2 = 0
for i in range(len(red_tiles)):
    for j in range(i+1, len(red_tiles)):
        rect_area = rectangle_area(red_tiles[i], red_tiles[j])
        if max_area_part_2 > rect_area:
            continue
        if rect_is_valid(red_tiles[i], red_tiles[j], green_tiles):
            max_area_part_2 = rect_area
        # draw_border(red_tiles, rect_border)

print(f"Part 2: {max_area_part_2}")
