def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == row - i:
            return False
    return True

def solve(board, row):
    if row == len(board):
        print_board(board)
        return True
    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row] = col
            if solve(board, row + 1):
                return True
            board[row] = -1
    return False

def print_board(board):
    size = len(board)
    for i in range(size):
        row = ['Q' if board[i] == j else '.' for j in range(size)]
        print(" ".join(row))
    print()

# ---- Input from user ----
try:
    size = int(input("Enter board size (e.g., 8 for 8x8): "))
    if size < 4:
        print("Board size should be at least 4.")
    else:
        board = [-1] * size
        if not solve(board, 0):
            print("No solution exists.")
except ValueError:
    print("Please enter a valid number.")
