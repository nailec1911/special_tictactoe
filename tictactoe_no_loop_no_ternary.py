#!/usr/bin/env python3

def check_all_win_possibilities(list_line, s):
    return (not len(list_line) == 0) and (list_line[0][0] != " " and list_line[0].count(list_line[0][0]) == s or check_all_win_possibilities(list_line[1:], s))

def add_col(board, count, s, sol):
    return not sol.append(board[count:s*s:s]) and ((count < s-1 and add_col(board, count + 1, s, sol)) or True)

def add_line(board, count, s, sol):
    return not sol.append(board[count:count + s]) and ((count + s < s * s and add_line(board, count + s, s, sol)) or True)

def is_win(board, p, s) -> bool:
    return (sol := [board[0:s*s:s+1], board[s-1:s*s-1:s-1]]) and add_col(board, 0, s, sol) and add_line(board, 0, s, sol) and check_all_win_possibilities(sol, s) and (not print(f"{p} win !!!"))

def is_draw(board):
    return not (" " in board or print("draw !!!"))

def display(board, size):
    return len(board) > 0 and ((size * size == len(board) and print("+-"*size+"+")) or (not print(f'|{board[0]}', end="")) and (len(board) % size - 1 == 0 and not print('|\n'+"+-"*size+"+") or True) and display(board[1:], size))

def end(board, p, size):
    return (display(board, size) or True) and (not is_win(board, p, size) and not is_draw(board))

def is_good_value(entry, s) -> bool:
    return ((entry.isdigit() and len(entry) > 0) and 0 <= int(entry) < s) or print("invalid number")

def ask_for(param, s):
    return ((((line := input(f"which {param} ? ")) and is_good_value(line, s)) or (line := ask_for(param, s))) and False) or int(line)

def valid_coord(board, coords) -> bool:
    return board[coords] == " " or print("already something, try an other")

def get_coords(board, s):
    return (((((coords := s * ask_for("line", s) + ask_for("col", s)) or True) and valid_coord(board, coords)) or (coords := get_coords(board, s))) and False) or coords

def update(board, ind, char):
    return board[:ind] + [char] + board[ind + 1:]

def game(board, size):
    return (board := update(board, get_coords(board, size), "x")) and end(board, "player", size) and (not print("\n")) and (board := update(board, board.index(" "), "o")) and end(board, "ia", size) and game(board, size)

def init(size):
    return game([' '] * size * size, size)

init(3)
