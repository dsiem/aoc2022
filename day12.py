import collections

grid = open(0).read()
width = grid.find("\n") + 1

def allowed(old, new):
    return ord(grid[old]) - ord(grid[new].replace("S", "a")) <= 1

def find_shortest(start_pos, destinations):
    deque, seen = collections.deque([(start_pos, 0)]), {start_pos}
    while deque and destinations:
        old, dist = deque.popleft()
        if (dest := grid[old]) in destinations:
            destinations.remove(dest)
            yield dest, dist
        for new in (old + 1, old - 1, old + width, old - width):
            if new not in seen and 0 <= new < len(grid) and -new % width != 1 and allowed(old, new):
                seen.add(new)
                deque.append((new, dist + 1))

shortest = dict(find_shortest(grid.find("E"), ["S", "a"]))
print(shortest["S"], shortest["a"])  # 472 465
