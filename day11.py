import math
import operator

class Monkey:
    def __init__(self, lines):
        _, items, op, div_test, dst_true, dst_false = lines.splitlines()
        self._items = [*map(int, items[18:].split(", "))]
        self._operator = {"*": operator.mul, "+": operator.add}[op[23]]
        self._operand = op[25:]
        self.div, *destinations = map(int, (div_test[21:], dst_true[29:], dst_false[30:]))
        self.dst = lambda worry: destinations[worry % self.div > 0]
        self.reset()

    def reset(self):
        self.items = self._items[:]
        self.num = 0
        return self

    def __call__(self, worry):
        if self._operand == "old":
            return worry ** 2
        return self._operator(worry, int(self._operand))

def play(monkeys, rounds=10_000, div=1):
    mod = math.prod(monkey.div for monkey in monkeys)
    for _ in range(rounds):
        for monkey in monkeys:
            monkey.num += len(monkey.items)
            items, monkey.items = monkey.items, []
            for item in items:
                worry = monkey(item) % mod // div
                monkeys[monkey.dst(worry)].items.append(worry)
    return math.prod(sorted(m.num for m in monkeys)[-2:])

monkeys = [*map(Monkey, open(0).read().split("\n\n"))]
print(play(monkeys, 20, 3), play([m.reset() for m in monkeys]))  # 54253, 13119526120
