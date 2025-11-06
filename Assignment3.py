import math

def print_board(board):
    for row in board:
        print(" | ".join(cell if cell != "" else " " for cell in row))
        print("-" * 5)

def is_moves_left(board):
    return any(' ' in row or '' in row for row in board)

def evaluate(board):
    # Rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] in ['X', 'O']:
            return 10 if row[0] == 'X' else -10
    # Columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] in ['X', 'O']:
            return 10 if board[0][col] == 'X' else -10
    # Diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] in ['X', 'O']:
        return 10 if board[0][0] == 'X' else -10
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] in ['X', 'O']:
        return 10 if board[0][2] == 'X' else -10
    return 0

def minimax(board, depth, is_max):
    score = evaluate(board)
    if score in [10, -10]:
        return score
    if not is_moves_left(board):
        return 0

    if is_max:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] in [' ', '']:
                    board[i][j] = 'X'
                    best = max(best, minimax(board, depth + 1, False))
                    board[i][j] = ' '
        return best
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] in [' ', '']:
                    board[i][j] = 'O'
                    best = min(best, minimax(board, depth + 1, True))
                    board[i][j] = ' '
        return best

def find_best_move(board):
    best_val = -math.inf
    best_move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] in [' ', '']:
                board[i][j] = 'X'
                move_val = minimax(board, 0, False)
                board[i][j] = ' '
                if move_val > best_val:
                    best_move, best_val = (i, j), move_val
    return best_move

# Example usage
if __name__ == "__main__":
    board = [
        ['X', 'O', 'X'],
        ['O', 'X', 'X'],
        [' ', ' ', '']
    ]
    
    print("Current board:")
    print_board(board)
    
    best_move = find_best_move(board)
    print(f"\nThe best move for X is at: {best_move}\n")
    
    # Apply the best move to board
    if best_move != (-1, -1):
        board[best_move[0]][best_move[1]] = 'X'
    
    print("Board after best move:")
    print_board(board)
