def get_file_text(filepath: str):
    with open(filepath) as f:
        text = f.read()
    return text


def parse_text_into_pairs(text: str) -> list:
    result = list()
    line_split: list = text.split("\n")
    for element in line_split:
        brkpt = int(len(element) / 2)
        result.append((element[:brkpt], element[brkpt:]))
    return result


def part_one(pairs: list):
    score: int = 0
    for one, two in pairs:
        unique_one = set(one)
        unique_two = set(two)
        common = [e for e in unique_one if e in unique_two][0]
        score += PRIORITIES[common]
    return score


def part_two(text: str):
    score: int = 0
    line_split: list = text.split("\n")
    length: int = int(len(line_split)/3)
    for i in range(length):
        r1 = set(line_split[i*3])
        r2 = set(line_split[1+(i*3)])
        r3 = set(line_split[2+(i*3)])
        common = [e for e in r1 if e in r2 and e in r3][0]
        score += PRIORITIES[common]
    return score


PRIORITIES = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12,
              "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21, "v": 22, "w": 23,
              "x": 24, "y": 25, "z": 26, "A": 27, "B": 28, "C": 29, "D": 30, "E": 31, "F": 32, "G": 33, "H": 34,
              "I": 35, "J": 36, "K": 37, "L": 38, "M": 39, "N": 40, "O": 41, "P": 42, "Q": 43, "R": 44, "S": 45,
              "T": 46, "U": 47, "V": 48, "W": 49, "X": 50, "Y": 51, "Z": 52}

if __name__ == "__main__":
    result_part_one = part_one(parse_text_into_pairs(get_file_text("data\\day3.txt")))
    result_part_two = part_two(get_file_text("data\\day3.txt"))
    print(result_part_two)
    pass
