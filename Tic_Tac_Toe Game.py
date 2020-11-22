"""
(1, 3) (2, 3) (3, 3)
(1, 2) (2, 2) (3, 2)
(1, 1) (2, 1) (3, 1)
"""
def grid():
    var1 = (f'''
    ---------     ( User Cordinate Manual )
    | {matrix[0][0]} {matrix[0][1]} {matrix[0][2]} |     |  (1, 3) (2, 3) (3, 3)  | 
    | {matrix[1][0]} {matrix[1][1]} {matrix[1][2]} |     |  (1, 2) (2, 2) (3, 2)  |
    | {matrix[2][0]} {matrix[2][1]} {matrix[2][2]} |     |  (1, 1) (2, 1) (3, 1)  |
    ---------
    ''')
    return var1
#Functions Used in the Progamme
def check(i, grid):
    for y in range(0, 3):
        if grid[y][0] == grid[y][1] == grid[y][2] == i:
            return True
        elif grid[0][y] == grid[1][y] == grid[2][y] == i:
            return True
        elif grid[0][0] == grid[1][1] == grid[2][2] == i:
            return True
        elif grid[0][2] == grid[1][1] == grid[2][0] == i:
            return True
def which_player_wins(argument, player1, player2):
    if argument == 'X':
        print(f'Congratulations "{player1}"  X Wins')
    elif argument == 'O':
        print(f'Congratulations "{player2}"  O Wins')


matrix = [[' ', ' ', ' '] for _ in range(3)]
print(f'"X" is for Player-1 "O" is for Player-2')
print()
player_1= input('Enter Player-1 Name:- ').upper().replace(' ', '')
player_2= input('Enter Player-2 Name:- ').upper().replace(' ', '')
print()
print(f'Setting X is for "{player_1}", O is for "{player_2}"')
print(grid())

counter = 1
mark = 'X'
while True:
    if counter % 2 != 0:
        mark = 'X'
        print(f'{player_1}')
    else:
        mark = 'O'
        print(f'{player_2}')
    try:
        draw_check = [i for z in matrix for i in z if i == ' ']
        if not draw_check:
            print('Draw')
            break
        x, y = input('Please Enter the coordinates: ').split()
        x = int(x)
        y = int(y)
        if y >= 4 or y<= 0:
            print('Coordinates should be from 1 to 3!')
            continue
        if matrix[3 - y][x - 1] == ' ':
            matrix[3 - y][x - 1] = mark
            print(grid())
            counter += 1
            continue
        else:
            print('This cell is occupied! Choose another one!')
            continue
    except ValueError:
        print('You should enter numbers!')
        continue
    except IndexError:
        print('Coordinates should be from 1 to 3!')
        continue
    finally:
        if check(mark, matrix):
            grid()
            which_player_wins(mark, player_1, player_2)
            break

