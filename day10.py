import itertools

def int_or_zero(str):
    return int(str) if str[-1].isdecimal() else 0

ops = map(int_or_zero, open(0).read().split())

part1, part2 = 0, ""
for cycle, acc in enumerate(itertools.accumulate(ops, initial=1), start=1):
    part1 += (cycle % 40 == 20) * cycle * acc
    part2 += (cycle % 40 == 1) * "\n" + " #"[0 <= cycle % 40 - acc <= 2]

print(part1, part2)  # 13480 EGJBGCFK
