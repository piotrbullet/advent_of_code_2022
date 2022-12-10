def add_entry(dirs: dict, path: list, file_name: str, size: int):
    if path[0] not in dirs.keys():
        dirs[path[0]] = dict()
    if len(path) > 1:
        add_entry(dirs[path[0]], path[1:], file_name, size)
    else:
        dirs[path[0]][file_name] = size
    return dirs


def make_directories(filepath: str):
    with open(filepath) as f:
        text = f.read()
    commands = text.split("\n")
    path = list()
    dirs = dict()
    for i in range(len(commands)):
        if commands[i].startswith("$ cd .."):
            path.pop()
        elif commands[i].startswith("$ cd"):
            path.append(commands[i][5:])
        elif commands[i].split()[0].isnumeric():
            size, name = commands[i].split()
            dirs = add_entry(dirs, path, name, size)
    return dirs


def count(dirs: dict, limit_size: int):
    size: int = 0
    for k in dirs.keys():
        if isinstance(dirs[k], dict):
            size += count(dirs[k], limit_size)
        else:
            size += int(dirs[k])
    if size < limit_size:
        global SCORE
        SCORE += size
    return size


def get_smallest_valid_folder(dirs: dict, limit_size):
    size: int = 0
    for k in dirs.keys():
        if isinstance(dirs[k], dict):
            size += get_smallest_valid_folder(dirs[k], limit_size)
        else:
            size += int(dirs[k])
    global SMALLEST_FOLDER_SIZE
    if SMALLEST_FOLDER_SIZE > size > limit_size:
        SMALLEST_FOLDER_SIZE = size
    return size


if __name__ == "__main__":
    SCORE = 0
    SMALLEST_FOLDER_SIZE = 30000000000
    # pt 1
    d = make_directories("data\\day7.txt")
    total_size = count(d, 100000)
    # pt 2
    disc_space = 70000000
    space_needed = 30000000
    LIMITER = space_needed-(disc_space-total_size)

    get_smallest_valid_folder(d, LIMITER)
    print(f"Total size of small folders: {SCORE}")
    print(f"Smallest folder: {SMALLEST_FOLDER_SIZE}")
