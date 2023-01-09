def range_pairs(nums):
    to_range = lambda *xs: range(min(xs), max(xs) + 1)
    return zip(map(to_range, nums[0::2], nums[2::2]), map(to_range, nums[1::2], nums[3::2]))

def solve(solid, flow, void=True):
    rocks = len(solid)
    floor = max(x.imag for x in solid)
    avail = lambda pos: pos not in solid and pos.imag < floor + 2
    while flow:
        pos = flow[-1]
        if next := [*filter(avail, (pos + 1 + 1j, pos - 1 + 1j, pos + 1j))]:
            flow.extend(next)
        else:
            if void and pos.imag >= floor:
                yield len(solid) - rocks
                void = False
            solid.add(flow.pop())
    yield len(solid) - rocks

solid = set()
for nums in ([*map(int, line.replace("->", ",").split(","))] for line in open(0)):
    solid |= {complex(x, y) for rx, ry in range_pairs(nums) for x in rx for y in ry}

print(*solve(solid, [500]))  # 1406 20870
