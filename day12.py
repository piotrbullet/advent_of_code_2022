def part_one(filepath: str):
    with open(filepath) as f:
        text = f.read()
    score: int = 0
    indices = list()
    pairs_text = text.split("\n\n")
    for n, p in enumerate(pairs_text):
        p1, p2 = p.split("\n")
        p1 = eval(p1)
        p2 = eval(p2)
        if compare_lists(p1, p2):
            indices.append(n + 1)
    score = sum(indices)
    print(f"Score for part 1: {score}")


def compare_lists(l1, l2) -> bool or None:
    if isinstance(l1, int) and isinstance(l2, int):
        return l1 < l2
    elif isinstance(l1, list) and isinstance(l2, list):
        for i in range(max([len(l1), len(l2)])):
            try:
                if l1[i] == l2[i] or compare_lists(l1[i], l2[i]) is None:
                    continue
                else:
                    return compare_lists(l1[i], l2[i])
            except IndexError:
                return len(l1) < len(l2)
        return None
    else:
        if isinstance(l1, int):
            return compare_lists([l1], l2)
        else:
            return compare_lists(l1, [l2])


def part_two(filepath: str):
    with open(filepath) as f:
        text = f.read()
    lines = text.split("\n")
    lines = [eval(x) for x in lines if not x == ""]
    correct_order: list = [False]
    while not all(correct_order):
        correct_order = []
        div_packets: list = []
        for i in range(len(lines)-1):
            l1 = lines[i]
            l2 = lines[i+1]
            if not compare_lists(l1, l2):
                lines[i] = l2
                lines[i+1] = l1
                correct_order.append(False)
            else:
                correct_order.append(True)
            if l1 == [[2]] or l1 == [[6]]:
                div_packets.append(i+1)
    print(div_packets)


if __name__ == "__main__":
    # part_one("data/day12.txt")
    part_two("data/day12.txt")
