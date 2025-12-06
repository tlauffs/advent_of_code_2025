def count_fresh_ingredients(lines):
    fresh_ingredients: set[tuple[int, int]] = set()
    number_of_fresh_ingredients: int = 0

    for line in lines:
        line = line.strip()
        if not line:
            continue
        if "-" in line:
            start, end = map(int, line.split("-"))
            fresh_ingredients.add((start, end))
        else:
            num = int(line)
            if any(start <= num <= end for start, end in fresh_ingredients):
                number_of_fresh_ingredients += 1

    return number_of_fresh_ingredients, fresh_ingredients

def merge_ranges(ranges: set[tuple[int, int]]) -> list[tuple[int, int]]:
    sorted_ranges = sorted(ranges, key=lambda x: x[0])
    merged = []

    for start, end in sorted_ranges:
        if not merged:
            merged.append([start, end])
        else:
            last_start, last_end = merged[-1]
            if start <= last_end + 1:
                merged[-1][1] = max(last_end, end)
            else:
                merged.append([start, end])
    return merged

with open("input.txt") as f:
    lines = f.readlines()

number_of_fresh_ingredients, fresh_ingredient_ranges = count_fresh_ingredients(lines)
print(f"Part 1: {number_of_fresh_ingredients}")

merged_ranges = merge_ranges(fresh_ingredient_ranges)
number_of_ingredients = sum(end - start + 1 for start, end in merged_ranges)
print(f"Part 2: {number_of_ingredients}")
