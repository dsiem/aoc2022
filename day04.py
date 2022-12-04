import re


part1 = part2 = 0
for line in open(0):
    start1, stop1, start2, stop2 = map(int, re.split("-|,", line))
    if (start1 <= start2 and stop1 >= stop2) or (start1 >= start2 and stop1 <= stop2):
        part1 += 1
    if start1 <= stop2 and start2 <= stop1:
        part2 += 1
print(part1, part2)  # 485 857
