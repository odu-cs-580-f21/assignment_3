# CS 480/580 - Assignment_3 - Dániel B. Papp

# How to run

```console
python3 app.py [input board .txt file]
```

# How it works

The program takes a text file as input and outputs the solved board to the terminal. The program consists of 3 different parts:

## Finding the empty cells

The purpose of this function is to scans the board in all valid ranges (9 x 9 as defined by our board size) and returns the **first** empty cell it finds. Do note that this function does not weight the importance of the found cell based on the values around it as a human or better AI would. Since it is a lot easier to find an empty cell's value the more values are around it, the solution found might not be the shortest and most optimal path to the solution.

_Returns None, None if no empty cell are left on the board._

```python
def find_next_empty(board):
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                return r, c
    return None, None
```

## Evaluating the guess validity

The purpose of this function is to checks if the guess found by the AI is valid in the context of the board and the values around it. The function takes the board as an argument in order to evaluate the validity of the guess. It also takes the guess as an argument. Furthermore, it takes the the row, and column as an argument in order to be able to identify the smaller box (3 x 3) on the board we are validating against. The function returns a boolean value depending on whether the guess is valid or not.

```python
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
```

## Solving the board

This function calls all of our previously defined functions. With the board as an argument it can find the **first** empty cell on our board. If it cannot find an empty cell on the board it returns True, since that would mean that our board is solved. If there are empty cells present it loops over every integer in the range of 1 through 9 inclusively. It then passes the number into our validator function defined above. If the validator function returns True the program inserts the guess into the board at the appropriate position. It then checks if the board is solved using recursion, meaning it will pass the updated board as an argument and as noted above the first things that the function does is it checks for empty cells on the board. If that condition is True the board is solved. If that condition is False we change the value back to 0 as a backtracking technique. If the for loop runs through all the numbers in the range of 1 through 9 without finding a solution the program will return False, meaning the board is unsolvable.

```python
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
```

# Test cases

I ran tests with different board difficulties and recorded the time it took to solve the board. The results are as follows:

_Bolded and italicized values on the board are the given constants. The inputted boards can also be seen in this repository with their respective difficulty as their file name._

|              | Number of given values in the board | Time it took to solve | Solved board                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ------------ | ----------------------------------- | --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Basic board  | 31                                  | 0.0031 seconds        | 4, 8, **_3_**, 9, **_2_**, 1, **_6_**, 5, 7, <br/> **_9_**, 6, 7, **_3_**, 4, **_5_**, 8, 2, **_1_**, <br/> 2, 5, **_1_**, **_8_**, 7, **_6_**, **_4_**, 9, 3, <br/> 5, 4, **_8_**, **_1_**, 3, **_2_**, **_9_**, 7, 6, <br/> **_7_**, 2, 9, 5, 6, 4, 1, 3, **_8_**, <br/> 1, 3, **_6_**, **_7_**, 9, **_8_**, **_2_**, 4, 5, <br/> 3, 7, **_2_**, **_6_**, 8, **_9_**, **_5_**, 1, 4, <br/> **_8_**, 1, 4, **_2_**, 5, **_3_**, 7, 6, **_9_**, <br/> 6, 9, **_5_**, 4, **_1_**, 7, **_3_**, 8, 2 <br/> |
| Evil board   | 26                                  | 0.1768 seconds        | 7, **_1_**, 6, **_2_**, 4, 3, 9, 8, **_5_**, <br/> **_5_**, 4, 3, 1, 8, **_9_**, 7, 2, 6, <br/> **_2_**, **_8_**, 9, 7, 5, 6, **_3_**, 1, 4, <br/> 1, **_3_**, 8, **_9_**, **_7_**, **_5_**, 6, 4, **_2_**, <br/> 9, 2, 5, 4, 6, 1, 8, 3, 7, <br/> **_6_**, 7, 4, **_8_**, **_3_**, **_2_**, 5, **_9_**, 1, <br/> 8, 6, **_1_**, 5, 9, 4, 2, **_7_**, **_3_**, <br/> 3, 9, 2, **_6_**, 1, 7, 4, 5, **_8_**, <br/> **_4_**, 5, 7, 3, 2, **_8_**, 1, **_6_**, 9 <br/>                                     |
| Devil board  | 22                                  | 1.1556 seconds        | 6, 1, 7, **_2_**, 4, 3, **_8_**, **_9_**, 5, <br/> 2, **_4_**, 3, 8, 5, 9, 6, 1, **_7_**, <br/> **_9_**, 8, 5, 1, 7, **_6_**, 4, **_3_**, 2, <br/> 4, 5, 6, **_3_**, **_9_**, 7, **_1_**, 2, 8, <br/> 8, 2, 9, 4, 1, 5, 7, **_6_**, 3, <br/> 3, **_7_**, 1, 6, **_8_**, 2, 5, **_4_**, **_9_**, <br/> 1, 9, 8, **_7_**, 3, **_4_**, **_2_**, 5, 6, <br/> 7, 3, 2, 5, 6, 1, 9, **_8_**, **_4_**, <br/> 5, **_6_**, 4, 9, 2, **_8_**, **_3_**, 7, 1 <br/>                                                 |
| Custom board | 10                                  | 0.0061 seconds        | 1, 3, 5, **_2_**, 4, 6, 7, 9, 8, <br/> 2, **_4_**, 7, 8, 3, 9, 1, 5, 6, <br/> 6, 8, 9, 1, 5, 7, 4, **_3_**, 2, <br/> 4, 1, 2, **_3_**, 6, 5, 8, 7, 9, <br/> 3, 9, 8, 4, 7, 2, 5, **_6_**, 1, <br/> 5, 7, 6, 9, **_8_**, 1, 3, 2, 4, <br/> 8, 6, 1, **_7_**, 9, 3, **_2_**, 4, 5, <br/> 9, 2, 3, 5, 1, 4, 6, **_8_**, 7, <br/> 7, 5, 4, 6, 2, **_8_**, 9, 1, 3                                                                                                                                           |

As we can observe if the number of values given is so low that the number of possible solutions are high. This means that our AI can solve the problem quicker than other boards since it can have a higher number of solutions. The hardest board for the AI would be a board that only has 1 solution but still has a lot of empty cells. This would force the AI to run through a lot of guesses in the `solve` function's loop, which then would increase our time to completion.
