elves = open(0).read().split("\n\n")
calories = sorted(sum(map(int, elve.split())) for elve in elves)
print(calories[-1], sum(calories[-3:]))  # 67658, 200158
