#!/usr/bin/env python3

def check_all_win_possibilities(list_line, s):
    return (not len(list_line) == 0) and (list_line[0][0] != " " and list_line[0].count(list_line[0][0]) == s or check_all_win_possibilities(list_line[1:], s))

def get_col(board, count, l, s):
    return [board[count:l:s]] + get_col(board, count + 1, l, s) if count < 2 else [board[count:l:s]]

def get_line(board, count, l, s):
    return [board[count:count + s]] + get_line(board, count + s, l, s) if count + s < l else [board[count:count + s]]

def is_win(board, p, lenght, s) -> bool:
    return not print(f"{p} win !!!") if check_all_win_possibilities([board[0:lenght:s+1], board[s-1:lenght-1:s-1], *get_col(board, 0, lenght, s), *get_line(board, 0, lenght, s)], s) else False

def is_draw(board):
    return not print("draw !!!") if not " " in board else False

def display(board, l, size):
    return (not print("+-"*size+"+") if l == len(board) else True) and (not print(f'|{board[0]}', end="")) and (not print('|\n'+"+-"*size+"+") if len(board) % size - 1 == 0 else True) and display(board[1:], l, size) if len(board) > 0 else True

def end(board, p, lenght, size):
    return board if display(board, lenght, size) and (not is_win(board, p, lenght, size) and not is_draw(board)) else None

def is_good_value(entry, size):
    return True if (0 <= int(entry) < size if (entry.isdigit() and len(entry) > 0) else False) else print("invalid number")

def ask_for(param, size):
    return line if (line := input(f"which {param} ? ")) and is_good_value(line, size) else ask_for(param, size)

def valid_coord(board, coords):
    return True if board[coords] == " " else print("already something, try an other")

def get_coords(board, size):
    return coords if (coords := size * int(ask_for("line", size)) + int(ask_for("col", size))) and valid_coord(board, coords) else get_coords(board, size)

def update(board, ind, char):
    return board[:ind] + [char] + board[ind + 1:]

def turn(board, lenght, size):
    return end(update(board, get_coords(board, size), "x"), "player", lenght, size)

def ia(board, lenght, size):
    return end(update(board, board.index(" "), "o"), "ia", lenght, size)

def game(board, size):
    return game(board, size) if (board := turn(board, len(board), size)) and (board := ia(board, len(board), size)) else None

def init(size):
    return game([' '] * size * size, size)


init(4)
