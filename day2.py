def parse_file(filepath: str) -> list:
    with open(filepath) as f:
        text = f.read()
    pairs = text.split("\n")
    pairs_split = list()
    for element in pairs:
        game = element.split()
        pairs_split.append(game)
    return pairs_split


def part1_calc(path: str, letters: dict, logic: dict):
    games = parse_file(path)
    score: int = 0
    for el in games:
        opponent = letters[el[0]]
        player = letters[el[1]]
        if opponent == player:
            score += (3+player)
        elif logic[opponent] == player:
            score += (6+player)
        else:
            score += player
    return score


def part2_calc(path: str):
    games = parse_file(path)
    score: int = 0
    for el in games:
        opponent = el[0]
        outcome = el[1]
        if outcome == "X":  # lose
            score += GAME_LOGIC_PT2[LETTER_DICT[opponent]]
        elif outcome == "Y":  # draw
            score += 3 + LETTER_DICT[opponent]
        elif outcome == "Z":  # win
            score += 6 + GAME_LOGIC_PT1[LETTER_DICT[opponent]]
    return score


LETTER_DICT = {
    "A": 1, "B": 2, "C": 3,
    "X": 1, "Y": 2, "Z": 3
}

GAME_LOGIC_PT1 = {1: 2, 2: 3, 3: 1}
GAME_LOGIC_PT2 = {1: 3, 2: 1, 3: 2}

if __name__ == "__main__":
    print(part1_calc("data\\day2.txt", LETTER_DICT, GAME_LOGIC_PT1))
    print(part2_calc("data\\day2.txt"))
