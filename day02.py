part1 = part2 = 0

for round in open(0):
    first, other = map(ord, round.split())
    other -= 88
    part1 += ((other - first) % 3) * 3 + other + 1
    part2 += ((other + first) % 3) + 3 * other + 1

print(part1, part2)  # 12679 14470
