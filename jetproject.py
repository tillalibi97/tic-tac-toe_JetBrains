cells = ("         ")
def grids (x):

    cells = x
    print('---------')
    print('|', *x[:3], '|')
    print('|', *x[3:6], '|')
    print('|', *x[6:], '|')
    print('---------')

grids(cells)

def inp ():
    while True:
        try:
            a1, a2 = map(int, input('Enter the coordinates:').split())
            if a1 <= 0 or a1 > 3 or a2 <= 0 or a2 > 3:
                print("Coordinates should be from 1 to 3!")
                continue
        except ValueError:
            print('You should enter numbers!')
            continue
        else:
            return a1, a2

def coord (x,y):
    s = [(i,j) for i in range(1,4) for j in range(1,4)]
    return s.index((x,y))

a1, a2 = inp()
def move ():
    global cells
    if cells[coord(a1,a2)] == ' ' or cells[coord(a1,a2)] == '_':
        ind = coord(a1,a2)
        if cells.count('X') == 0 or cells.count('X') == cells.count('O'):
            cells = cells[:ind] + "X" + cells[ind + 1:]
            grids(cells)
        else:
            cells = cells[:ind] + "O" + cells[ind + 1:]
            grids(cells)

def comb_check ():
    global cells, comb
    comb = [cells[:3], cells[6:], cells[3:6], cells[0::3],
            cells[1::3], cells[2::3], cells[2:7:2], cells[0::4]]
    if 'XXX' in comb:
        grids(cells)
        print('X wins')
        exit()
    elif 'OOO' in comb:
        grids(cells)
        print('O wins')
        exit()
    elif cells.count(' ') == 0:
        grids(cells)
        print('Draw')
        exit()

def check():
    global cells, a1, a2, co1, co2
    while cells[coord(a1, a2)] != ' ' and cells[coord(a1, a2)] != '_':
        print('This cell is occupied! Choose another one!')
        a1, a2 = inp()
    else:
        move()
        comb_check()
        a1, a2 = inp()
counter = 0
while counter < 1:
    check()
