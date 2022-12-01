from utils.data_reader import get_puzzle_input


def main():
    data = get_puzzle_input('01a.txt')
    items = sorted([sum(map(int, item.split("\n"))) for item in "\n".join(data).split("\n\n")], reverse=True)
    print(f'Puzzle 1: {items[0]}')
    print(f'Puzzle 2: {sum(items[:3])}')


if __name__ == '__main__':
    main()
