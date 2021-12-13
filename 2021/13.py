
from typing import DefaultDict

BOARD = DefaultDict(int)
instrucations = []
for line in open('../puzzleInput/2021/13.in'):
    if line.strip()=='':
        continue
    if line[0].isnumeric():
        x,y = line.strip().split(',')
        BOARD[(int(x),int(y))]=1
    else:
        x,y = line.strip().split()[2].split('=')
        instrucations.append((x, int(y)))
sum = 0
# print(len([k for k,v in BOARD.items()]), 'len after init')
part1 = False
for inst in instrucations:
    BOARD2 = DefaultDict(int)
    i,v = inst
    for k,val in BOARD.items():
        xx,yy = k
        # print(xx,yy, i, v)
        if i=='x':
            if xx>=v:
                BOARD2[(2*v-xx,yy)]+=1
            else:
                BOARD2[xx,yy]=1
        elif i=='y':
            if yy>=v:
                BOARD2[(xx,2*v-yy)]+=1
            else:
                BOARD2[xx,yy]=1
    BOARD = BOARD2
    if not part1:
        print(f'part1: {len([k for k,v in BOARD.items()])}')
        part1=True
max_x = 0
max_y = 0
for k,v in BOARD.items():
    x,y = k
    max_x = max(max_x,x)
    max_y = max(max_y,y)
M = [['.' for _ in range(max_x+1)] for _ in range(max_y+1)]
for x,y in BOARD.keys():
    M[y][x] = '#'
print('part2:')
for row in M:
    print(''.join(row))