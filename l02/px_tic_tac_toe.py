# board_ = [
#     ['.', '.', '.'] for n in range(3)
# ]
import string

board_ = ['.' for _ in range(9)]


def show_board(board):
    for idx, el in enumerate(board):
        print(el, ' ', end='')
        if (idx + 1) % 3 == 0:
            print()
    print()


def choose_position(board, player, pos):
    if pos not in string.digits or pos == '':
        print(f"Pos must be digit!")
        return False
    else:
        pos = int(pos)

    if pos not in [i for i in range(0, 9)]:
        print(f"Position {pos} is invalid. Allowed positions are between 0-8.")
        return False
    if board[pos] != '.':
        print(f"Position {pos} is is already occupied!")
        return False
    board[pos] = player
    return True


def iswinner(board, player):
    return any(player == board[a] == board[b] == board[c]
               for a, b, c in [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)])


turn = 0
show_board(board_)
while True:
    player = 'x' if turn % 2 == 0 else 'o'
    print(f"Turn {turn}. Current player is {player}")

    position = input()
    choose_position_success = choose_position(board_, player, position)
    if choose_position_success:
        turn += 1
    show_board(board_)
    if iswinner(board_, player):
        print(f"The winner is {player}")
        break

print("Game end")
