from utils.data_reader import get_puzzle_input


def part1(data):
    priorities = 0
    for line in data:
        _sep = len(line) // 2
        items1, items2 = set(line[:_sep]), set(line[_sep:])
        badge = items1.intersection(items2).pop()
        priorities += ord(badge) - [38, 96][badge.islower()]
    return priorities


def part2(data):
    priorities = 0
    for i in range(0, len(data), 3):
        rucksack1, rucksack2, rucksack3 = map(set, data[i : i + 3])
        badge = rucksack1.intersection(rucksack2, rucksack3).pop()
        priorities += ord(badge) - [38, 96][badge.islower()]
    return priorities


def main():
    data = get_puzzle_input('03.txt')

    print(f'Puzzle 1: {part1(data)}')
    print(f'Puzzle 2: {part2(data)}')


if __name__ == '__main__':
    main()
