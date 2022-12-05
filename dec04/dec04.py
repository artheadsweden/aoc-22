from utils.data_reader import get_puzzle_input

def main():
    data = get_puzzle_input('04a.txt')

    split = lambda line: list(map(lambda section: tuple(map(int, section.split("-"))), line.split(",")))
    part1 = lambda data: sum([1 for s1, s2 in list(map(split, [line for line in data])) if (s1[0] - s2[0]) * (s1[1] - s2[1]) <= 0 ])
    part2 = lambda data: sum([1 for s1, s2 in list(map(split, [line for line in data])) if s2[0] <= s1[0] <= s2[1] or s1[0] <= s2[0] <= s1[1]])
    print(f'Puzzle 1: {part1(data)}')
    print(f'Puzzle 2: {part2(data)}')


if __name__ == '__main__':
    main()
