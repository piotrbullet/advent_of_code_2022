import pandas as pd
import numpy as np


def part_one(filepath: str):
    with open(filepath) as f:
        text = f.read()
    no_cols = len(text.split("\n")[0])
    no_rows = len(text.split("\n"))
    map_arr = np.array(pd.read_fwf(filepath, widths=[1 for x in range(no_cols)], header=None), dtype=np.int_)
    visible_trees_arr = np.zeros((no_rows, no_cols), dtype=np.int_)
    for i in range(4):
        pass
        for curr_row in range(no_rows):
            curr_high = -1
            for curr_col in range(no_cols):
                curr_tree = map_arr[curr_row][curr_col]
                if curr_tree > curr_high:
                    visible_trees_arr[curr_row][curr_col] = 1
                    curr_high = curr_tree
                if curr_high == 9:
                    break
        map_arr = np.rot90(map_arr)
        visible_trees_arr = np.rot90(visible_trees_arr)
    print(np.count_nonzero(visible_trees_arr))


def part_two(filepath: str):
    with open(filepath) as f:
        text = f.read()
    no_cols = len(text.split("\n")[0])
    no_rows = len(text.split("\n"))
    map_arr = np.array(pd.read_fwf(filepath, widths=[1 for x in range(no_cols)], header=None), dtype=np.int_)
    top_score: int = 0
    best_coordinates = tuple()
    for curr_row in range(no_rows):
        for curr_col in range(no_cols):
            curr_tree = map_arr[curr_row][curr_col]
            score_right: int = 0
            score_left: int = 0
            score_down: int = 0
            score_top: int = 0
            for cf in range(curr_col+1, no_cols):
                height = map_arr[curr_row][cf]
                score_right += 1
                if height >= curr_tree:
                    break
            for cb in list(reversed(list(range(0, curr_col)))):  # columns numbers going backwards towards 0
                height = map_arr[curr_row][cb]
                score_left += 1
                if height >= curr_tree:
                    break
            for rf in range(curr_row+1, no_rows):
                height = map_arr[rf][curr_col]
                score_down += 1
                if height >= curr_tree:
                    break
            for rb in list(reversed(list(range(0, curr_row)))):  # rows numbers going backwards towards 0
                height = map_arr[rb][curr_col]
                score_top += 1
                if height >= curr_tree:
                    break
            score = score_top * score_down * score_right * score_left
            if score > top_score:
                top_score = score
                best_coordinates = (curr_row, curr_col)
    print(f"Top score: {top_score}")
    print(f"Best coordinates are: {best_coordinates}")


if __name__ == "__main__":
    part_one("data/day8.txt")
    part_two("data/day8.txt")
