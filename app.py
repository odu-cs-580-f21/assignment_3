from pprint import pprint
import time
import sys
start_time = time.time()

def find_next_empty(board):
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                return r, c
    return None, None

def is_valid(board, guess, row, col):
    row_val = board[row]
    if guess in row_val:
        return False
    
    col_val = [board[i][col] for i in range(9)]
    if guess in col_val:
        return False

    row_start = (row // 3) * 3
    col_start = (col // 3) * 3

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if board[r][c] == guess:
                return False
    return True

def solve(board):
    row, col = find_next_empty(board)
    if row == None:
        return True
    for guess in range(1, 10):
        if is_valid(board, guess, row, col):
            board[row][col] = guess
            if solve(board):
                pprint(board)
                return True
        board[row][col] = 0
    return False

if __name__ == '__main__':
    file = open(sys.argv[1], "r")
    board = []

    for line in file:
        row = []
        cleared_line = line.replace('\n', '')
        for ch in cleared_line:
            row.append(int(ch))
        board.append(row)

    solve(board)
    print("--- %s seconds ---" % (time.time() - start_time))
    file.close()