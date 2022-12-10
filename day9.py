import numpy as np


def part_one(filepath: str):
    with open(filepath) as f:
        text = f.read()
    instructions = text.split("\n")
    positions = np.zeros((10000, 10000), dtype=np.int_)
    pos_head = np.array([5000, 5000])
    pos_tail = np.array([5000, 5000])
    movement = {
        "R": np.array([1, 0]),
        "L": np.array([-1, 0]),
        "U": np.array([0, 1]),
        "D": np.array([0, -1])
    }
    for i in instructions:
        direction, count = i.split(" ")
        for j in range(int(count)):
            pos_head = pos_head + movement[direction]
            pos_tail = tail_movement(pos_head, pos_tail)
            positions[pos_tail[0]][pos_tail[1]] = 1
    return np.count_nonzero(positions)


def tail_movement(head, tail):
    movement_vector = head - tail
    x, y = movement_vector
    tail_move = np.array([0, 0], dtype=np.int_)
    if abs(x)+abs(y) > 2:  # diagonal movement
        if abs(x) > 1:
            tail_move = np.array([x/2, y], dtype=np.int_)
        if abs(y) > 1:
            tail_move = np.array([x, y/2], dtype=np.int_)
    elif abs(x) > 1:
        tail_move = np.array([x/2, 0], dtype=np.int_)
    elif abs(y) > 1:
        tail_move = np.array([0, y/2], dtype=np.int_)
    new_tail_pos = (tail + tail_move)
    return new_tail_pos


def part_two(filepath: str, no_knots: int = 10):
    with open(filepath) as f:
        text = f.read()
    instructions = text.split("\n")
    tail_positions = np.zeros((10000, 10000), dtype=np.int_)
    pos_knots = [np.array([5000, 5000]) for x in range(no_knots)]
    movement = {
        "R": np.array([1, 0]),
        "L": np.array([-1, 0]),
        "U": np.array([0, 1]),
        "D": np.array([0, -1])
    }
    for i in instructions:
        direction, count = i.split(" ")
        for j in range(int(count)):
            pos_knots[0] = pos_knots[0] + movement[direction]
            for k in range(len(pos_knots)-1):
                pos_knots[k+1] = tail_movement(pos_knots[k], pos_knots[k+1])
            tail_positions[pos_knots[9][0], pos_knots[9][1]] = 1
        # d = np.count_nonzero(tail_positions)
        pass
    return np.count_nonzero(tail_positions)


if __name__ == "__main__":
    # print(f"Tail positions in part one: {part_one('data/day9.txt')}")
    print(f"Tail positions in part two: {part_two('data/day9.txt')}")
