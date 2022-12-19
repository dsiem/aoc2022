import numpy as np

trees = np.genfromtxt(open(0), dtype=int, delimiter=1)
part1 = np.zeros_like(trees)
part2 = np.ones_like(trees)
index = np.arange(len(trees))
for _ in range(4):
    lower = np.triu(trees[..., None] <= trees[:, None], 1)
    part1 |= ~lower.any(2)
    part2 *= lower.argmax(2) + np.where(lower.any(2), -index, index[::-1])
    trees, part1, part2 = map(np.rot90, (trees, part1, part2))
print(part1.sum(), part2.max())  # 1705 371200
