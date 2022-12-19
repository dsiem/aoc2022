abcde = [*" abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"]
three = {*abcde}
part1 = part2 = 0

for i, items in enumerate(open(0)):
    half = len(items) // 2
    part1 += abcde.index(({*items[:half]} & {*items[half:]}).pop())
    three &= {*items}
    if i % 3 == 2:
        part2 += abcde.index(three.pop())
        three = {*abcde}

print(part1, part2)  # 7716 2956
