import Lib.os

list = []
i = 0
j = 0
for i in range(3):
    new = []
    for j in range(3):
        new.insert(j, j)
        j += 1
    list.append(new)
    i += 1
print(list)

X = input('Player #1: ')
O = input('Player #2: ')
print('Player #1: ' + X, 'Your Sign Is: X\n' 'Player #2: ' +
      O, 'Your Sign Is: O\n' 'Let\'s Play Tic Tac Toe!\n')

x_element = 'X'
o_element = 'O'

x_move = int(input('X, Move\n'))
list.insert(x_move, x_element)
print(x_move)
o_move = int(input('O, Move\n'))
list.insert(o_move, o_element)
print(o_move)
print(list)



