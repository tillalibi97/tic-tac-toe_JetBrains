cells = ("         ")
def grids (x):

    cells = x
    print('---------')
    print('|', *x[:3], '|')
    print('|', *x[3:6], '|')
    print('|', *x[6:], '|')
    print('---------')

grids(cells)
numbers = ('0123456789')
numbers1 = ('123')

def inp ():
    global co1, co2, a
    a = input('Enter the coordinates:')
    co1 = [x for x in a if x in numbers]
    co2 = [x for x in a if x in numbers1]
    x, y = a[0], a[2]
    return x, y

def coord (x,y):
    s = [(i,j) for i in range(1,4) for j in range(1,4)]
    return s.index((x,y))

a1, a2 = inp()
def move ():
    global cells
    if cells[coord(int(a1),int(a2))] == ' ' or cells[coord(int(a1),int(a2))] == '_':
        ind = coord(int(a1),int(a2))
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
    while co1 == [] or len(co1) == 1:
        print('You should enter numbers!')
        a1, a2 = inp()
        if len(co1) > 1:
            break
    while len(co2) != 2 or len(a) > 3:
        print('Coordinates should be from 1 to 3!')
        a1, a2 = inp()
        if len(co2) == 2 and len(a) == 3:
            break
    while cells[coord(int(a1), int(a2))] != ' ' and cells[coord(int(a1), int(a2))] != '_':
        print('This cell is occupied! Choose another one!')
        a1, a2 = inp()
    else:
        move()
        comb_check()
        a1, a2 = inp()
counter = 0
while counter < 1:
    check()
