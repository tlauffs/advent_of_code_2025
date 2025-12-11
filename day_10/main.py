import ast
from collections import deque
from typing import Dict
import pulp

Button = tuple[int, ...]

class Machine:
    def __init__(self, light_diagram: list[int], buttons: list[tuple[int, ...]], jultage_level: list[int]):
         # target light diagram (0=off, 1=on)
        self.light_diagram = light_diagram 
        # list of buttons (tuples of light switch indices)
        self.buttons = buttons
        # target light jultages
        self.jultage_level = jultage_level
        # current light state
        self.current_lights = [0] * len(light_diagram)
        # current jultage level
        self.current_jultage_levels = [0] * len(jultage_level)

    def __str__(self) -> str:
        return f"light_diagram: {self.light_diagram}\nbuttons: {self.buttons}\ncurrent_lights: {self.current_lights}\njultage_level: {self.jultage_level}"

    def push_button(self, button: Button) -> None:
        for i in button:
            self.current_lights[i] ^= 1

    def is_goal_light_state(self) -> bool:
        return self.current_lights == self.light_diagram

    def get_lowest_presses_needed(self) -> int:
        start = tuple(self.current_lights)
        goal = tuple(self.light_diagram)

        visited = {start: 0}
        queue = deque([start])

        while queue:
            state = queue.popleft()
            current_presses = visited[state]
            if state == goal:
                return current_presses
            for button in self.buttons:
                new_state = list(state) 
                for i in button:
                    new_state[i] ^= 1
                new_state = tuple(new_state)
                if new_state not in visited:
                    visited[new_state] = current_presses + 1
                    queue.append(new_state)
        return -1

    def get_lowest_presses_needed_jultages(self) -> int:
        matrix = [[1 if i in button else 0 for button in self.buttons] for i in range(len(self.current_jultage_levels))]
        goal = self.jultage_level
        num_buttons = len(self.buttons)

        problem = pulp.LpProblem("minimum_jultage_presses", pulp.LpMinimize)

        # x[i] number of presses of button i
        x = [pulp.LpVariable(f"x{i}", lowBound=0, cat="Integer") for i in range(num_buttons)]

        problem += pulp.lpSum(x)

        # Add constraints: each counter i must reach its goal exactly
        for i, row in enumerate(matrix):
            problem += pulp.lpSum(row[j] * x[j] for j in range(len(self.buttons))) == self.jultage_level[i]

        problem.solve()
        if problem.status != pulp.LpStatusOptimal:
            return -1
        return sum(int(x[j].value()) for j in range(len(self.buttons)))

inputs: list[Machine] = []
with open("input.txt") as f:
    for line in f:
        line = line.split()

        light_diagram = [1 if i == '#' else 0 for i in line[0][1:-1]]

        raw_buttons = [ast.literal_eval(x) for x in line[1:-1]]
        buttons = [b if isinstance(b, tuple) else (b,) for b in raw_buttons]

        jultage_str = line[-1][1:-1]
        jultage_level = [int(i) for i in jultage_str.split(',')]

        machine = Machine(light_diagram, buttons, jultage_level)
        inputs.append(machine)

result_part_1 = 0
result_part_2 = 0
for i,machine in enumerate(inputs):
    result_part_1 += machine.get_lowest_presses_needed()
    result_part_2 += machine.get_lowest_presses_needed_jultages()

print(f"Part 1: {result_part_1}")
print(f"Part 2: {result_part_2}")
