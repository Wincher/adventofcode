import sys
steps = None
ZONES = []
grid = []
for line in open('4.in'):
    line = line.strip()
    if steps is None:
        steps = [int(x) for x in line.split(',')]
    else:
        if line:
            grid.append([int(x) for x in line.split()])
        else:
            if grid:
                ZONES.append(grid)
            grid = []
ZONES.append(grid)

MARK = []
# for z in ZONES:
#     MARK.append([[False for _ in range(5)] for _ in range(5)])
# for n in steps:
#     for i in range(len(ZONES)):
#         for x in range(5):
#             for y in range(5):
#                 if ZONES[i][x][y] == n:
#                     MARK[i][x][y] = True
#         won = False
#         for x in range(5):
#             ok = True
#             for y in range(5):
#                 if not MARK[i][x][y]:
#                     ok = False
#             if ok:
#                 won = True
#         for y in range(5):
#             ok = True
#             for x in range(5):
#                 if not MARK[i][x][y]:
#                     ok = False
#             if ok:
#                 won = True
#         if won:
#             count = 0
#             for x in range(5):
#                 for y in range(5):
#                     if not MARK[i][x][y]:
#                         count += ZONES[i][x][y]
#             print('part1:', count*n)
            # sys.exit(0)

MARK = []
WON = [False for _ in range(len(ZONES))]
for z in ZONES:
    MARK.append([[False for _ in range(5)] for _ in range(5)])
for n in steps:
    for i in range(len(ZONES)):
        for x in range(5):
            for y in range(5):
                if ZONES[i][x][y] == n:
                    MARK[i][x][y] = True
        won = False
        for x in range(5):
            ok = True
            for y in range(5):
                if not MARK[i][x][y]:
                    ok = False
            if ok:
                won = True
        for y in range(5):
            ok = True
            for x in range(5):
                if not MARK[i][x][y]:
                    ok = False
            if ok:
                won = True
        if won:
            WON[i] = True
            if all([WON[j] for j in range(len(ZONES))]):
                print(WON, i, n)
                count = 0
                for x in range(5):
                    for y in range(5):
                        if not MARK[i][x][y]:
                            count += ZONES[i][x][y]
                print('part2:', count*n)
                sys.exit()