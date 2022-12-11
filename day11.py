def part_one(filepath: str):
    monkeys = parse_monkeys_from_file(filepath)
    for i in range(1, 21):
        for j in range(len(monkeys)):
            for k in range(len(monkeys[j]["items"])):
                monkeys[j], throw_to_monkey, new_worry_level = inspection(monkeys[j])
                monkeys[throw_to_monkey]["items"].append(new_worry_level)
    pass


def part_two(filepath: str):
    monkeys = parse_monkeys_from_file(filepath)
    m: int = 1
    for i in range(len(monkeys)):
        m *= monkeys[i]["test_no"]
    for i in range(1, 10001):
        print(f" loop {i}")
        for j in range(len(monkeys)):
            for k in range(len(monkeys[j]["items"])):
                monkeys[j], throw_to_monkey, new_worry_level = inspection_2(monkeys[j], m)
                monkeys[throw_to_monkey]["items"].append(new_worry_level)
    pass


def inspection(monkey: dict):
    curr_item = monkey['items'].pop(0)
    operation_no = int(monkey["op_no"]) if monkey["op_no"].isnumeric() else curr_item
    if monkey["operation"] == "*":
        new_worry_level = int((curr_item*operation_no)/3)
    elif monkey["operation"] == "+":
        new_worry_level = int((curr_item+operation_no)/3)
    if new_worry_level % monkey["test_no"] == 0:
        throw_to_monkey = monkey["true_monkey"]
    else:
        throw_to_monkey = monkey["false_monkey"]
    monkey["inspections"] += 1
    return monkey, throw_to_monkey, new_worry_level


def inspection_2(monkey: dict,  m: int):
    curr_item = monkey['items'].pop(0)
    operation_no = int(monkey["op_no"]) if monkey["op_no"].isnumeric() else curr_item
    if monkey["operation"] == "*":
        new_worry_level = int(curr_item*operation_no) % m
    elif monkey["operation"] == "+":
        new_worry_level = int(curr_item+operation_no) % m
    if new_worry_level % monkey["test_no"] == 0:
        throw_to_monkey = monkey["true_monkey"]
    else:
        throw_to_monkey = monkey["false_monkey"]
    monkey["inspections"] += 1
    return monkey, throw_to_monkey, new_worry_level


def parse_monkeys_from_file(filepath: str) -> list:
    with open(filepath) as f:
        text = f.read()
    monkeys_raw = text.split("\n\n")
    monkeys = list()
    for m in monkeys_raw:
        curr_monkey_lines = m.split("\n")
        items = [int(x) for x in curr_monkey_lines[1].replace(",", "").split()[2:]]
        operation = curr_monkey_lines[2].split()[4]
        op_no = curr_monkey_lines[2].split()[5]
        test_no = int(curr_monkey_lines[3].split()[3])
        true_monkey = int(curr_monkey_lines[4].split()[5])
        false_monkey = int(curr_monkey_lines[5].split()[5])
        monkeys.append({"items": items,
                        "operation": operation,
                        "op_no": op_no,
                        "test_no": test_no,
                        "true_monkey": true_monkey,
                        "false_monkey": false_monkey,
                        "inspections": 0})
    return monkeys


if __name__ == "__main__":
    # part_one("data/day11.txt")
    part_two("data/day11.txt")
