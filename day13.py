def compare(a, b):
    match a[0], b[0]:
        case a_, b_ if a_ == b_:
            return compare(a[1:], b[1:])
        case "]", _:
            return True
        case _, "]":
            return False
        case "[", b_:
            return compare(a[1:], f"{b_}]{b[1:]}")
        case a_, "[":
            return compare(f"{a_}]{a[1:]}", b[1:])
        case a_, b_:
            return a_ < b_

packets = [line.replace("10", ":") for line in open(0) if line.strip()]

part1 = sum(i for i, ordered in enumerate(map(compare, packets[::2], packets[1::2]), 1) if ordered)
part2 = sum((compare(p, "[[2]]") for p in packets), 1) * sum((compare(p, "[[6]]") for p in packets), 2)
print(part1, part2)  # 6420 22000
