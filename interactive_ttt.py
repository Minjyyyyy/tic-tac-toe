# Interactive Tic-Tac-Toe AI (Minimax)

import math

def print_board(board):
    for i in range(0, 9, 3):
        print(board[i], "|", board[i+1], "|", board[i+2])
    print()

def check_winner(board):
    wins = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]
    for a,b,c in wins:
        if board[a] == board[b] == board[c] != " ":
            return board[a]
    return None

def moves_left(board):
    return " " in board

def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == "O": return 1
    if winner == "X": return -1
    if not moves_left(board): return 0

    if is_maximizing:
        best = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, depth+1, False)
                board[i] = " "
                best = max(best, score)
        return best
    else:
        best = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, depth+1, True)
                board[i] = " "
                best = min(best, score)
        return best

def best_move(board):
    best_score = -math.inf
    move = None
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, 0, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    return move

# ----- Interactive Game -----
board = [" "] * 9
print("Welcome to Tic-Tac-Toe! You are X, AI is O.\n")
print_board(board)

while moves_left(board) and check_winner(board) is None:
    # Player move
    while True:
        try:
            player_move = int(input("Enter your move (0-8): "))
            if board[player_move] == " ":
                board[player_move] = "X"
                break
            else:
                print("Cell occupied, choose another.")
        except:
            print("Invalid input. Enter a number from 0 to 8.")
    
    # Print board
    print_board(board)
    
    # Check for winner
    if check_winner(board) is not None or not moves_left(board):
        break

    # AI move
    ai_move = best_move(board)
    board[ai_move] = "O"
    print("AI chooses position:", ai_move)
    print_board(board)

# Final result
winner = check_winner(board)
if winner == "X":
    print("You win! 🎉")
elif winner == "O":
    print("AI wins! 🤖")
else:
    print("It's a draw! 🤝")
