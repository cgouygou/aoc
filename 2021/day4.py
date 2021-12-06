import os
os.chdir("/home/cedric/Travail/AlgoInfo/CodesPython/adventofcode/2021/")

## Part 1 
data_str = open("input_day4.txt").read().splitlines()

def create_board(data, pos):
    board = []
    for k in range(5):
        board += list(map(int, data[pos+k].split()))
    return board

def is_winning(board):
    sum_lines = [sum(board[5*k:5*(k+1)]) for k in range(5)]
    sum_rows = [sum([board[5*i + k] for i in range(5)]) for k in range(5)]
    return 0 in sum_lines+sum_rows
    
draw_numbers = list(map(int, data_str[0].split(',')))

boards = [create_board(data_str, 2+6*k) for k in range((len(data_str)-2)//6)]

def find_winning_board(numbers, board_lst):
    for n in numbers:  
        for board in board_lst:
            if n in board:
                board[board.index(n)] = 0
                if is_winning(board):
                    return  n * sum(board)
            
print(find_winning_board(draw_numbers, boards))

## Part 2

def find_last_winning_board(numbers, board_lst):
    winning_boards = []
    for k, n in enumerate(numbers):
        if len(board_lst) == len(winning_boards):
            return numbers[k-1]* sum(winning_boards[-1])
        else:
            for board in board_lst:
                if board not in winning_boards:
                    if n in board:
                        board[board.index(n)] = 0
                    if is_winning(board):
                        winning_boards.append(board)

print(find_last_winning_board(draw_numbers, boards))
