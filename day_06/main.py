from functools import reduce
import operator
import re

def calculate_result(numbers: list[list[int]], operations: list[str]) -> int:   
    result = []
    for i, op in enumerate(operations):
        if op == "+":
            result.append(sum(numbers[i]))
        if op == "*":
            result.append(reduce(operator.mul, numbers[i], 1))
    return sum(result)

with open("input.txt") as f:
    lines = f.readlines()

numbers: list[list[int]] = []
operations: list[str] = []

rows = [list(map(int, line.split())) for line in lines[:-1]]
numbers = [list(col) for col in zip(*rows)]
operations = lines[-1].strip().split()

result = calculate_result(numbers, operations)

print(f"Part 1: {result}")

col_length = [len(m) for m in re.findall(r' +', lines[-1])]
col_length[-1] += 1

rows_part_2 = [] 
for line in lines[:-1]:
    parts = []
    pos = 0
    for length in col_length:
        parts.append(line[pos:pos + length])
        pos += length + 1
    rows_part_2.append(parts)

rows_part_2 = [list(col) for col in zip(*rows_part_2)]
numbers_part_2: list[list[int]] = []
for row in rows_part_2:
    row = list(map(list, row))
    num_lists = [list(x) for x in zip(*row)]
    nums = [int(''.join(num_list)) for num_list in num_lists]
    numbers_part_2.append(nums)

result_part_2 = calculate_result(numbers_part_2, operations)
print(f"Part 2: {result_part_2}")

