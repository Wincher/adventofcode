from collections import defaultdict

BOARD = defaultdict(int)
l = (0,0)
BOARD[l]=1
h = {
    '^': 1,
    'v': -1,
}
v = {
    '<': -1,
    '>': 1,
}
for o in open('../puzzleInput/2015/3.in').read():
    x, y = l
    if o in h.keys():
       x +=h[o] 
    if o in v.keys():
       y +=v[o] 
    l = (x,y)
    BOARD[l]+=1
print(f'part1: {len([ val for k,val in BOARD.items() if val > 0])}')

BOARD = defaultdict(int)
l = (0,0)
lr = (0,0)
BOARD[l]=2
h = {
    '^': 1,
    'v': -1,
}
v = {
    '<': -1,
    '>': 1,
}
robot = False
for o in open('../puzzleInput/2015/3.in').read():
    x, y = l if not robot else lr
    if o in h.keys():
       x +=h[o] 
    if o in v.keys():
       y +=v[o] 
    lt = (x, y)
    if robot:
        lr = lt
    else:
        l = lt
    BOARD[lt]+=1
    robot = not robot
print(f'part2: {len([ val for k,val in BOARD.items() if val > 0])}')
