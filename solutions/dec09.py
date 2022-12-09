from utils.data_reader import get_puzzle_input


def solve(lines):
    def adjust(h_, t_):
        dr_ = (h_[0] - t_[0])
        dc_ = (h_[1] - t_[1])
        if abs(dr_) <= 1 and abs(dc_) <= 1:
            return t_
        elif abs(dr_) >= 2 and abs(dc_) >= 2:
            t_ = (h_[0] - 1 if t_[0] < h_[0] else h_[0] + 1, h_[1] - 1 if t_[1] < h_[1] else h_[1] + 1)
        elif abs(dr_) >= 2:
            t_ = (h_[0] - 1 if t_[0] < h_[0] else h_[0] + 1, h_[1])
        elif abs(dc_) >= 2:
            t_ = (h_[0], h_[1] - 1 if t_[1] < h_[1] else h_[1] + 1)
        return t_

    h = (0, 0)
    t = [(0, 0) for _ in range(9)]
    dr = {'L': 0, 'U': -1, 'R': 0, 'D': 1}
    dc = {'L': -1, 'U': 0, 'R': 1, 'D': 0}
    p1 = {t[0]}
    p2 = {t[8]}
    for line in lines:
        d, amt = line.split()
        amt = int(amt)
        for _ in range(amt):
            h = (h[0] + dr[d], h[1] + dc[d])
            t[0] = adjust(h, t[0])
            for i in range(1, 9):
                t[i] = adjust(t[i - 1], t[i])
            p1.add(t[0])
            p2.add(t[8])
    return len(p1), len(p2)


def main():
    data = get_puzzle_input('09.txt')
    one, two = solve(data)
    print(f'Puzzle 1: {one}')
    print(f'Puzzle 2: {two}')


if __name__ == '__main__':
    main()
