# special_tictactoe
Different version of a tictactoe in python, but with some (a lot) constraints.\
Yes, the code in this repo is ugly, the goal of this project is to code with constraints, so the exact opposite of clean code.\
This is the first time I try to do this type of stuff, so there is probably a lot of room for improvement.

## What is it ?
Here are different version of the famous tictactoe, to play in the terminal, depending on the version, it's 1 or 2 player and you can choose the map size. A map of size 3 is the standard grid, you need to do a line of the map's size to win.\
Each version was made with different constraints, from the easiest to the hardest.

## Why ?
Why not ? 
I wanted to do a tictactoe to learn to use PyGames, but as I started to do the code, I thought of a lot of things that I could do in single line.\
Hence, I had the idea to do a tictactoe with a lot of constraints, in the objective to learn new things, and make my brain work.\
(I still don't know anything about PyGame).

## How to use
* Clone the project
```
git clone git@github.com:nailec1911/special_tictactoe.git special_tictactoe
```
* Go into the folder (`cd special_tictactoe`)
* Launch the version that you want to play with
```
./tictactoe.py
or
./tictactoe_no_loop.py
...
```
* Enjoy !

## The different versions
Firstly, whatever the user do, the code must not crash.
### Main rules :
All the functions are just one line, meaning :
```python
def foo(param):
  return something(param)
```
A function can't have more than 4 parameters.\
As few lines as possible outside functions, so just what is needed to start the game.\
Obviously, I tried to make a DRY code, with a simple logic, no use of weird functions, no import, and 0 "powerful" keyword or function (like lambda).\
And has my code is always clean, there is no endless loop, no break, no continue ...

### First version
```
./tictactoe.py
```
In this version , the game will ask you to enter a number while the value you enter is wrong. The map is not resizable, and you can only play against the computer (which is really bad).\
I didn't add constraints in this version, the objective was to use it as a "base" for the other versions.

### Second version
```
./tictactoe_no_loop.py
```
#### New constraints : no loop
I replaced all the loop with recursion.\
Only one line outside of funtion (call of the first function to launch the game).\
In this version, you can change the map size (change the value in the last line ``init(size)``)


### Third version
```
./tictactoe_no_loop_no_ternary.py
```
#### New constraints : no ternary
Same constraints than the second version, but no ternary, so no ``if`` and ``else``.\
Only one line outside of funtion (call of the first function to launch the game).

### Fourth (and last) version
```
./tictactoe_oneline.py
```
In this version, you can change the map size, but you can also choose (at the begining of the game) if it is 1v1 or against the computer.\
I you input a wrong value (other than a number, or an occupied box), you loose. Sadly, I didn't find a way to ask again for input in one line. (for all numbers nb % size is used).\
#### New constraints : one line
This is exaclty what it says, there is only one line of code (I added comment to explain it).\
It is also without ternary (no ``if`` and ``else``).\
And it is a single condition, quite big, but just one.\
This mean that if you allow one line to create the count, you could do something like :
```python
i = 0
while (s := 3) and (the whole condition) and (i := i + 1): pass
```
So yes, this is a code without statement.
Declaring a variable on a previous line as above (with a while) also allow to do a loop for the input, so this is what I made in the oneline_bis version.
Exactly the same thing, but with a loop to ask for input.

## Conclusion
Here is the list of what I used for the one-line version
* variables (I can't do without)
  ```python
  i, board, player, s, not_endend, coord, line, col
  ```
  I could use less by using the same multiple time, but this is useless.

* operator (no, i didn't use '=' )
  ```python
  +, -, *, %, :=
  ```
* boolean stuff (I don't know the name)
  ```python
  True, False, and, or, ==
  ```
* loop (no infinite loop, no while)
  ```python
  for elt in list
  for i in range()
  ```
* keyword and function
  ```python
  in, print, all, isdigit, input, index, int
  ```
* other special characters
  ```python
  *, (), [], '', :, .
  ```

not a lot of things.

## More
### Golf version
The objective of code golf is to solve a problem in the least number of characters.\
I didn't use automatic golfer (some of them put your utf-8 code in utf-16, reducing by more than 50% the number of characters).\
As the objective is only to do short code, I did it with 0 constraints.\
Functionalities:
* 2 players or ai (choice at the beginning)
* any board size (change the first var `s=3` to the desired size)







