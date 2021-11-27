from pprint import pprint
import time
import sys
start_time = time.time()

# This function scans the board in all valid ranges (9 x 9) and returns the first empty cell it finds.
# This function does not evaluate the weight of the scanned cell
# This means that the solving the cell might not be the most optimal path
# Returns None, None tuple if no empty cell is found.
def find_next_empty(board):
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                return r, c
    return None, None

# This function checks if the guess is valid and if the guess is a possible answer 
# Takes the board, the guess, the row, and column as an argument.
# Returns a boolean value depending on whether the guess is valid or not.
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

# Our recursive solver function that calls all previously defined functions.
# It takes in a board and returns a boolean value. 
# True if the board is solvable and solvable. 
# False if the board cannot be solved due to missing values or incorrect board set up. 
def solve(board):
    row, col = find_next_empty(board)
    if row == None:
        return True
    for guess in range(1, 10):
        if is_valid(board, guess, row, col):
            board[row][col] = guess
            if solve(board):
                return True
        board[row][col] = 0
    return False

# This is the main functions that runs on compilation
# It reads the terminal input for which board to solve
# It removes the newline character within the inputted board 
# It then adds each character in the board row and appends the rows to the board
# It then calls the solve function
# It then prints the board and the time it took to solve the board to the terminal
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
    pprint(board)
    print("--- %s seconds ---" % (time.time() - start_time))
    file.close()