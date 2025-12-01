pos = 50
score = 0
score_part2 = 0

for line in open("./input.txt"):
    prev_pos = pos
    dir,step = line[0], int(line[1:])
    if dir == "R":
        pos = (pos + step) % 100
        wraps = (step + prev_pos) // 100
    if dir == "L":
        pos = (pos - step) % 100
        wraps = (step + ((100 - prev_pos) % 100)) // 100
    score += pos == 0
    score_part2 += wraps

print("part 1:", score, "part 2:", score_part2)
