from utils.data_reader import get_puzzle_input
def part1(data):
    col1 = {"A": 1, "B": 2, "C": 3}
    col2 = {"X": 1, "Y": 2, "Z": 3}
    scores = {"L": 0, "D": 3, "W": 6}
    
    total = 0
    
    for game in data:
        player1, player2 = game.split()
        player1 = col1[player1]
        player2 = col2[player2]


        match player2 - player1:
            case 0:
                total += 3
            case -2 | 1:
                total += 6
        total += player2

    return total
    
def part2(data):
    col1 = {"A": 1, "B": 2, "C": 3}
    col2 = {"X": 0, "Y": 3, "Z": 6}

    total_score = 0

    for line in data:
        player1, player2 = line.split()
        x = col1[player1]
        round_score = col2[player2]

        match round_score:
            case 6:  # win
                y = x % 3 + 1
            case 3:  # draw
                y = x
            case 0:  # loss
                y = (x + 1) % 3 + 1

        total_score += y + round_score
    return total_score

def main():
    data = get_puzzle_input('02a.txt')


    print(f'Puzzle 1: {part1(data)}')
    print(f'Puzzle 2: {part2(data)}')


if __name__ == '__main__':
    main()
