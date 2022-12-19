sizes = {"": 0}

for line in open(0):
    match line.split():
        case ["$", "cd", "/"]:
            path = []
        case ["$", "cd", ".."]:
            path.pop()
        case ["$", "cd", dir]:
            path.append(dir)
            sizes["/".join(path)] = 0
        case [size, _] if size.isnumeric():
            for n in range(len(path)+1):
                sizes["/".join(path[:n])] += int(size)

needed = sizes[""] - 40000000
print(sum(s for s in sizes.values() if s <= 100000), min(s for s in sizes.values() if s >= needed))
# 1315285 9847279
