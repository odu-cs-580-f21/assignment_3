file = open('board.txt', "r")

counter = 0
board = []
DOMAIN = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for line in file:
    board.append(line.replace('\n', ''))
    counter += 1


print('Our board \n')
for line in board:
    print(line, '\t') 

print('\n')

def checkBox(pos:int):
    pass

def checkCol(pos:int):
    domain = DOMAIN
    col_index = 0
    col_nums = []
    for col in board:
        col_nums.append(int(board[col_index][pos]))
        col_index += 1
    
    for num in col_nums:
        if num in domain:
            domain.remove(num)
        else:
            pass

    return domain

def checkRow(pos:int):
    domain = DOMAIN
    row_index = 0
    row_nums = []
    for row in board:
        row_nums.append(int(board[pos][row_index]))
        row_index += 1
    
    for num in row_nums:
        if num in domain:
            domain.remove(num)
        else:
            pass

    return domain

def getDomain(row, col):
    bigDomain = row + col

    temp_list = []

    for i in bigDomain:
        if i not in temp_list:
            temp_list.append(i)

    bigDomain = temp_list

    return bigDomain


print(getDomain(checkRow(1), checkCol(1)))