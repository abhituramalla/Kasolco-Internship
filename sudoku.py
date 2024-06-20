def is_valid(board, row, col, num):
    if num in board[row]:
        return False
    
    for r in range(9):
        if board[r][col] == num:
            return False
    
    box_row_start = 3 * (row // 3)
    box_col_start = 3 * (col // 3)
    for r in range(box_row_start, box_row_start + 3):
        for c in range(box_col_start, box_col_start + 3):
            if board[r][c] == num:
                return False
    
    return True

def solve_sudoku(board):
    empty_spot = find_empty_spot(board)
    if not empty_spot:
        return True
    
    row, col = empty_spot
    
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            
            if solve_sudoku(board):
                return True
            
            board[row][col] = 0
    
    return False 
def find_empty_spot(board):
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                return (r, c)
    return None

def print_board(board):
    for row in board:
        print(row)

board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

print("Sudoku puzzle to solve:")
print_board(board)
print("\nSolving...\n")

if solve_sudoku(board):
    print("Sudoku puzzle solved:")
    print_board(board)
else:
    print("No solution exists.")
