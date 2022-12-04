abc = [*" abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"]
three = {*abc}
part1 = part2 = 0
for i, items in enumerate(open(0)):
    half = len(items) // 2
    part1 += abc.index(({*items[:half]} & {*items[half:]}).pop())
    three &= {*items}
    if i % 3 == 2:
        part2 += abc.index(three.pop())
        three = {*abc}
print(part1, part2)  # 7716 2956
