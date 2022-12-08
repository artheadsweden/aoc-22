from utils.data_reader import get_puzzle_input


def solve(data):
    tt = [[*map(int, l)] for l in data]
    s = 0
    n = 2 * (len(tt[0]) + len(tt) - 2)
    for y in range(1, len(tt) - 1):
        for x in range(1, len(tt[0]) - 1):
            t = tt[y][x]
            if t > min(max(tt[y][:x]), max(tt[y][x + 1 :]), max([i[x] for i in tt][:y]), max([i[x] for i in tt][y + 1 :])):
                n += 1
            ls = x if len([i for i, v in enumerate(tt[y][:x][::-1]) if v - t >= 0]) == 0 else [i for i, v in enumerate(tt[y][:x][::-1]) if v - t >= 0][0] + 1
            rs = len(tt[0]) - x - 1 if len([i for i, v in enumerate(tt[y][x + 1 :]) if v - t >= 0]) == 0 else [i for i, v in enumerate(tt[y][x + 1 :]) if v - t >= 0][0] + 1
            ts = y if len([i for i, v in enumerate([i[x] for i in tt][:y][::-1]) if v - t >= 0]) == 0 else [i for i, v in enumerate([i[x] for i in tt][:y][::-1]) if v - t >= 0][0] + 1
            bs = len(tt) - y - 1 if len([i for i, v in enumerate([i[x] for i in tt][y + 1 :]) if v - t >= 0]) == 0 else [i for i, v in enumerate([i[x] for i in tt][y + 1 :]) if v - t >= 0][0] + 1
            s = ls * rs * ts * bs if ls * rs * ts * bs > s else s
    return n, s

def main():
    data = get_puzzle_input('08.txt')
    one, two = solve(data)
    print(f'Puzzle 1: {one}')
    print(f'Puzzle 2: {two}')    


if __name__ == '__main__':
    main()
