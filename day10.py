def part_one(filepath: str):
    with open(filepath) as f:
        text = f.read()
    instructions = text.split("\n")
    curr_x = 1
    cycles = []
    for i in instructions:
        if i.startswith("addx"):
            cycles.append(curr_x)
            cycles.append(curr_x)
            curr_x += int(i[5:])
        elif i.startswith("noop"):
            cycles.append(curr_x)

    # part one
    score: int = 0
    for i in range(1, 7):
        no = (i*40)-20
        curr_score = no * cycles[no-1]
        score += curr_score
        print(curr_score)
    print(score)

    # part two
    s = str()
    for i in range(len(cycles)):
        if cycles[i]+1 >= i%40 >= cycles[i]-1:
            s += "█"
        else:
            s += "░"
    for i in range(1, 7):
        print(s[((i*40)-40):(i*40)-1])


if __name__ == "__main__":
    part_one("data/day10.txt")
