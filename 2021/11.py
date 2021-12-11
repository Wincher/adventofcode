
BOARD = []
result = 0
for line in open('../puzzleInput/2021/11.in'):
    line = [int(i) for i in line.strip()]
    BOARD.append(line)
# print(BOARD)
rl = len(BOARD)
cl = len(BOARD[0])
ro = [1,1,1,0,0,-1,-1,-1]
co = [-1,0,1,-1,1,0,-1,1]
def flash(i, j):
    global result
    BOARD[i][j]=(BOARD[i][j]+1)
    if BOARD[i][j]==10:
        result+=1
        for k in range(len(ro)):
            ii=i+ro[k]
            jj=j+co[k]
            if ii in range(rl) and jj in range(cl):
                flash(ii,jj)
for _ in range(100):
    for i in range(rl):
        for j in range(cl):
            flash(i,j)
    for i in range(rl):
        for j in range(cl):
            if BOARD[i][j]>9:
                BOARD[i][j]=0
print(f'part1: {result}')
while True:
    for i in range(rl):
        for j in range(cl):
            flash(i,j)
    ok = True
    for i in range(rl):
        for j in range(cl):
            if BOARD[i][j]>9:
                BOARD[i][j]=0
            else:
                ok = False
    if ok:
        print(f'part2: {_+1}')
        break