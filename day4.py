def part_one(filepath: str):
    with open(filepath) as f:
        text = f.read()
    lines = text.split("\n")
    score: int = 0
    for line in lines:
        range1_s, range2_s = line.split(",")
        r1b, r1e = range1_s.split("-")
        r2b, r2e = range2_s.split("-")
        range_1 = set(range(int(r1b), int(r1e)+1))
        range_2 = set(range(int(r2b), int(r2e)+1))
        if range_1.issubset(range_2) or range_2.issubset(range_1):
            score += 1
    return score


def part_two(filepath: str):
    with open(filepath) as f:
        text = f.read()
    lines = text.split("\n")
    score: int = 0
    cont: bool = False
    for line in lines:
        range1_s, range2_s = line.split(",")
        r1b, r1e = range1_s.split("-")
        r2b, r2e = range2_s.split("-")
        range_1 = set(range(int(r1b), int(r1e)+1))
        range_2 = set(range(int(r2b), int(r2e)+1))
        for num in range_1:
            if num in range_2:
                score += 1
                cont = True
                break
        if cont:
            cont = False
            continue
    return score


if __name__ == "__main__":
    print(part_one("data\\day4.txt"))
    print(part_two("data\\day4.txt"))
