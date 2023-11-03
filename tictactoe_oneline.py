#!/usr/bin/env python3

# my constraints :
# one line, one condition
# no infinite loop (and no break, continue or exit())
# no lambda
# no import (it would be a second line)
# no while

# this tictactoe can do all size (you'll have to do a line of 4 for a grid of size 4)
# change the 's' parameter (first on the line), to change the size


#                               | from here, the rest of the line is a single condition
for i in range((s := 3) * s + 1): (i == 0 and (not_ended := True) and (board := [' ' for i in range(s*s)]) and (player := 'x') and (vs_ia := input('1 vs 1 (Enter) or 1 vs ia (key + Enter) : '))) or not_ended and ((vs_ia and player == 'o' and ((coord := board.index(' ')) or True)) or ((((line := input('Which line ? ')) or True) and line.isdigit() and ((col := input('Which col ? ')) or True) and col.isdigit() and (((coord := s * (int(line)%s) + (int(col)%s))) or True) and board[coord] == ' ') or (not_ended := False) or print('wrong input, you lose'))) and (board := board[:coord] + [player] + board[coord + 1:]) and (not print(''.join([('+-'*s+'+\n|')+'|'.join(board[i*s:i*s+s])+'|\n' for i in range(s)]) + '+-'*s+'+\n')) and (not (True in [all(i == line[0] for i in line) and not ' ' in line for line in [board[s-1:s*s-1:s-1], board[0:s*s:s+1], *[board[i*3:i*3+s:1] for i in range(s)], *[board[i:s*s:s] for i in range(s)]]] and not print(player, 'win !!!')) and (' ' in board or print('draw !!!')) or (not_ended := False)) and (player == 'o' and (player := 'x') or (player := 'o'))
#                    ^           #            var to check the end              empty board creation        init the player           ask if one or two player                                   # if game is ended #  if ia turn, chose the coordinates to play         ^     #    #                                     get input and check if it is a number                                                 #       get the index of the corresponding box            check that the box is free       end if input isn't correct                               #                   update the board                        #                    | between lines |        | create the line      |                         last line     #                 check that all the char in the line are the same,                    diagonal 1            diagonal 2       #             lines                   #  #                columns           #        win !!!!                 #       if there is no more spaces          if win or draw        #  #                        if player == o :               #
#                    |           #      (False if wrong input, win or draw)                                                                                                                      # do nothing until #  the ia is always playing the first empty space    ^     #    #---------------------------------------------------------------------------------------------------------------------------#                                                                                                               (calling print is equal to false)   #        change the box choosen by the player               #                                                                                                            #                   but not blank (as the board is full of blank)                          creat a list with all the possibilities of winning, then create a list full of bool for each possibilities                                       #              it's a draw                   end the game         #  #                            player = x                 #
#              size to change    #                                                                                                                                                               # loop is finished #                                                    ^     #                                                                                         if the input is invalid (not a number, already something, the player loose)                 if this part result in False (player loose), as it is followed by an and                       #                                                           #  display the board                    all lines are concatenated with '+-+-+' (between lines)              #                                                                                           (true if line is entirely the same player, else false), if there is a true in this list, it is a win                                            # if not win------------------------------------------------------#  #                        else :                         #
# impossible to do more turn that#                      initialisation on the first loop                                                                                                         #------------------+                                  needed because elt := 0 #   if player turn use wait for input, and asign it to coord with a calcul                                                                                                            the end of the line will not be executed (and the loop will do nothing until its ended)        #-----------------------------------------------------------#  this part is always True             results are then joined together to form an only string ( +last line)#                                                                                                                                                                                                                                                                                                                #  update the player         player = o                 #
# the number of boxes, so not an +---------------------------------------------------------------------------------------------------------------------------------------------------------------+                  #                                 is considered as False   #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#                                                           #------------------------------------------------------------------------------------------------------------# check the win or loose, end with True if continue, false (and not_endend = False), if the game is winned (or draw)                                                                                                                                                                                             #-------------------------------------------------------#
# infinite loop                                                                                                                                                                                                     +----------------------------------------------------------+



#here is the same code but with no statement
# i = 0
# while (s := 3) and ((i == 0 and (not_ended := True) and (board := [' ' for i in range(s*s)]) and (player := 'x') and (vs_ia := input('1 vs 1 (Enter) or 1 vs ia (key + Enter) : '))) or not_ended and ((vs_ia and player == 'o' and ((coord := board.index(' ')) or True)) or ((((line := input('Which line ? ')) or True) and line.isdigit() and ((col := input('Which col ? ')) or True) and col.isdigit() and (((coord := s * (int(line)%s) + (int(col)%s))) or True) and board[coord] == ' ') or (not_ended := False) or print('wrong input, you lose'))) and (board := board[:coord] + [player] + board[coord + 1:]) and (not print(''.join([('+-'*s+'+\n|')+'|'.join(board[i*s:i*s+s])+'|\n' for i in range(s)]) + '+-'*s+'+\n')) and (not (True in [all(i == line[0] for i in line) and not ' ' in line for line in [board[s-1:s*s-1:s-1], board[0:s*s:s+1], *[board[i*3:i*3+s:1] for i in range(s)], *[board[i:s*s:s] for i in range(s)]]] and not print(player, 'win !!!')) and (' ' in board or print('draw !!!')) or (not_ended := False)) and (player == 'o' and (player := 'x') or (player := 'o'))) and (i := i + 1): pass



#Here is a list of the python keyword, opeartor, function ... that I used

# variable (hard to do without, I could use less by using the same one muliple time, but it would be ugly)
# i, board, player, s, not_endend, coord, line, col

# operator (no = !!!)
# :=, +, -, *, %

# boolean or condition related :
# and, or, ==, True, False

# loop (no infinite loop, no while)
# for elt in list, for i in range()

# other keyword or funtion :
# in, print, all, isdigit, input, index, int

#special character:
# (), [], '', :, .
