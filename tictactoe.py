#!/usr/bin/env python3

def entire_line(line) -> bool:
    return False if " " in line else all(i == line[0] for i in line)

def check_all_win_possibilities(list_line) -> bool:
    return True in [entire_line(line) for line in list_line]

def is_win(board, p) -> bool:
    return not print(f"{p} win !!!") if check_all_win_possibilities([[board[i] for i in range(2, 8, 2)], [board[i] for i in range(0, 9, 4)], *[[board[i * 3 + j] for j in range(3)] for i in range(3)], *[[board[i + j * 3] for j in range(3)] for i in range(3)]]) else False

def is_draw(board):
    return not print("draw !!!") if not " " in board else False

def display(board):
    return not print(f"+-+-+-+\n|{board[0]}|{board[1]}|{board[2]}|\n+-+-+-+\n|{board[3]}|{board[4]}|{board[5]}|\n+-+-+-+\n|{board[6]}|{board[7]}|{board[8]}|\n+-+-+-+\n")

def end(board, p):
    return board if display(board) and (not is_win(board, p) and not is_draw(board)) else None

def is_good_value(entry) -> bool:
    return True if (0 <= int(entry) <= 2 if (entry.isdigit() and len(entry) > 0) else False) else print("invalid number")

def ask_for(param) -> str:
    return line if (line := input(f"which {param} ? ")) and is_good_value(line) else ask_for(param)

def valid_coord(board, coords) -> bool:
    return True if board[coords] == " " else print("already something, try an other")

def get_coords(board):
    return coords if (coords := 3 * int(ask_for("line")) + int(ask_for("col"))) and valid_coord(board, coords) else get_coords(board)

def update(board, ind, char):
    return [char if i == ind else elt for i, elt in enumerate(board)]

def turn(board):
    return end(update(board, get_coords(board), "x"), "player")

def ia(board):
    return end(update(board, board.index(" "), "o"), "ia")

board = [" " for i in range(9)]
while (board := turn(board)) and (board := ia(board)): pass
