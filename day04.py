part1 = part2 = 0

for line in open(0):
    start1, stop1, start2, stop2 = map(int, line.replace(*"-,").split(","))
    part1 += (start1 - start2) * (stop1 - stop2) <= 0
    part2 += start1 <= stop2 and start2 <= stop1

print(part1, part2)  # 485 857
