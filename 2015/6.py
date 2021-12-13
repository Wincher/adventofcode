instructions = []
for line in open('../puzzleInput/2015/6.in'):
    l = line.split()
    if l[0]=='toggle':
        inst = (2, tuple(map(int, l[1].split(','))),tuple(map(int, l[3].split(','))))
    elif l[1]=='on':
        inst = (1, tuple(map(int, l[2].split(','))),tuple(map(int, l[4].split(','))))
    else:
        inst = (0, tuple(map(int, l[2].split(','))),tuple(map(int, l[4].split(','))))
    instructions.append(inst)
BOARD = [[False for _ in range(1000)] for _ in range(1000)]
for ins in instructions:
    inst, f, t = ins
    for i in range(f[0],t[0]+1):
        for j in range(f[1],t[1]+1):
            if inst==2:
                BOARD[i][j] = not BOARD[i][j]
            elif inst==0:
                BOARD[i][j] = False
            elif inst==1:
                BOARD[i][j] = True
sum = 0
for row in BOARD:
    for elem in row:
        if elem:
            sum+=1
print(f'part1: {sum}')
BOARD = [[0 for _ in range(1000)] for _ in range(1000)]
for ins in instructions:
    inst, f, t = ins
    for i in range(f[0],t[0]+1):
        for j in range(f[1],t[1]+1):
            if inst==2:
                BOARD[i][j]+=2
            elif inst==0:
                BOARD[i][j]=BOARD[i][j]-1 if BOARD[i][j]-1>=0 else 0
            elif inst==1:
                BOARD[i][j]+=1
sum = 0
for row in BOARD:
    for elem in row:
        sum+=elem
print(f'part2: {sum}')