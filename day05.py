lines = open(0).readlines()
stack = [*("".join(x).strip() for x in zip(*(f" {crates[1::4]:<9}" for crates in lines[:8])))]
parts = (stack, stack[:])

for moves in lines[10:]:
    n, src, dst = map(int, moves.split()[1::2])
    for stack, mode in zip(parts, (-1, 1)):
        stack[src], stack[dst] = stack[src][n:], stack[src][:n][::mode] + stack[dst]

print(*("".join(s[0] for s in stack[1:]) for stack in parts))  # CVCWCRTVQ CNSCZWLVT
