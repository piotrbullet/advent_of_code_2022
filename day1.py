import sys

if __name__ == "__main__":
    with open("data\\day1.txt") as f:
        day1_data = f.read()
        elves = day1_data.split("\n\n")
        elves_cal = list()
        for e in elves:
            elves_cal.append([int(e) for e in e.split("\n")])
        calories_summed = [sum(c) for c in elves_cal]
        max_cal = max(calories_summed)
        print(max_cal)
        sorted_cal = sorted(calories_summed)
        top3 = [sorted_cal[-1], sorted_cal[-2], sorted_cal[-3]]
        top3_sum = sum(top3)
        print(top3_sum)
