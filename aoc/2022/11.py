# Part 2: We keep track the remainders of each item divided by all divisors
import copy


def throw_item(to_monkey, item):
    to_monkey.items.append(item)


class Monkey:

    ALL_MONKEYS = None
    DIVISORS = None

    def __init__(self, starting_items, operation, test):
        self.items = starting_items
        self.operation = operation
        self.test = test
        self.inspect_cnt = 0

    def inspect_part_1(self):
        for item in self.items:
            item = int(self.operation(item)) // 3
            divisorition = item % self.test["divisor"] == 0
            throw_item(Monkey.ALL_MONKEYS[self.test[divisorition]], item)
        self.inspect_cnt += len(self.items)
        self.items.clear()

    def inspect_part_2(self):
        for item in self.items:
            item = tuple(self.operation(r) % d for d, r in zip(Monkey.DIVISORS, item))

            divisorition = item[Monkey.DIVISORS.index(self.test["divisor"])] == 0
            throw_item(Monkey.ALL_MONKEYS[self.test[divisorition]], item)
        self.inspect_cnt += len(self.items)
        self.items.clear()


SIMPLE_TEST_CASE = {
    "0": Monkey(
        starting_items=[79, 98],
        operation=lambda x: x * 19,
        test={"divisor": 23, True: "2", False: "3"},
    ),
    "1": Monkey(
        starting_items=[54, 65, 75, 74],
        operation=lambda x: x + 6,
        test={"divisor": 19, True: "2", False: "0"},
    ),
    "2": Monkey(
        starting_items=[79, 60, 97],
        operation=lambda x: x * x,
        test={"divisor": 13, True: "1", False: "3"},
    ),
    "3": Monkey(
        starting_items=[74],
        operation=lambda x: x + 3,
        test={"divisor": 17, True: "0", False: "1"},
    ),
}

FULL_TEST_CASE = {
    "0": Monkey(
        starting_items=[91, 66],
        operation=lambda x: x * 13,
        test={"divisor": 19, True: "6", False: "2"},
    ),
    "1": Monkey(
        starting_items=[78, 97, 59],
        operation=lambda x: x + 7,
        test={"divisor": 5, True: "0", False: "3"},
    ),
    "2": Monkey(
        starting_items=[57, 59, 97, 84, 72, 83, 56, 76],
        operation=lambda x: x + 6,
        test={"divisor": 11, True: "5", False: "7"},
    ),
    "3": Monkey(
        starting_items=[81, 78, 70, 58, 84],
        operation=lambda x: x + 5,
        test={"divisor": 17, True: "6", False: "0"},
    ),
    "4": Monkey(
        starting_items=[60],
        operation=lambda x: x + 8,
        test={"divisor": 7, True: "1", False: "3"},
    ),
    "5": Monkey(
        starting_items=[57, 69, 63, 75, 62, 77, 72],
        operation=lambda x: x * 5,
        test={"divisor": 13, True: "7", False: "4"},
    ),
    "6": Monkey(
        starting_items=[73, 66, 86, 79, 98, 87],
        operation=lambda x: x * x,
        test={"divisor": 3, True: "5", False: "2"},
    ),
    "7": Monkey(
        starting_items=[95, 89, 63, 67],
        operation=lambda x: x + 2,
        test={"divisor": 2, True: "1", False: "4"},
    ),
}


def part_1():
    Monkey.ALL_MONKEYS = copy.deepcopy(FULL_TEST_CASE)

    ROUNDS = 20

    for _ in range(ROUNDS):
        for monkey in Monkey.ALL_MONKEYS.values():
            monkey.inspect_part_1()

    all_inspect_cnt = [monkey.inspect_cnt for monkey in Monkey.ALL_MONKEYS.values()]
    all_inspect_cnt.sort(reverse=True)
    mk_level = all_inspect_cnt[0] * all_inspect_cnt[1]
    print("Part 1:", mk_level)


def part_2():
    Monkey.ALL_MONKEYS = copy.deepcopy(FULL_TEST_CASE)
    Monkey.DIVISORS = list(
        sorted(monkey.test["divisor"] for monkey in Monkey.ALL_MONKEYS.values())
    )

    # Convert number to list of remainders
    for monkey in Monkey.ALL_MONKEYS.values():
        monkey.items = [
            tuple(item % d for d in Monkey.DIVISORS) for item in monkey.items
        ]

    ROUNDS = 10000
    for _ in range(ROUNDS):
        for monkey in Monkey.ALL_MONKEYS.values():
            monkey.inspect_part_2()

    all_inspect_cnt = [monkey.inspect_cnt for monkey in Monkey.ALL_MONKEYS.values()]
    all_inspect_cnt.sort(reverse=True)
    mk_level = all_inspect_cnt[0] * all_inspect_cnt[1]
    print("Part 2:", mk_level)


if __name__ == "__main__":
    part_1()
    part_2()
