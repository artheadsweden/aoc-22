from collections import defaultdict
from itertools import accumulate
from utils.data_reader import get_puzzle_input


def solve(data, part):
    sizes = defaultdict(int)
    stack = []
    for line in data:
        if line.startswith("$ ls") or line.startswith("dir"):
            continue

        match line.split():
            case "$", "cd", "..":
                stack.pop()
            case "$", "cd", directory:
                stack.append(directory)
            case size, _:
                for path in accumulate(stack, func=lambda a, b: a + "/" + b):
                    sizes[path] += int(size)
    return sum(size for size in sizes.values() if size <= 100_000) if part == 1 else min(size for size in sizes.values() if size >= sizes["/"] - 40_000_000)


def main():
    data = get_puzzle_input('07.txt')
    print(f'Puzzle 1: {solve(data, 1)}')
    print(f'Puzzle 2: {solve(data, 2)}')


if __name__ == '__main__':
    main()
