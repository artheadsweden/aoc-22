from utils.data_reader import get_puzzle_input, short

def solve(data):
    m1, m2, m3, e, z, rr, ii = short
    tt = [[*m3(ii, l)] for l in data]
    s = 0
    n = 2 * (z(tt[0]) + z(tt) - 2)
    for y in rr(1, z(tt) - 1):
        for x in rr(1, z(tt[0]) - 1):
            t = tt[y][x]
            if t > m1(m2(tt[y][:x]), m2(tt[y][x + 1 :]), m2([i[x] for i in tt][:y]), m2([i[x] for i in tt][y + 1 :])):
                n += 1
            r = (x if z([i for i, v in e(tt[y][:x][::-1]) if v - t >= 0]) == 0 else [i for i, v in e(tt[y][:x][::-1]) if v - t >= 0][0] + 1) * \
                (z(tt[0]) - x - 1 if z([i for i, v in e(tt[y][x + 1 :]) if v - t >= 0]) == 0 else [i for i, v in e(tt[y][x + 1 :]) if v - t >= 0][0] + 1) * \
                (y if z([i for i, v in e([i[x] for i in tt][:y][::-1]) if v - t >= 0]) == 0 else [i for i, v in e([i[x] for i in tt][:y][::-1]) if v - t >= 0][0] + 1) * \
                (z(tt) - y - 1 if z([i for i, v in e([i[x] for i in tt][y + 1 :]) if v - t >= 0]) == 0 else [i for i, v in e([i[x] for i in tt][y + 1 :]) if v - t >= 0][0] + 1)
            s = r if r > s else s
    return n, s


def main():
    data = get_puzzle_input('08.txt')
    one, two = solve(data)
    print(f'Puzzle 1: {one}')
    print(f'Puzzle 2: {two}')    


if __name__ == '__main__':
    main()
