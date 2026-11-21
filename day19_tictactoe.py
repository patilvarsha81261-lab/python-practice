#Simple code for tic-tac-toe game

board = [" "] * 9
wins = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)]
player = "X"
winner = None

for turn in range(9):
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])

    move = int(input("Player " + player + ", choose a square (1-9): ")) - 1
    board[move] = player

    for a, b, c in wins:
        if board[a] == board[b] == board[c] == player:
            winner = player

    if winner:
        break

    if player == "X":
        player = "O"
    else:
        player = "X"

if winner:
    print("Player", winner, "wins!")
else:
    print("It's a draw!")




# day19_tictactoe.py
import random

WINS = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)]


def show_board(board):
    # empty squares show their number, so you know what to type
    cells = [board[i] if board[i] != " " else str(i + 1) for i in range(9)]
    print()
    print(f" {cells[0]} | {cells[1]} | {cells[2]}")
    print("---+---+---")
    print(f" {cells[3]} | {cells[4]} | {cells[5]}")
    print("---+---+---")
    print(f" {cells[6]} | {cells[7]} | {cells[8]}")
    print()


def winner(board):
    for a, b, c in WINS:
        if board[a] != " " and board[a] == board[b] == board[c]:
            return board[a]
    return None


def get_human_move(board, player):
    while True:
        try:
            move = int(input(f"Player {player}, choose a square (1-9): ")) - 1
        except ValueError:
            print("Please type a number from 1 to 9")
            continue

        if move < 0 or move > 8:
            print("Choose between 1 and 9")
        elif board[move] != " ":
            print("That square is already taken")
        else:
            return move


def computer_move(board, me, other):
    empty = [i for i in range(9) if board[i] == " "]

    # 1. win if possible, 2. otherwise block the other player
    for symbol in (me, other):
        for square in empty:
            board[square] = symbol
            wins_here = winner(board) == symbol
            board[square] = " "
            if wins_here:
                return square

    # 3. take the centre, 4. otherwise pick randomly
    if 4 in empty:
        return 4
    return random.choice(empty)


def play_game(vs_computer):
    board = [" "] * 9
    player = "X"

    for turn in range(9):
        show_board(board)

        if vs_computer and player == "O":
            move = computer_move(board, "O", "X")
            print(f"Computer chooses square {move + 1}")
        else:
            move = get_human_move(board, player)

        board[move] = player

        if winner(board):
            show_board(board)
            print(f"Player {player} wins!")
            return player

        player = "O" if player == "X" else "X"

    show_board(board)
    print("It's a draw!")
    return None


print("=== TIC-TAC-TOE ===")
print("1. Two players")
print("2. Play against the computer")
mode = input("Choose (1-2): ")
vs_computer = mode == "2"

score = {"X": 0, "O": 0, "Draw": 0}

while True:
    result = play_game(vs_computer)

    if result is None:
        score["Draw"] += 1
    else:
        score[result] += 1

    print(f"\nScore - X: {score['X']}   O: {score['O']}   Draws: {score['Draw']}")

    if input("Play again? (y/n): ").lower() != "y":
        print("Thanks for playing!")
        break