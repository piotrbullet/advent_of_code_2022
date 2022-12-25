def part_one(filepath: str):
    with open(filepath) as f:
        text = f.read()
    lines = text.split("\n")


if __name__ == "__main__":
    fpath = "data/day15.txt"
    fpath_ex = "data/day15_ex.txt"
    part_one(fpath_ex)