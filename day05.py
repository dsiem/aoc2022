lines = open(0).readlines()
stacks = [*("".join(x).strip() for x in zip(*(f" {crates[1::4]:<9}" for crates in lines[:8])))]
both = (stacks, stacks[:])
for moves in lines[10:]:
    n, src, dst = map(int, moves.split()[1::2])
    for stacks, mode in zip(both, (-1, 1)):
        stacks[src], stacks[dst] = stacks[src][n:], stacks[src][:n][::mode] + stacks[dst]
print(*("".join(stack[0] for stack in stacks[1:]) for stacks in both))  # CVCWCRTVQ CNSCZWLVT
