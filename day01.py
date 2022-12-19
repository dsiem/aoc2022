elves = open(0).read().split("\n\n")
calrs = sorted(sum(map(int, elve.split())) for elve in elves)
print(calrs[-1], sum(calrs[-3:]))  # 67658, 200158
