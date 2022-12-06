from utils.data_reader import get_puzzle_input


def solver(data, part):
    col1 = {"A": 1, "B": 2, "C": 3}
    col2 = {"X": 1, "Y": 2, "Z": 3} if part == 1 else {"X": 0, "Y": 3, "Z": 6}
    total = 0
    for game in data:
        player1, player2 = game.split()
        player1 = col1[player1]
        player2 = col2[player2]

        if part == 1:
            match player2 - player1:
                case 0:
                    total += 3
                case -2 | 1:
                    total += 6
            total += player2
        else:
            match player2:
                case 6: 
                    total += player1 % 3 + 1
                case 3: 
                    total += player1
                case 0: 
                    total += (player1 + 1) % 3 + 1

            total += player2
    return total


def main():
    data = get_puzzle_input('02.txt')

    print(f'Puzzle 1: {solver(data, 1)}')
    print(f'Puzzle 2: {solver(data, 2)}')


if __name__ == '__main__':
    main()
