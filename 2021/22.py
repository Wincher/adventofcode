from collections import defaultdict

S = set()
for line in open('../puzzleInput/2021/22.in'):
    line = line.strip().split()
    x_, y_, z_ = line[1].split(',')
    x_min, x_max = list(map(int, x_.split('=')[1].split('..')))
    y_min, y_max = list(map(int, y_.split('=')[1].split('..')))
    z_min, z_max = list(map(int, z_.split('=')[1].split('..')))
    if line[0].startswith('on'):
        f = S.add
    else:
        assert line[0].startswith('off')
        f = S.discard
        
    xl = [x for x in range(-50, 51) if x in range(x_min, x_max+1)]
    yl = [y for y in range(-50, 51) if y in range(y_min, y_max+1)]
    zl = [z for z in range(-50, 51) if z in range(z_min, z_max+1)]

    for x in xl:
        for y in yl:
            for z in zl:
                f((x,y,z))
print(f'part1: {len(S)}')

# python3 22.py  294.68s user 177.96s system 87% cpu 8:58.03 total
# takes too much time and too much mem
# after optimize using map istead of traversal array 208.29s user 2.94s system 99% cpu 3:31.75 total
steps = []
X, Y, Z=[], [], []
for line in open('../puzzleInput/2021/22.in'):
    line = line.strip().split()
    on = line[0].startswith('on')
    x_, y_, z_ = line[1].split(',')
    x_min, x_max = list(map(int, x_.split('=')[1].split('..')))
    y_min, y_max = list(map(int, y_.split('=')[1].split('..')))
    z_min, z_max = list(map(int, z_.split('=')[1].split('..')))
    x_max+=1
    y_max+=1
    z_max+=1

    steps.append((x_min, x_max, y_min, y_max, z_min, z_max, on))
    X.append(x_min)
    X.append(x_max)
    Y.append(y_min)
    Y.append(y_max)
    Z.append(z_min)
    Z.append(z_max)
X.sort()
Y.sort()
Z.sort()
xm = {x: i for i, x in enumerate(X)}
ym = {y: i for i, y in enumerate(Y)}
zm = {z: i for i, z in enumerate(Z)}
N = len(X)
grid = [[[False]*N for _ in range(N)] for _ in range(N)]

# remove after optimize, using map instead
# def get_index(arr, v):
#     for i,c in enumerate(arr):
#         if c >= v:
#             return i

for step in steps:
    # x0 = get_index(X, step[0])
    # x1 = get_index(X, step[1])
    # y0 = get_index(Y, step[2])
    # y1 = get_index(Y, step[3])
    # z0 = get_index(Z, step[4])
    # z1 = get_index(Z, step[5])

    for x in range(xm[step[0]], xm[step[1]]):
        for y in range(ym[step[2]], ym[step[3]]):
            for z in range(zm[step[4]], zm[step[5]]):
                grid[x][y][z] = step[6]

sum = 0
for x in range(N-1):
    for y in range(N-1):
        for z in range(N-1):
            if grid[x][y][z]:
                sum += (X[x+1] - X[x]) * (Y[y+1] - Y[y]) * (Z[z+1] - Z[z]) 
print(f'part2: {sum}')