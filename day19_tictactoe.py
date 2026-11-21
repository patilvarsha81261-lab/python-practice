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