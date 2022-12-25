def part_one(filepath: str, starting_point: tuple):
    with open(filepath) as f:
        text = f.read()
    lines = text.split("\n")
    rocks_coordinates = set()
    lowest_y: int
    for l in lines:
        xy_list = [(int(x), int(y)) for x, y in [x.split(",") for x in l.split(" -> ")]]
        for i in range(len(xy_list)-1):
            rocks_coordinates = add_rocks(rocks_coordinates, xy_list[i], xy_list[i+1])
    sand_coordinates = add_sand(rocks_coordinates)
    # print_map(range(493, 505), range(0, 11), rocks_coordinates, sand_coordinates)
    print(len(sand_coordinates))


def add_rocks(rocks: set, c1: tuple, c2: tuple) -> set:
    if c2[0] - c1[0]:
        starting_x: int = min(c1[0], c2[0])
        fin_x: int = max(c1[0], c2[0])
        for x in range(starting_x, fin_x+1):
            rocks.add((x, c1[1]))
    elif c2[1] - c1[1]:
        starting_y: int = min(c1[1], c2[1])
        fin_y: int = max(c1[1], c2[1])
        for y in range(starting_y, fin_y+1):
            rocks.add((c1[0], y))
    else:
        raise RuntimeError("Vectors are not being calculated properly in the add_rocks funtion")
    return rocks


def print_map(range_x: range, range_y: range, rocks: set, sand: set):
    for y in range_y:
        line = ""
        for x in range_x:
            if (x, y) not in rocks and (x, y) not in sand:
                # line += "⚪"
                line += "."
            elif (x, y) in sand:
                # line += "⚫"
                line += "o"
            elif (x, y) in rocks:
                # line += "⛔"
                line += "#"
            else:
                line += "chuj"
        print(line)


def add_sand(rocks: set, starting_point: tuple = (500, 0)) -> set:
    sand: set = set()
    lowest_y = get_lowest_rock_y(rocks)
    falling_forever: bool = False
    while not falling_forever:
        # print_map(range(493, 505), range(0, 11), rocks, sand)
        x, y = starting_point
        while True:
            if y == lowest_y:
                falling_forever = True
                break
            elif (x, y+1) in sand or (x, y+1) in rocks:
                if (x-1, y+1) not in sand and (x-1, y+1) not in rocks:
                    x -= 1
                    y += 1
                elif (x+1, y+1) not in sand and (x+1, y+1) not in rocks:
                    x += 1
                    y += 1
                else:
                    sand.add((x, y))
                    break
            else:
                y += 1
    return sand


def get_lowest_rock_y(rocks: set) -> int:
    lowest_y: int = 0
    for r in rocks:
        if r[1] > lowest_y:
            lowest_y = r[1]
    return lowest_y


def part_two(filepath: str, starting_point: tuple = (500, 0)):
    with open(filepath) as f:
        text = f.read()
    lines = text.split("\n")
    rocks_coordinates = set()
    lowest_y: int
    for l in lines:
        xy_list = [(int(x), int(y)) for x, y in [x.split(",") for x in l.split(" -> ")]]
        for i in range(len(xy_list)-1):
            rocks_coordinates = add_rocks(rocks_coordinates, xy_list[i], xy_list[i+1])
    rock_bottom = get_lowest_rock_y(rocks_coordinates) + 2
    rocks_coordinates = add_rocks(rocks_coordinates, (0, rock_bottom), (1000, rock_bottom))
    sand_coordinates = add_sand_2(rocks_coordinates)
    # print_map(range(493, 505), range(0, 11), rocks_coordinates, sand_coordinates)
    print(len(sand_coordinates))


def add_sand_2(rocks: set, starting_point: tuple = (500, 0)) -> set:
    sand: set = set()
    lowest_y = get_lowest_rock_y(rocks)
    finished: bool = False
    while not finished:
        # print_map(range(480, 520), range(0, 12), rocks, sand)
        x, y = starting_point
        while True:
            if (500, 0) in sand:
                finished = True
                break
            elif (x, y+1) in sand or (x, y+1) in rocks:
                if (x-1, y+1) not in sand and (x-1, y+1) not in rocks:
                    x -= 1
                    y += 1
                elif (x+1, y+1) not in sand and (x+1, y+1) not in rocks:
                    x += 1
                    y += 1
                else:
                    sand.add((x, y))
                    break
            else:
                y += 1
    return sand


if __name__ == "__main__":
    sp = (500, 0)
    # part_one("data/day14_ex.txt", sp)
    part_two("data/day14.txt")
