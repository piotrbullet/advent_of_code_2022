class Knot:
    def __init__(self):
        self.x: int = 0
        self.y: int = 0

    def get_pos(self) -> tuple:
        return self.x, self.y


class Head(Knot):
    def __int__(self):
        super().__init__()

    def move(self, direction: str):
        if direction == "U":
            self.y += 1
        elif direction == "D":
            self.y -= 1
        elif direction == "L":
            self.x -= 1
        elif direction == "R":
            self.x += 1


class Tail(Knot):
    def __init__(self):
        super().__init__()
        self.save_pos_history: bool = False
        self.pos_history: set = {(self.x, self.y)}

    def follow(self, head_pos: tuple):
        head_x, head_y = head_pos
        vector_x = head_x - self.x
        vector_y = head_y - self.y
        if abs(vector_x) > 1:
            self.x += int(vector_x/2)
            if vector_y > 0:
                self.y += 1
            elif vector_y < 0:
                self.y -= 1
        elif abs(vector_y) > 1:
            self.y += int(vector_y/2)
            if vector_x > 0:
                self.x += 1
            elif vector_x < 0:
                self.x -= 1
        if self.save_pos_history:
            self.pos_history.add((self.x, self.y))


def part_one(filepath: str):
    head = Head()
    tail = Tail()
    tail.save_pos_history = True
    with open(filepath) as f:
        text = f.read()
    instructions = text.split("\n")
    for i in instructions:
        direction, count = i.split(" ")
        for j in range(int(count)):
            head.move(direction)
            tail.follow(head.get_pos())
    print(f"PART ONE:\n"
          f"Unique tail positions: {len(tail.pos_history)}")


def part_two(filepath: str):
    head = Head()
    tails = [Tail() for _ in range(9)]
    tails[8].save_pos_history = True
    with open(filepath) as f:
        text = f.read()
    instructions = text.split("\n")
    for i in instructions:
        direction, count = i.split(" ")
        for j in range(int(count)):
            head.move(direction)
            tails[0].follow(head.get_pos())
            for k in range(1, len(tails)):
                tails[k].follow(tails[k-1].get_pos())
    print(f"PART TWO:\n"
          f"Unique tail positions: {len(tails[len(tails)-1].pos_history)}")


if __name__ == "__main__":
    path = "data/day9.txt"
    part_one(path)
    part_two(path)
