with open("input.txt") as f:
    lines = f.readlines()

start_col: int = lines[0].strip().index("S")
beam_cols: dict[int, int] = {start_col: 1}
split_count: int = 0

for line in lines[1:]:
    splitters: set[int] = {i for i,x in enumerate(line) if x == "^" }
    for beam_col in list(beam_cols):
        if beam_col in splitters:
            split_count += 1
            current_count = beam_cols[beam_col]
            beam_cols.pop(beam_col)
            if not beam_col + 1 in beam_cols:
                beam_cols[beam_col + 1] = 0
            beam_cols[beam_col + 1] += current_count
            if not beam_col - 1 in beam_cols:
                beam_cols[beam_col - 1] = 0
            beam_cols[beam_col - 1] += current_count

print(f"Part 1: {split_count}")
print(f"Part 2: {sum(beam_cols.values())}")
