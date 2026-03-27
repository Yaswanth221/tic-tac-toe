board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

current_player = "X"

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-"*9)

def is_draw(board):
    for row in board:
        if " " in row:
            return False
    return True

def check_win(board, player):

    for row in board:
        if row[0] == row[1] == row[2] == player:
            return True
    
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True

    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    
    return False

while True:
    print("current player:", current_player)
    print_board(board)

    row = int(input("Enter a row(0-2):"))
    col = int(input("Enter a col(0-2):"))

    if row < 0 or col > 2 or col < 0 or row > 2:
        print("Invalid position:")
        continue
    if board[row][col] != " ":
        print("postion has filled already") 
        continue

    board[row][col] = current_player

    if check_win(board, current_player):
        print_board(board)
        print(f"{current_player} wins!")
        break

    if is_draw(board):
        print_board(board)
        print("It is draw")
        break

    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"
