#!/usr/bin/env python3

# mostly same than the one-line, but the declaration of i allow to ask again for the input
# if the input was incorrect, everything is ignored until it loop back to the input

# i = 0 start
# i = 1 in game
# i = 2 wrong input
i = 0
while (s := 3) and ((i == 0 and (i := 1) and (board := [' ' for i in range(s*s)]) and (player := 'x') and (vs_ia := input('1 vs 1 (Enter) or 1 vs ia (key + Enter) : '))) or ((vs_ia and player == 'o' and ((coord := board.index(' ')) or True)) or (((((line := input('Which line ? ')) or True) and line.isdigit() and ((col := input('Which col ? ')) or True) and col.isdigit() and (((coord := s * (int(line)%s) + (int(col)%s))) or True) and board[coord] == ' ') and (i := 1)) or print("Wrong value") or (i := 2))) and i == 2 or (board := board[:coord] + [player] + board[coord + 1:]) and (not print(''.join([('+-'*s+'+\n|')+'|'.join(board[i*s:i*s+s])+'|\n' for i in range(s)]) + '+-'*s+'+\n')) and (not (True in [all(i == line[0] for i in line) and not ' ' in line for line in [board[s-1:s*s-1:s-1], board[0:s*s:s+1], *[board[i*3:i*3+s:1] for i in range(s)], *[board[i:s*s:s] for i in range(s)]]] and not print(player, 'win !!!')) and (' ' in board or print('draw !!!')) or (not_ended := False)) and (player == 'o' and (player := 'x') or (player := 'o'))): pass
