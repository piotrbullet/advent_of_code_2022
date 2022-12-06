def parse_instructions(filepath: str):
    with open(filepath) as f:
        text = f.read()
    stacks, instructions = text.split("\n\n")
    instructions_lines = instructions.split("\n")
    ins = list()
    for line in instructions_lines:
        ins.append([int(s) for s in line.split() if s.isdigit()])
    return ins


def part_one(filepath: str):
    instructions = parse_instructions(filepath)
    stacks: dict = STACKS.copy()
    for no, from_, to_ in instructions:
        for i in range(no):
            moving_box = stacks[from_].pop(len(stacks[from_])-1)
            stacks[to_].append(moving_box)
    for i in range(1, len(stacks)+1):
        stack = stacks[i]
        print(stack[len(stacks[i])-1])


def part_two(filepath: str):
    instructions = parse_instructions(filepath)
    stacks: dict = STACKS.copy()
    for no, from_, to_ in instructions:
        for i in reversed(list(range(no))):
            moving_box = stacks[from_].pop(len(stacks[from_])-(1+i))
            stacks[to_].append(moving_box)
    for i in range(1, len(stacks)+1):
        stack = stacks[i]
        print(stack[len(stacks[i])-1])


STACKS: dict = {1: ["V", "C", "D", "R", "Z", "G", "B", "W"],
                2: ["G", "W", "F", "C", "B", "S", "T", "V"],
                3: ["C", "B", "S", "N", "W"],
                4: ["Q", "G", "M", "N", "J", "V", "C", "P"],
                5: ["T", "S", "L", "F", "D", "H", "B"],
                6: ["J", "V", "T", "W", "M", "N"],
                7: ["P", "F", "L", "C", "S", "T", "G"],
                8: ["B", "D", "Z"],
                9: ["M", "N", "Z", "W"]}


if __name__ == "__main__":
    data_path = "data\\day5.txt"
    # print(part_one(data_path))
    part_two(data_path)
