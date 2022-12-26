import collections

grid = open(0).read()
width, peak = grid.find("\n") + 1, grid.find("E")
deque, seen = collections.deque([(peak, 0)]), {peak}
final = ["S", "a"]
parts = []

def allowed(old, new):
    return ord(grid[old]) - ord(grid[new].replace("S", "a")) <= 1

while deque:
    old, dist = deque.popleft()
    if grid[old] in final:
        final.remove(grid[old])
        parts.insert(0, dist)
        if not final: break
    for new in (old + 1, old - 1, old + width, old - width):
        if new not in seen and 0 <= new < len(grid) and -new % width != 1 and allowed(old, new):
            seen.add(new)
            deque.append((new, dist + 1))

print(*parts)  # 472 465
