from utils.data_reader import get_puzzle_input
from string import ascii_uppercase

def create_stacks_procedures2(data):
    sep = [i for i, v in enumerate(data) if v == ""][0]
    cc = list(zip(*data[: sep - 1][::-1]))
    [cc.pop(p) for p in [i for i, c in enumerate(cc) if c[0] in "[] "][::-1]]
    crates = [list(filter(lambda x: x != " ", c)) for c in cc]
    crates.insert(0, [])
    return crates, data[sep + 1 :], max(map(int, data[sep - 1].split()))

def create_stacks_procedures(data):
    sep = [i for i, v in enumerate(data) if v == ""][0]

    crates = data[: sep - 1][::-1]
    stack_num = max(map(int, data[sep - 1].split()))
    stacks = [[] for _ in range(stack_num + 1)]
    for line in crates:
        items = [line[i] for i in range(1, len(line), 4)]
        for i, value in enumerate(items):
            if value != " ":
                stacks[i + 1].append(value)
    return stacks, data[sep + 1 :], stack_num


def solve(data, part):
    stacks, procedures, stack_num = create_stacks_procedures2(data)
    for line in procedures:
        _, a, _, b, _, c = [int(value) if i % 2 else value for i, value in enumerate(line.split())]
        stacks[c].extend(stacks[b][-a:][::-1]) if part == 1 else stacks[c].extend(stacks[b][-a:])
        del stacks[b][-a:]

    return "".join(stacks[i][-1] for i in range(1, stack_num + 1))


def main():
    data = get_puzzle_input('05.txt', is_raw=True)
    print(f'Puzzle 1: {solve(data, 1)}')
    print(f'Puzzle 2: {solve(data, 2)}')


if __name__ == '__main__':
    main()
