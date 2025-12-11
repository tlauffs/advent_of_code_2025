from functools import lru_cache


devices: dict[str, list[str]] = {}

for line in open("input.txt"):
    line = line.split()
    input = line[0][:-1]
    outputs = line[1:]
    devices[input] = outputs

def get_paths_count(start: str, devices: dict[str, list[str]]) -> int:
    @lru_cache(maxsize=None)
    def dfs(node: str) -> int:
        device = devices.get(node, [])
        if "out" in device:
            return 1
        total = 0
        for child in device:
            total += dfs(child)
        return total
    return dfs(start)

start = "you"
print(f"Part 1: {get_paths_count(start, devices)}")

def get_paths_count_part2(start: str, devices: dict[str, list[str]]) -> int:
    @lru_cache(maxsize=None)
    def dfs(node: str, has_fft: bool, has_dac: bool) -> int:
        device = devices.get(node, [])

        if node == "fft":
            has_fft = True
        if node == "dac":
            if not has_fft:
                return 0
            has_dac = True

        if "out" in device:
            return 1 if has_fft and has_dac else 0

        total = 0
        for child in device:
            total += dfs(child, has_fft, has_dac)
        return total

    return dfs(start, False, False)

start = "svr"

print(f"Part 2: {get_paths_count_part2(start, devices)}")
