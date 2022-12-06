def sol(filepath: str, length: int):
    with open(filepath) as f:
        text = f.read()
    pos: int = 0
    letters = list()
    for letter in text:
        if len(set(letters)) == length:
            break
        pos += 1
        letters.append(letter)
        if len(letters) > length:
            letters.pop(0)
    return pos


if __name__ == "__main__":
    path = "data\\day6.txt"
    print(f"Part one: {sol(path, 4)}")
    print(f"Part two: {sol(path, 14)}")

