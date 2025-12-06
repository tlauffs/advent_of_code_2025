class Bank:
    def __init__(self, batteries: str):
        self.batteries = batteries

    def __str__(self):
        return self.batteries

    def get_largest_joltage(self, number_of_turns = 2) -> int:
        batteries = self.batteries
        remaining_pops = len(batteries) - number_of_turns
        stack = []
        for b in batteries:
            while remaining_pops > 0 and stack and stack[-1] < b:
                stack.pop()
                remaining_pops -= 1
            stack.append(b)
        return int(''.join(stack[:number_of_turns]))

banks = []
with open('input.txt') as f:
    for line in f:
        banks.append(Bank(line.strip()))

result_part1 = 0
result_part2 = 0
for bank in banks:
    result_part1 += bank.get_largest_joltage(2)
    result_part2 += bank.get_largest_joltage(12)

print("part 1:", result_part1)
print("part 2:", result_part2)



