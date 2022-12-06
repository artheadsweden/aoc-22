from utils.data_reader import get_puzzle_input

def solve(data, marker):
    for i in range(marker, len(data)):
        if len(set(data[:i][-marker:])) == marker:
            return i


def main():
    data = get_puzzle_input('06a.txt', is_raw=True, is_str=True)
    l = lambda d, m: [i for i in range(m, len(d)) if len(set(d[:i][-m:])) == m][0]
    print(f'Puzzle 1: {l(data, 4)}')
    print(f'Puzzle 2: {l(data, 14)}')


if __name__ == '__main__':
    main()
