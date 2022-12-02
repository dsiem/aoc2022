part1 = part2 = 0
for round in open(0).readlines():
    elf, other = map(ord, round.split())
    other -= 88
    part1 += ((other - elf) % 3) * 3 + other + 1
    part2 += ((other + elf) % 3) + 3 * other + 1
print(part1, part2)  # 12679 14470
