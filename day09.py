def sign(z):
    return complex((z.real > 0) - (z.real < 0), (z.imag > 0) - (z.imag < 0))

dirs = {"R": 1, "L": -1, "U": 1j, "D": -1j}
rope = [0] * 10
seen = [{0}, {0}]

for move in open(0):
    dir, n = dirs[move[0]], int(move[2:])
    for _ in range(n):
        rope[0] += dir
        for i in range(1, len(rope)):
            dist = rope[i - 1] - rope[i]
            rope[i] += sign(dist) * (abs(dist) >= 2)
        seen[0].add(rope[1])
        seen[1].add(rope[-1])

print(*map(len, seen))  # 6197 2562
